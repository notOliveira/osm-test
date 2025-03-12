import requests, json

def get_lat_lon(address):
    API_KEY = "CqlpfhTNJXi4I8voW5hp2kLcnnK65wuwp7IvWKMqUrY"
    url = f"https://geocode.search.hereapi.com/v1/geocode?apiKey={API_KEY}&q={address}"
    # print(url)
    # url = "https://geocode.search.hereapi.com/v1/geocode?apiKey=CqlpfhTNJXi4I8voW5hp2kLcnnK65wuwp7IvWKMqUrY&q=Rua Marisa Prado 16, Jardim Orly"
    response = requests.get(url)
    data = response.json()
    # print json with 4 indentations
    print(json.dumps(data, indent=4))
    items = data.get('items')
    if items:
        return items[0]['position']['lat'], items[0]['position']['lng']
    else:
        return

# Exemplo de uso
address = input("Digite o endereço: ") # Rua Marisa Prado 16, Jardim Orly, São Paulo
lat, lon = get_lat_lon(address)

if lat and lon:
    print(f"{lat} {lon}")
else:
    print("Endereço não encontrado!")