# Weather Forecast App

This project provides a simple Python application to fetch and display weather forecasts for any city using the [Open-Meteo API](https://open-meteo.com/). It includes both a command-line backend and a graphical user interface (GUI) built with Tkinter.

## Features

- Get latitude and longitude for any city using OpenStreetMap Nominatim.
- Fetch hourly temperature forecasts for up to 48 hours.
- User-friendly GUI to select city and forecast duration.
- Results displayed in a sortable table.

## Requirements

- Python 3.8+
- [openmeteo-requests](https://pypi.org/project/openmeteo-requests/)
- pandas
- requests
- requests-cache
- retry-requests
- tkinter (included with standard Python installations)

Install dependencies with:

```
pip install openmeteo-requests pandas requests requests-cache retry-requests
```

## Usage

### GUI

Run the GUI application:

```
python gui.py
```

- Enter a city name (e.g., "Frankfurt am Main").
- Enter the number of hours for the forecast (1-48).
- Click "Get Forecast" to view hourly temperature data.

### Backend

You can also use the functions in `weather.py` directly:

```python
from weather import get_location_by_city, fetch_weather

lat, lon = get_location_by_city("Frankfurt am Main")
df = fetch_weather(lat, lon, 12)
print(df)
```

## File Structure

- `weather.py`: Contains functions for location lookup and weather data fetching.
- `gui.py`: Tkinter GUI for user interaction and displaying results.
- `README.md`: Project documentation.

## Notes

- The app uses OpenStreetMap Nominatim for geocoding. Please respect their usage policy.
- Weather data is fetched from Open-Meteo and cached locally for efficiency.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
