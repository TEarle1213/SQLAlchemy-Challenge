#Import python dependencies
import pandas as pd
import numpy as np
import datetime as dt 
#Import Flask
from flask import Flask, jsonify
#Import sqlalchemy 
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

#Read SQL into Pandas 
engine= create_engine("sqlite:///Resources/hawaii.sqlite")
#create tables 
Base= automap_base()
Base.prepare(engine, reflect=True)
#save each table
msmt=Base.classes.measurement
stn=Base.classes.station
#start session
session=Session(engine)

#create app
app=Flask(__name__)

#List all available routes
@app.route("/")
def welcome():
    return (
        f"Hawaiian Weather API<br/>"
        f"What would you like to know?<br/>"
        f"Precipitation data:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"List of Stations<br/>"
        f"/api/v1.0/stations<br/>"
        f"Most active station data:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Temperature information from a specified start date<br/>"
        f"/api/v1.0/temp_start<br/>"
        f"Temperature information for a specified date range<br/>"
        f"/api/v1.0/temp_start/end"
    )

#Define precipitation queries
@app.route("/api/v1.0/precipitation")
def precipitation():
    #only one year
    one_year=dt.date(2017,8,23) - dt.timedelta(days=365)
    scores=session.query(msmt.date, msmt.prcp).filter(msmt.date>=one_year).all()
    #save as a dictionary
    precip= {date:prcp for date, prcp in precipitation}
    #jsonified
    return jsonify(precip)

#Define station queries
@app.route("api/v1.0/stations")
def stations():
    stn_results=session.query(stn.station).all()
    #save as a list
    stations=list(np.ravel(stn_results))
    #jsonified
    return jsonify(stations=stations)

#Define TOBS queries
@app.route("api/v1.0/tobs")
def tobs():

#Define temperature queries with specified start date
def s_temps():    

#Define temperatures within specified start-to-end dates
@app.route("app/v1.0/temp_start/end")
def temps():    

