import requests

def get_weather(city, api_key):
    # 1. This URL is exactly what n8n builds behind the scenes
    # 'units=metric' gives us Celsius instead of Fahrenheit
    url = f"http://openweathermap.org{city}&appid={api_key}&units=metric"
    
    # 2. This is the 'Execute' step. It sends the request to the internet.
    response = requests.get(url)
    
    # 3. Check if the 'handshake' worked (Status Code 200 = Success)
    if response.status_code == 200:
        data = response.json()  # This turns the raw text into a 'Dictionary' (JSON)
        
        # 4. We 'drill down' into the data just like your 'Edit Fields' node
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        
        return f"Currently in {city}, it is {temp}°C with {description}."
    else:
        return f"Failed! Error code: {response.status_code}. Check your API Key."

# --- TESTING THE SCRIPT ---
# Replace 'YOUR_API_KEY_HERE' with the key you get from OpenWeatherMap
MY_KEY = "YOUR_API_KEY_HERE"
print(get_weather("Dar es Salaam", MY_KEY))

