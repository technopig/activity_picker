from app import app
from flask import render_template, request
from weather import get_weather
from water_gauge import get_cfs_tomorrow
from avy import get_avy_frontrange

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Sam'
    }
    forecasts = []
    # boulder_forecast =
    forecasts.append(get_weather("40.0338,-105.2561", "Boulder"))
    # eldora_forecast =
    forecasts.append(get_weather("39.93646991379455,-105.58600635354678", "Eldora"))
    # water_info =
    forecasts.append(get_cfs_tomorrow("06730200", "Boulder Creek"))
    # avy_info =
    forecasts.append(get_avy_frontrange())
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
