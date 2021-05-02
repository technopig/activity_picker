from app import app
from flask import render_template, request
from weather import get_weather

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Sam'
    }
    # forecasts = [
    #     {
    #         'type': 'temp',
    #         'location': 'boulder',
    #         'value': 15
    #     },
    #     {
    #         'type': 'wind',
    #         'location': 'boulder',
    #         'value': [10, 11, 12, 13, ("EIGHT", 124)]
    #     }
    # ]
    boulder_forecast = get_weather("40.0338,-105.2561", "Boulder")
    return render_template('index.html', user=user, forecasts=[boulder_forecast])


@app.route('/weather')
def weather():
    user = {
        'username': 'Sam'
    }
    BOULDER_COORDINATES = "40.0338,-105.2561"
    ELDORA_COORDINATES = "39.93646991379455,-105.58600635354678"
    location = request.args.get('location')
    if location == 'boulder':
        weather_info = get_weather(BOULDER_COORDINATES)
    elif location == 'eldora':
        weather_info = get_weather(ELDORA_COORDINATES)
    else:
        return "invalid location"
    return render_template('base.html', user=user, temps=weather_info['temps'], winds=weather_info['winds'])
    # return render_template('weather.html', forecast_location='Boulder', temps=weather_info['temps'])
