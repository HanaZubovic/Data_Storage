# SQLAlchemy Challenge - Surfs Up!

### The Challenge

Using Python and SQLAlchemy, complete a climate analysis and data exploration of a climate database to find an ideal time to plan a trip to Honolulu, Hawaii. The analysis has to be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

## File Directory
- Resources folder contains both `.csv` and `.sqlite` data regarding information collected by weather stations in Hawaii.
- Data_Storage folder contains both the main python script and flask app
- `flask_app.py` contains sqlalchemy script for app routes
- `climate.ipynb` is the Jupyter Notebook with the main weather analysis and visualizations
- Images folder contains screenshots of some visualizations

## Process
- With Pandas, created a summary statistics for the precipitation and station data.
- Used Flask to create routes to API data and `jsonify` the API data into a valid JSON response object.
- Queried last 12 months of temperature data for specific weather stations 

### Precipitation Analysis

*The last 12 months of precipitation data queried. Selected only the `date` and `prcp` values.*
![precipitation](Images/precipitation.png)


### Station Analysis
*Queried the last 12 months of temperature observation data for the most active weather station.*
![station-histogram](Images/station-histogram.png)


### Script for Flask
*A screenshot of some of the code used to create a local host server with Flask.*
![flask](https://user-images.githubusercontent.com/16246354/156869898-ed793891-89b1-495a-bb19-7c1cb520da18.png)
