from geopy.geocoders import Nominatim

### POBIERANIE WSPÓŁRZĘDNYCH ###
def get_cordinates (address):
    geolocator = Nominatim(user_agent='my_geocoder')
    location = geolocator.geocode(address)

    latitude, longitude = location.latitude, location.longitude
    return latitude, longitude