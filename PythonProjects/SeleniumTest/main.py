import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '186a1d926109bb0d04cb717411be3ed5'
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
Body_create = {
    "name": "Доби",
    "photo_id": 125
}
Body_put = {
    "pokemon_id": "44596",
    "name": "Доби Свободный",
    "photo_id": 125
}
Body_add_pokeball = {
    "pokemon_id": "44596"
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = Body_create)
print(response_create.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = Body_put)
print(response_put.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = Body_add_pokeball)
print(response_add_pokeball.text)