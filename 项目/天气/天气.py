import pandas as pd
import requests

url = 'http://tianqi.2345.com/Pc/GetHistory'

headers = {
    'User-Agent': """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15"""
}

params = {
        'areaInfo[areaId]': 54511,
        'areaInfo[areaType]': 2,
        'date[year]': 2024,
        'date[month]': 2
    }

r = requests.get(url, headers=headers, params=params)
data = r.json()['data']
print(data)
