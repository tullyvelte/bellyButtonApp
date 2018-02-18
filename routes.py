# Import dependencies
import os
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Base definition
Base = automap_base()

# Create engine
dbpath = os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f'sqlite:///{dbpath}')

# Reflect the DB Tables
Base.prepare(engine, reflect=True)

# Create Sample Name variable
Sample = Base.classes.samples

# Create OTU variable
OTU = Base.classes.otu

#Create Samples Meta variable
Samples_meta = Base.classes.samples_metadata

#Create the Session
session = Session(engine)