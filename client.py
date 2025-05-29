import requests

url = "http://localhost:8000/"

try:
    response = requests.get(url)
    response.raise_for_status() 
    print(response.json())       
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête : {e}")
