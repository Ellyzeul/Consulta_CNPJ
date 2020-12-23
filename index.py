# apikey is a local file with my personal token to Sintegra API
from apikey import apikey
import requests


test_cnpj = '06990590000123'

url = "https://www.sintegraws.com.br/api/v1/execute-api.php"
querystring = {"token":apikey,"cnpj":test_cnpj,"plugin":"ST"}
response = requests.request("GET", url, params=querystring)

st_response = response.json()

print(st_response)