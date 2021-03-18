import requests
import json
from datetime import datetime

api_key = '123456789'

#Zhytomyr
lat = '50.2649'
lon = '28.6767'

lang = 'ru'
units = 'metric'
exclude = 'minutely,hourly,alerts'
error = 'Ошибка получения данных :-('

def weather_3_days ():
    def weather_today ():
        weather_url = requests.get ('http://api.openweathermap.org/data/2.5/onecall?' , params = {'lat' : lat, 'lon' : lon, 'exclude' : exclude, 'units' : units, 'appid' : api_key, 'lang' : lang})
        json_item = json.loads(weather_url.text)
        try:
            today = json_item["daily"][0]
            today_date = datetime.fromtimestamp(today["dt"]).strftime('%d-%m-%Y')
            weather_today = ('Сегодня ' + today_date + ':' + '\n' +
                    today["weather"][0]["description"].capitalize() + '\n' +
                    'Температура днем: ' + str (int (today["temp"]["day"])) + ' ℃' + '\n' +
                    'Температура ночью: ' + str (int (today["temp"]["night"])) + ' ℃' + '\n' +
                    'Ветер: ' + str (int (today["wind_speed"] * 3.6))  + ' km/h')
            return weather_today
        except:
            weather_today = error
            return weather_today

    def weather_tomorrow ():
        weather_url = requests.get ('http://api.openweathermap.org/data/2.5/onecall?' , params = {'lat' : lat, 'lon' : lon, 'exclude' : exclude, 'units' : units, 'appid' : api_key, 'lang' : lang})
        json_item = json.loads(weather_url.text)
        try:
            tomorrow = json_item["daily"][1]
            tomorrow_date = datetime.fromtimestamp(tomorrow["dt"]).strftime('%d-%m-%Y')
            weather_tomorrow = ('\n' 'Завтра ' + tomorrow_date + ':' + '\n' +
                tomorrow["weather"][0]["description"].capitalize() + '\n' +
                'Температура днем: ' + str (int (tomorrow["temp"]["day"])) + ' ℃' + '\n' +
                'Температура ночью: ' + str (int (tomorrow["temp"]["night"])) + ' ℃' + '\n' +
                'Ветер: ' + str (int (tomorrow["wind_speed"] * 3.6))  + ' km/h')
            return weather_tomorrow
        except:
            weather_tomorrow = error
            return weather_tomorrow

    def weather_day_after_tomorrow ():
        weather_url = requests.get ('http://api.openweathermap.org/data/2.5/onecall?' , params = {'lat' : lat, 'lon' : lon, 'exclude' : exclude, 'units' : units, 'appid' : api_key, 'lang' : lang})
        json_item = json.loads(weather_url.text)
        try:
            day_after_tomorrow =  json_item["daily"][2]
            day_after_tomorrow_date = datetime.fromtimestamp(day_after_tomorrow["dt"]).strftime('%d-%m-%Y')
            weather_day_after_tomorrow = ('\n' 'Послезавтра ' + day_after_tomorrow_date + ':' + '\n' +
                day_after_tomorrow["weather"][0]["description"].capitalize() + '\n' +
                'Температура днем: ' + str (int (day_after_tomorrow["temp"]["day"])) + ' ℃' + '\n' +
                'Температура ночью: ' + str (int (day_after_tomorrow["temp"]["night"])) + ' ℃' + '\n' +
                'Ветер: ' + str (int (day_after_tomorrow["wind_speed"] * 3.6))  + ' km/h' )
            return weather_day_after_tomorrow
        except:
            weather_day_after_tomorrow = error
            return weather_day_after_tomorrow

    return weather_today () + '\n' + weather_tomorrow () + '\n' + weather_day_after_tomorrow ()