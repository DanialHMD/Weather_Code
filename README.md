# Weather_Code

This code is an easy example of how to extract data from a website using python and beautifulsoup.
For the start we begin with adding `beautifulsoup` and `requests` to our code.

> For learning more visit [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [requests](https://requests.readthedocs.io/en/latest/)

```
import requests
from bs4 import BeautifulSoup as bs
```

With adding the required libraries we can officially begin the code.

You can either define a function for the process called `weather` or you can write the code simply.(your choice)
For accessing a website we use `requests.get(url)` and add the result to an object called `req` (the name is optional).
```
req=requests.get(f'https://www.google.com/search?q=weather+{city}',headers=headers)
```
you might wonder for a beginner that what is the `headers` part for?

the **headers** are the key values that are sent along with your request to server for accessing website.
(In this example you have to use it but in other cases you might not need it.)

Right now we need `User_Agent` to send to server so we can access it with this [link](http://httpbin.org/get).

```
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
```
So far so good. now we have to use beautifulsoup to find the data we want.
```
data=bs(req.text , 'html.parser')
```
with this easily we sort the source code so we can search through it.
```
time =  data.select('#wob_dts')[0].getText().strip()
info = data.select('#wob_dc')[0].getText().strip()
weather = data.select('#wob_tm')[0].getText().strip()
```
These are the data we want to extract. The `select` function finds all the matching scripts and adds theme to a list, what we need is the first index so we add a `[0]` after that. Then we call `getText()` function for extracting only strings and texts. Using `strip()` function is simple and it removes spaces before and after string, so you get a pure and solid string with no typing problems.

After that it's all printing the results.
```
print(time)
print(weather,'C°')
print(info)
```
