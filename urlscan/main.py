import os
import sys
import subprocess
import argparse
import requests
import json

'''clé API():
    #Pour que le script puisse utiliser l'API urlscan
    URLSCAN_API_KEY = "ddda4437-7896-4b73-906a-7e2a9c231c37"'''


def urlscan():
    # Récupération de la clé d'API urlscan
    api_key = input("Entrez votre clé d'API urlscan : ")
    headers = {'API-Key': api_key, 'Content-Type':'application/json'}
    url = input("Entrez l'URL à scanner : ")
    data = {"url": url, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
    print(response.json())

urlscan()
