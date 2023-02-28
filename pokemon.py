import requests
import concurrent.futures


def get_pokemons_urls():
    URL = "https://pokeapi.co/api/v2/"

    data = list()

    response = requests.get(f"{URL}/pokemon/?limit=500&offeset=0").json()
    return response["results"]


def send_request(url: str):
    return requests.get(url).json()


def get_pokemons_details(pokemons_url: list):
    print(pokemons_url)
    data = list()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = list()

        for url in pokemons_url:
            futures.append(executor.submit(send_request, url=url["url"]))

        for future in concurrent.futures.as_completed(futures):
            data.append(future.result())

    return data


urls = get_pokemons_urls()
data = get_pokemons_details(urls)
print(data)
