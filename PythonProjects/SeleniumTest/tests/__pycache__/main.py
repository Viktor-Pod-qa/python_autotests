import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '186a1d926109bb0d04cb717411be3ed5'
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
TRAINER_ID = '4131'




def test_status_code():
    response = requests.get(url= f'{URL}\trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 404
