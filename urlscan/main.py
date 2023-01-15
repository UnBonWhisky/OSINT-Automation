import os
import sys
import subprocess
import argparse
import requests
import json

'''def urlscan():
    #Pour que le script puisse utiliser l'API urlscan
    URLSCAN_API_KEY = "ddda4437-7896-4b73-906a-7e2a9c231c37"'''


'''def scan_url(url, visibility='public', apikey=None):
    headers = {'Content-Type':'application/json'}
    if apikey:
        headers.update({'API-Key': apikey})

    data = {"url": url, "visibility": visibility}
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    return response.json()

# Utilisation de la fonction scan_url
result = scan_url("https://flavien-fouqueray.fr/", apikey='ddda4437-7896-4b73-906a-7e2a9c231c37')
print(result)
'''

def scan_url():
    # Récupération de la clé d'API urlscan
    api_key = input("Entrez votre clé d'API urlscan : ")
    headers = {'API-Key': api_key, 'Content-Type':'application/json'}
    url = input("Entrez l'URL à scanner : ")
    data = {"url": url, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    print(response.json())

scan_url()
