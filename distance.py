import requests

def get_distance(origin, destination, api_key):
    # 1. Prepare the URL for Google's Distance Matrix API
    # 'units=metric' ensures the result is in kilometers
    url = f"https://googleapis.com{origin}&destinations={destination}&units=metric&key={api_key}"

    # 2. Execute the request
    response = requests.get(url)
    data = response.json()

    # 3. Check if the API request was successful
    if data['status'] == 'OK':
        # Navigate the JSON structure to find distance and duration
        element = data['rows'][0]['elements'][0]
        
        if element['status'] == 'OK':
            distance = element['distance']['text']
            duration = element['duration']['text']
            return f"The distance from {origin} to {destination} is {distance}, and it will take about {duration} by car."
        else:
            return f"No route found between {origin} and {destination}."
    else:
        return f"Error: {data.get('error_message', 'Invalid request')}"

# --- TESTING THE SCRIPT ---
# Use the API key you generated in the Google Cloud Console
GOOGLE_KEY = "YOUR_GOOGLE_API_KEY_HERE"
print(get_distance("Dar es Salaam", "Arusha", GOOGLE_KEY))

