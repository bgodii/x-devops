from airflow.decorators import task
import requests


@task
def get_pokemons_urls():
    URL = "https://pokeapi.co/api/v2/"

    data = list()

    response = requests.get(f"{URL}/pokemon/").json()
    data.extend(response["results"])

    while response.get("next"):
        response = requests.get(response.get("next")).json()
        data.extend(response["results"])

    print(data)
    return data
