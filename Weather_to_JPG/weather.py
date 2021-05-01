import sys
from PyQt5.QtWidgets import QDesktopWidget,QApplication
from PIL import ImageDraw, ImageFont, Image
import requests
import json
from datetime import datetime

app = QApplication(sys.argv)
q = QDesktopWidget().availableGeometry()
api_key = ''
city_id ='686967'
lang = 'ru'
units = 'metric'
#celsium = bytes.fromhex('E2 84 83').decode('utf-8')

error = 'Ошибка получения данных :-('
weather_url = requests.get ('http://api.openweathermap.org/data/2.5/weather' , params = {'id' : city_id , 'units' : units, 'appid' : api_key, 'lang' : lang})
json_item = json.loads(weather_url.text)



img = Image.new('RGB', (q.width(), q.height()), color=('#FAACAC'))
font = ImageFont.truetype('arial.ttf', 30, index=0, encoding='unic')
weather_text = ImageDraw.Draw(img)
try:
    city = json_item['name']
    sky = (json_item['weather'][0]['description']).capitalize()
    humidity = 'Влажность: ' + str (int (json_item['main']['humidity'])) + '%'
    temp = 'Температура: ' + str (int (json_item['main']['temp'])) + ' C'
    feels_like = 'Ощущается как: ' + str (int (json_item['main']['feels_like']))
    date = 'Обновлено: ' + datetime.fromtimestamp(json_item['dt']).strftime('%d-%m-%Y %H:%M:%S')
    wind_spped = 'Ветер: ' + str (int (json_item['wind']['speed'] * 3.6))  + ' km/h'



    weather_text.text((895, 100), city, fill=('#1C0606'), font=font)
    weather_text.text((895, 800), city + '\n' + sky + '\n' + humidity + '\n' + temp + '\n' + feels_like + '\n' + date + '\n' + wind_spped, fill=('#1C0606'), font=font)
except:
    weather_text.text(((q.width() / 2) - 200, q.height() / 2), error, fill=('#1C0606'), font=font)

img.save('pic.jpg')