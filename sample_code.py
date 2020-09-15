import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://forecast.weather.gov/MapClick.php?lat=47.61099000000007&lon=-122.33588999999995#.X2DW8JMzbfA'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
forecasts = soup.find_all(class_="tombstone-container")

period_names, short_desc, temp = [], [], []

for forecast in forecasts:
    period_names.append(forecast.find(
        class_="period-name").get_text().encode('utf-8'))
    short_desc.append(forecast.find(
        class_="short-desc").get_text().encode('utf-8'))
    temp.append(forecast.find(class_="temp").get_text().encode('utf-8'))

weather_details = pd.DataFrame(
    {
        'Period': period_names,
        'Short Description': short_desc,
        'Temperature': temp
    }
)

print(weather_details)
weather_details.to_csv('weather.csv')
