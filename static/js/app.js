function init() {
    var queryURL = "/names";
    d3.json(queryURL, function (error, response) {
        if (error) return console.warn(error);
        for (var i = 0; i < response.length; i++) {
            var select = document.getElementById('dropdown');
            option = document.createElement('option');
            option.value = response[i]; 
            option.text = response[i];
            select.appendChild(option);
        }

        pieChart();
        bubbleChart();
    });
}

function pieChart() {
    sample = document.getElementById('pie').options[0].value;
    var url = "/samples/" + sample;
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var layout = {showlegend: false};
        response.type = 'pie';
        Plotly.newPlot('pie', [response], layout);
        Plotly.restyle('pie', 'labels', response.labels)
        Plotly.restyle('pie', 'values',response.values);
    });
}

function bubbleChart() {
    sample = document.getElementById('bubble').options[0].value;
    var url = "/samples/" + sample;
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var trace1 = {
          x: response.labels,
          y: response.values,
          mode: 'markers',
          marker: {
            size: response.values
          }
        };
        var layout = {
        showlegend: false,
        xaxis: {
        showticklabels: false
        }};
        Plotly.newPlot('bubble', [trace1], layout);
        Plotly.restyle('bubble', 'x', [response.labels])
        Plotly.restyle('bubble', 'y',[response.values]);
    });
}

function updatePie(sample) {
    var url = "/samples/" + sample;
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        response.type = 'pie';
        Plotly.restyle('pie', 'labels', [response.labels])
        Plotly.restyle('pie', 'values', [response.values]);
    });
}
function updateBubble(sample) {
        var url = "/samples/" + sample;
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        Plotly.restyle('bubble', 'x', [response.labels])
        Plotly.restyle('bubble', 'y',[response.values]);
    });
}

function updatePanel(sample) {
    var obj = document.getElementById('meta');
    var queryURL = "/metadata/" + sample;
    d3.json(queryURL, function (error, response) {
        if (error) return console.warn(error);
        Object.keys(response).forEach(function(key) {
        obj.innerText +=  "" + key + ' : ' + response[key] + "\n";
        })
    });
}
function optionChanged() {
    var sample = document.getElementById('dropdown').value
    updatePie(sample);
    updateBubble(sample);
    updatePanel(sample);
}

init();