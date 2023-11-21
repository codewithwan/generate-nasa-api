# NASA APOD API Wrapper

This Python class, `NASAAPI`, provides a simple way to interact with NASA's Astronomy Picture of the Day (APOD) API.


## API Reference

#### Get API

```http
  https://api.nasa.gov
```

## Usage

#### Get an API Key

Before using this class, you need to obtain an API key from NASA's API portal here.

#### Instantiate the NASAAPI class
```python
from NASAAPI import NASAAPI

# Replace 'YOUR_API_KEY' with your actual API key
nasa = NASAAPI(api_key='YOUR_API_KEY')
```

#### Retrieve the Astronomy Picture of the Day (APOD)
```python
apod_data = nasa.get_apod()

# Access APOD information
if apod_data:
    print("Information about Astronomy Picture of the Day (APOD):")
    print("Title:", apod_data.get('title'))
    print("Date:", apod_data.get('date'))
    print("Explanation:", apod_data.get('explanation'))
    print("URL:", apod_data.get('url'))
else:
    print("Failed to fetch APOD data.")
```

#### Display the APOD Image
```python
apod_data = nasa.get_apod()

# Access APOD information
nasa.show_apod_image()
```