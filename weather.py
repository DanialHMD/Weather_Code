import requests 
from bs4 import BeautifulSoup as bs

def weather(city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req=requests.get(f'https://www.google.com/search?q=weather+{city}',headers=headers)
    data=bs(req.text , 'html.parser')

    time =  data.select('#wob_dts')[0].getText().strip()
    info = data.select('#wob_dc')[0].getText().strip()
    weather = data.select('#wob_tm')[0].getText().strip()

    print(time)
    print(weather,'C°')
    print(info)

city=input('Enter your city:')
weather(city)