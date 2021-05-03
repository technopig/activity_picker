import hydrofunctions as hf
from datetime import date, timedelta
import datetime
import json


def get_cfs_tomorrow(creek_water_gauge_num, location):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    # print(today)

    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    # print(yesterday)

    two_days_ago = date.today() - timedelta(days=2)
    two_days_ago = two_days_ago.strftime('%Y-%m-%d')
    # print(two_days_ago)

    start = two_days_ago
    end = yesterday

    herring = hf.NWIS(creek_water_gauge_num, 'dv', start, end)
    herring.get_data()

    cfs_yesterday = float(herring.json()['value']['timeSeries'][0]['values'][0]['value'][1]['value'])
    cfs_two_days_ago = float(herring.json()['value']['timeSeries'][0]['values'][0]['value'][0]['value'])
    # print(f"Yesterday: {cfs_yesterday}")
    # print(f"Two days ago: {cfs_two_days_ago}")
    diff = cfs_yesterday - cfs_two_days_ago
    # print(f"Difference = {round(diff,1)} cfs (positive numbers mean rising cfs)")

    MAX_CFS = 300
    MIN_CFS = 100
    cfs_tomorrow = cfs_yesterday + 2*diff
    condition = 'none'
    # print(f"CFS Tomorrow will be around {round(cfs_tomorrow,2)}:")
    if (MAX_CFS > cfs_tomorrow > MIN_CFS):
        # print("\t- Just right.")
        condition = 'good'
    elif (cfs_tomorrow < MIN_CFS):
        # print("\t- Too low.")
        condition = 'too low'
    elif (cfs_tomorrow > MAX_CFS):
        # print("\t- Too high.")
        condition = 'too high'
    else:
        print("\tThere's something wrong with your logic if you're seeing this.")

    return {
            "location": location,
            "value": f"{cfs_tomorrow} CFS - {condition}",
            "type": 'Water Gauge'
        }


if __name__ == '__main__':
    BOULDER_75TH_GAUGE = '06730200'
    # Boulder Creek at 75th - https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=06730200
    abc = get_cfs_tomorrow(BOULDER_75TH_GAUGE, 'boulder creek at 75th')
    print(abc)
