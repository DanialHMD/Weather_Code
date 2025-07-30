import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import requests
from datetime import datetime, timedelta


def get_location():
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    lat, lon = map(float, data["loc"].split(","))
    city = data.get("city", "Unknown")
    return lat, lon, city


def get_location_by_city(city):
    """Get latitude and longitude for a given city name."""
    try:
        response = requests.get("https://nominatim.openstreetmap.org/search",
                                params={
                                    "q": city,
                                    "format": "json",
                                    "limit": 1
                                },
                                headers={"User-Agent": "weather-app"})
        data = response.json()
        if not data:
            return None, None
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon
    except Exception:
        return None, None


def fetch_weather(lat, lon, hours):
    """Fetch weather forecast for the next `hours` hours."""
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    now = datetime.utcnow()
    start_date = now.strftime("%Y-%m-%d")
    end_date = (now + timedelta(hours=hours)).strftime("%Y-%m-%d")

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "start_date": start_date,
        "end_date": end_date,
        "timezone": "UTC"
    }

    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_data = {
            "date":
            pd.date_range(start=pd.to_datetime(hourly.Time(),
                                               unit="s",
                                               utc=True),
                          end=pd.to_datetime(hourly.TimeEnd(),
                                             unit="s",
                                             utc=True),
                          freq=pd.Timedelta(seconds=hourly.Interval()),
                          inclusive="left"),
            "temperature_2m":
            hourly_temperature_2m
        }
        df = pd.DataFrame(data=hourly_data)
        return df
    except Exception:
        return None