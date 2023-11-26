import os
from dotenv import load_dotenv
import googlemaps

load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')

gmaps = googlemaps.Client(key=api_key)

print('Welcome to the Geocoding API Application! Give it a try below!')
country = input('Enter country: ')
city = input('Enter city: ')
street = input('Enter street, neighborhood or specified address: ')

geocode_result = gmaps.geocode(f'{street}, {city}, {country}')

print('-' * 40)
for i in range(len(geocode_result)):
    result = geocode_result[i]
    formatted_address = result['formatted_address']
    location = result['geometry']['location']

    print(f'Address: {formatted_address}')
    print(f'Latitude: {location["lat"]}, Longitude: {location["lng"]}')
    print('-' * 40)
