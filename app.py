from flask import Flask, redirect, jsonify
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
        <h1>Welcome to the Climate App</h1>
        <h4>Select one of the following routes:</h4>
        <ul>
            <li>/api/v1.0/precipitation</li>
            <li>/api/v1.0/stations</li>
            <li>/api/v1.0/tobs</li>
            <li>/api/v1.0/start-date-here</li>
            <li>/api/v1.0/start-date-here/end-date-here</li>
        </ul>    
    '''

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    return { date:val for date,val in session.query(Measurement.date,Measurement.prcp).all() }

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    return { station:name for station,name in session.query(Station.station,Station.name).all() }


@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    return { station:name for station,name in session.query(Measurement.tobs,Station.name).all() }


@app.route('/api/v1.0/start-date-here')
 def date(start):
    tmin = session.query(Measurement.tobs).order_by(Measurement.date).filter(Measurement.date > start).all()
    tmin = min(tmin)
    tmax = session.query(Measurement.tobs).order_by(Measurement.date).filter(Measurement.date > start).all()
    tmax = max(tmax)
    tavg = session.query(Measurement.date, Measurement.tobs).order_by(Measurement.date).filter(Measurement.date > start).all()
    start_avg = 0
    for row in tavg:
        start_avg += row[1]
    tavg_len = len(tavg)
    tavg_value = start_avg/tavg_len
    tmin_list = list(np.ravel(tmin))
    tmax_list = list(np.ravel(tmax))
    tavg_list = list(np.ravel(tavg_value))
    return jsonify(tmin_list, tmax_list, tavg_list)

@app.route('/api/v1.0/start-date-here/end-date-here')
def dates(start, end):
    # start = 
    # end =
    tmin = session.query(Measurement.tobs).order_by(Measurement.date).filter(end >= Measurement.date).filter(Measurement.date > start).all()
    tmin = min(tmin)
    tmax = session.query(Measurement.tobs).order_by(Measurement.date).filter(end >= Measurement.date).filter(Measurement.date > start).all()
    tmax = max(tmax)
    tavg = session.query(Measurement.date, Measurement.tobs).order_by(Measurement.date).filter(end >= Measurement.date).filter(Measurement.date > start).all()
    start_end_avg = 0
    for row in tavg:
        start_end_avg += row[1]
    tavg_len = len(tavg)
    tavg_value = start_end_avg/tavg_len
    tmin_list = list(np.ravel(tmin))
    tmax_list = list(np.ravel(tmax))
    tavg_list = list(np.ravel(tavg_value))
    return jsonify(tmin_list, tmax_list, tavg_list)

if __name__=='__main__':
    app.run(debug=True)