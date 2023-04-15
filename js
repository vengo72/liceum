import json
import requests


with open('light.json') as file:
    data = json.load(file)
    api_server = f'http://{data["server"]}:{data["port"]}'
    response = requests.get(api_server)
    json_response = response.json()
    print(json_response)
