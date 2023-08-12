import requests

token = 'токен'
host = 'https://api.pokemonbattle.me:9104'

response_create_pokemon = requests.post(f'{host}/pokemons', json = {
   "name": "Буся",
   "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response_create_pokemon.text)

response_change_pokemon_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6116",
    "name": "Busya",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}, headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response_change_pokemon_name.text)

response_catch_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6116"
}, headers = {'trainer_token' : token, 'Content-Type' : 'application/json'})

print(response_catch_pokemon.text)