import requests
import json
from datetime import date, timedelta, datetime
from matplotlib import pyplot as plt
from operator import itemgetter


API_URL = "https://api.weather.gov/points/"


def get_weather(coordinates, loc_name):
    forecast_url = API_URL + coordinates
    overview_page = json.loads(requests.get(forecast_url).text)
    hourly_target_url = json.dumps(overview_page['properties']['forecastHourly'], indent=4)[1:-1]
    forecast_page = json.loads(requests.get(hourly_target_url).text)
    # print(f"Hourly target url: {hourly_target_url}")
    hourly_forecast = forecast_page['properties']['periods']
    # print(f"Hourly forecast: {hourly_forecast}")
    tomorrow = datetime.today() + timedelta(days=1)
    temps = []
    winds = []
    for h in hourly_forecast:
        hour_dt = datetime.strptime(h['startTime'][:-9], '%Y-%m-%dT%H:%M')
        if hour_dt.date() == tomorrow.date():
            # print(hour_dt)
            # print(f"Temperature: {h['temperature']}")
            # print(f"Wind Speed: {h['windSpeed'].split()[0]}")
            temps.append((h['startTime'], int(h['temperature'])))
            winds.append((h['startTime'], int(h['windSpeed'].split()[0])))

    forecast = {
        'type': 'Weather',
        'location': loc_name,
        'value': f"Max Temp:  {max(temps,key=itemgetter(1))[1] } <br/>" + \
                   f"Min Temp: {min(temps,key=itemgetter(1))[1]} <br/>" + \
                   f"Max Wind: {max(winds,key=itemgetter(1))[1]} <br/>" + \
                   f"Min Wind: {min(winds,key=itemgetter(1))[1]}"
    }
    # return {'temps': temps, 'winds': winds}
    return forecast

if __name__ == '__main__':
    BOULDER_URL = API_URL + BOULDER_COORDINATES
    BOULDER_COORDINATES = "40.0338,-105.2561"
    abc = get_weather(BOULDER_COORDINATES)
    print(abc)
