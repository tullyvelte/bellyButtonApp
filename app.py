# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
from routes import session, Samples, OTU, Samples_meta

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Routes
#################################################

# Main route
@app.route('/')
def home():
    return render_template('index.html')

# Names Route - return list of names
@app.route('/names')
def names():
    sample_names = Samples.__table__.columns.keys()
    del sample_names[0]
    return jsonify(sample_names)

# OTU route - return list of descriptions
@app.route('/otu')
def otu():
    otu_desc = session.query(Samples_otu.lowest_taxonomic_unit_found).all()

    otu_desc_list = []

    for each in otu_query:
        otu_desc_list.append(each[0])
    return jsonify(otu_desc_list)

# Sample_meta route - return a dictionary of metadata
@app.route('/metadata/<sample>')
def metadata(sample):
    sample = sample.lstrip('BB_')
    
    meta_data = (session
                .query(Sample_meta)
                .filter(Sample_meta.SAMPLEID == sample))
    
    for result in meta_data:
        metadata_dict = {
            "AGE": result.AGE,
            "BBTYPE": result.BBTYPE,
            "ETHNICITY": result.ETHNICITY,
            "GENDER": result.GENDER,
            "LOCATION": result.LOCATION,
            "SAMPLEID": result.SAMPLEID,
        }
        
    return jsonify(metadata_dict)

# Wash Frequency Route - return a value as number
@app.route('/wfreq/<sample>')
def wfreq(sample):
    sample = sample.lstrip('BB_')
    
    wfreq_query = (session
                  .query(Sample_meta.WFREQ)
                  .filter(Sample_meta.SAMPLEID == sample).all())
    
    wfreq_query_results = []
    for result in results:
        wfreq_results = {}
        wfreq_results[sample] = int(result[0])
        wfreq_query_results.append(wfreq_results)
        
    return jsonify(wfreq_results)

# OTU ID/Values route - return dictionary of OTU ids and values(DESC order)
@app.route('/samples/<sample>')
def samples(sample):
    
    sample_query = session.query(Sample.otu_id, getattr(Sample, sample))
    
    sample_query = sorted(sample_query, key=lambda x: x[1], reverse=True)
    
    sample_dict = {
        "OTU_ids": [otu[0] for otu in sample_query],
        "sample_values": [otu[1] for otu in sample_query]
    }
    
    return jsonify(sample_dict)

if __name__ == "__main__":
    app.run(debug=True)

