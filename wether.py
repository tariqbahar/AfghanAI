import requests

api_key = 'YOUR_API_KEY'
city_name = 'Kabul'  # Replace with the name of the city in Afghanistan

url = 'https://api.openweathermap.org/data/2.5/weather?q=kabul&appid=b6cb829dd19a410ea359cd9e0bbbefad'
try:
    res = requests.get(url)
    res.raise_for_status()  # Raise HTTPError for bad responses
    data = res.json()
    # Process weather data here
except requests.exceptions.RequestException as e:
    print("Error fetching data from API:", e)
except json.decoder.JSONDecodeError as e:
    print("Error decoding JSON:", e)
