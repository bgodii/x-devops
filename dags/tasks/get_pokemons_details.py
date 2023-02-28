from airflow.decorators import task
import requests
import concurrent.futures


def send_request(url: str):
    return requests.get(url).json()


@task
def get_pokemons_details(pokemons_url: list):
    data = list()

    for url in pokemons_url:
        data.append(requests.get(url["url"]).json())

    return data
