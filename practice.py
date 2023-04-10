import requests

api_key = '2f05f2cc-be6d-489d-a379-a5e848e8139c'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions :
    print(definition)