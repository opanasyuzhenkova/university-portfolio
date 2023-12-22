from urllib import request
from datetime import timezone, timedelta
from collections import defaultdict
import json

res_dict = defaultdict(
  lambda: {
    'name': 0,
    'coord': {
      'lon': 0,
      'lat': 0
    },
    'country': 0,
    'feels_like': 0,
    'timezone': 0
  })


def get_weather_data(place, api_key=None):
  with request.urlopen(
      f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
  ) as f:
    res = f.read().decode('utf-8')
    res_obj = json.loads(res)
    #print(res_obj)

    for id in res_obj:
      if id == 'name':
        res_dict['name'] = res_obj[id]
      if id == 'coord':
        res_dict['coord'] = res_obj[id]
      if id == 'timezone':
        res_dict['timezone'] = str(timezone(timedelta(seconds=res_obj[id])))
      if id == 'sys':
        for elem in res_obj[id]:
          if elem == 'country':
            res_dict['country'] = res_obj[id][elem]
      if id == 'main':
        for elem in res_obj[id]:
          if elem == 'feels_like':
            res_dict['feels_like'] = round(res_obj[id][elem] - 273.15, 2)
    #print(res_dict)
    #print(res_obj)

  print(json.dumps(res_dict))
  with open('result.json', 'w') as f:
    json.dump(res_dict, f, ensure_ascii=False, indent=4)
