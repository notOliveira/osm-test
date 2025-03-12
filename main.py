from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_lat_lon(address):
    geolocator = Nominatim(user_agent="meu_projeto_mapa")
    
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Exemplo de uso
endereco = input("Digite o endereço: ")
lat, lon = get_lat_lon(endereco)
print(f"{lat} {lon}")