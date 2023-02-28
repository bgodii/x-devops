from airflow.decorators import task
import requests


@task
def get_pokemons_urls():
    URL = "https://pokeapi.co/api/v2/"

    response = requests.get(f"{URL}/pokemon/?limit=500&offset=0").json()
    return response["results"]
