# *********************************** Module 9.5.1 ***********************
# import our dependencies.
import datetime as dt
import numpy as np
import pandas as pd

# import dependencies needed for SQLAlchemy.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import dependencies needed for Flask.
from flask import Flask, jsonify

# Set up database engine for the Flask application.
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

# reflect the database.
Base.prepare(engine, reflect=True)

# Create variable for each of the classes.
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database.
session = Session(engine)

# define our Flask app.
app = Flask(__name__)

# *********************************** Module 9.5.2 ***********************

# Create/define the welcome Flask route.
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# *********************************** Module 9.5.3 ***********************
# # Next route will return the 
# # precipitation data (precipitation analysis) for the last year. 

@app.route("/api/v1.0/precipitation")

# Create the precipitation() function.

# Calculate date 1 year ago from most recent date in database.
# Write a query to get date & precipitation for previous year.

# Create a dictionary with the date as the key and the
# precipitation as the value by "jsonify" our dictionary.

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# *********************************** Module 9.5.4 ***********************

# New Route - return a list of all the stations.
# Define route & route name.

@app.route("/api/v1.0/stations")

# Create new function called stations().

# Create query to get all of the stations in our database.
#   Unravel results into a one-dimensional array, using the
#   np.ravel() function, with "results" as the parameter.
#     THEN convert unraveled results into a list(),
#     THEN jsonify list and return it as JSON.

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# *********************************** Module 9.5.5 ***********************

# New Route - return temperature observations for the previous year.
# Define route & route name.

@app.route("/api/v1.0/tobs")

# Create new function called temp_monthly().

# Calculate date 1 year ago from most recent date in database.
# Create query the primary station for all temperature observations from the previous year.
#   Unravel results into a one-dimensional array, using the np.ravel() function.
#     THEN convert unraveled results into a list(),
#     THEN jsonify list and return it as JSON.


def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# *********************************** Module 9.5.6 ***********************

# New Route - return minimum, maximum, and average temperatures.
# Define route & route name for Start AND End.

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create new function called stats().
# Add a start AND an end parameter to stats() function.

# Create query to select the min, avg, and max temperatures from our SQLite database.
#   Create list called sel.
# Add if-not statement to determine the start and end date.
#     THEN convert Unravel results into a 1-dimensional array, then convert to list(),
#     THEN jsonify list and return it as JSON.
# Using sel list, Calculate min avg and max temps WITH the start and end dates.
# Create ANOTHER query to collect statistics data.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


# make sure to hv this at the END of ALL routes
if __name__ == "__main__":
    app.run(debug=True)