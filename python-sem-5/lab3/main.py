#from owm_key import owm_api_key
from getweatherdata import get_weather_data
import os

owm_api_key = os.environ['owm_api_key']

if __name__ == '__main__':
  get_weather_data('Moscow', api_key=owm_api_key)
  get_weather_data('Chicago', api_key=owm_api_key)
  get_weather_data('Sankt-Peterburg', api_key=owm_api_key)
  
