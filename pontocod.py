import requests

def get_cities(client_token, page_number):
    url = f"https://api.pontomais.com.br/external_api/v1/cities"
    headers = {
        "access-token": client_token
    }
    params = {
        "attributes": "id,name",
        "name": "sorocaba",
        "page": page_number,
        "per_page": 10,
        "sort_direction": "asc"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro na solicitação: {response.status_code} - {response.text}")
        return None

client_token = "$2a$12$aSBGbCTl7Jgy9do0Xuw1FOde1T/k8v01WBwLebgaUqQiasxZJFSdu"
page_number = 1

cities_data = get_cities(client_token, page_number)

if cities_data:
    print(cities_data)
