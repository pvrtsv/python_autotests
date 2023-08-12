import requests
import pytest

token = 'токен'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : '1264'})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('name', 'Буся'), ('trainer_id', '1264'), ('attack', '1.0')])

def test_trainer_id_check(key, value):
    response = requests.get(f'{host}/pokemons', params= {'trainer_id' : '1264'})
    assert response.json()[0][key] == value