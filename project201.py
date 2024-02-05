import requests



pokemon = input("Select a Pokemon: ").lower()


req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

if req.status_code != 404:
    pokemon = req.json()

    print(f"Pokemon ID: {pokemon['id']}")
    print(f"Pokemon's Name: {pokemon['name']}")
    print("Pokemon Type/s:")
    for type in pokemon['types']:
        typeUrl = type['type']
        req = requests.get(typeUrl['url'])
        typeName = req.json()
        print(typeName['name'])
else:
    print(f"{pokemon} is not a valid pokemon")