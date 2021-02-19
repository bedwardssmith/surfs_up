# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
# add SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# import the dependencies required for Flask
from flask import Flask, jsonify
# create database engine
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect the database into our classes
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# create variables for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to database
session = Session(engine)
# set up flask app
app = Flask(__name__)
# define welcome route
@app.route("/")
# Create a function welcome with a return statement
def welcom():
    return(
    '''
    Welcom to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temps/start/end
    ''')
# Create the precipitation route
@app.route("/api/v1.0/precipitation")
# Create precipiation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
# Create the stations route
@app.route("/api/v1.0/stations")
# Create stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
#Create the temperatures route
@app.route("/api/v1.0/tobs")
# Create temperature function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
# Create statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Create a stats function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)