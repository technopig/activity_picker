from app import app
from flask import render_template, request
from weather import get_weather
from water_gauge import get_cfs_tomorrow
from avy import get_avy_frontrange
import logging
import json_log_formatter
import random

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/Users/sam.cipriani/github/activity_picker/activity_picker.log')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Sam'
    }
    if random.randint(1,1000) < 50:
        raise Exception("I am a fake error.")
        logger.error('Fake error encountered.')
        return "Error"
    else:
        forecasts = []
        # boulder_forecast =
        forecasts.append(get_weather("40.0338,-105.2561", "Boulder"))
        logger.info('Got weather', extra={'location': 'Boulder', 'value': forecasts[len(forecasts)-1]})
        # eldora_forecast =
        forecasts.append(get_weather("39.93646991379455,-105.58600635354678", "Eldora"))
        logger.info('Got weather', extra={'location': 'Eldora', 'value': forecasts[len(forecasts)-1]})
        # water_info =
        forecasts.append(get_cfs_tomorrow("06730200", "Boulder Creek"))
        logger.info('Got water info', extra={'location': 'Boulder Creek', 'value': forecasts[len(forecasts)-1]})
        # avy_info =
        forecasts.append(get_avy_frontrange())
        logger.info('Got Avy info', extra={'location': 'Front Range', 'value': forecasts[len(forecasts)-1]})
        return render_template('index.html', user=user, forecasts=forecasts)

#
# @app.route('/weather')
# def weather():
#     user = {
#         'username': 'Sam'
#     }
#     BOULDER_COORDINATES = "40.0338,-105.2561"
#     ELDORA_COORDINATES = "39.93646991379455,-105.58600635354678"
#     location = request.args.get('location')
#     if location == 'boulder':
#         weather_info = get_weather(BOULDER_COORDINATES)
#     elif location == 'eldora':
#         weather_info = get_weather(ELDORA_COORDINATES)
#     else:
#         return "invalid location"
#     return render_template('base.html', user=user, temps=weather_info['temps'], winds=weather_info['winds'])
#     # return render_template('weather.html', forecast_location='Boulder', temps=weather_info['temps'])
