from airflow.decorators import task
import requests


@task
def get_pokemons_details(pokemon_url: list):
    return requests.get(pokemon_url).json()
