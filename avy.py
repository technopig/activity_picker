from bs4 import BeautifulSoup
import requests
import re

def get_avy_frontrange():
    location = "Front Range Colorado"
    type = "Avalanche"
    avy_page = requests.get("https://www.avalanche.state.co.us/caic/pub_bc_avo.php?zone_id=1").content
    avy_soup = BeautifulSoup(avy_page, 'html.parser')
    result = avy_soup.find(id='avalanche-forecast')
    danger_elems = result.find_all('td', class_='today-text')
    summary = str(result.find('div', class_='row').find_all('p')[0])[3:-4]
    tomorrow_above = str(danger_elems[1].find('strong'))
    tomorrow_near = str(danger_elems[3].find('strong'))
    tomorrow_below = str(danger_elems[5].find('strong'))
    tomorrow_above = int(re.search(r"\(([A-Za-z0-9_]+)\)", tomorrow_above).group(1))
    tomorrow_near = int(re.search(r"\(([A-Za-z0-9_]+)\)", tomorrow_near).group(1))
    tomorrow_below = int(re.search(r"\(([A-Za-z0-9_]+)\)", tomorrow_below).group(1))

    value = f"Above: {tomorrow_above}<br>" + \
            f"Near: {tomorrow_near}<br>" + \
            f"Below: {tomorrow_below}<br>" + \
            f"Summary: {summary}"

    return {
        'location': location,
        'type': type,
        'value': value
    }
