'''
import subprocess
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__))) # Ajout de l'emplacement du fichier au PATH pour le programme


# Définit l'email ou le domaine de la cible
cible = input("Entrer le domaine ou l'email de la cible : ")

# Création du répertoire pour le résultat
resulat_directory = f"{cible}_resultat"
os.mkdir(resultat_directory)

# Menu pour sélectionner l'outil à utiliser
print("Sélectionne l'outil à utiliser:")
print("1. Dnsscan")
print("2. Shodan")
print("3. TheHarvester")
print("4. Urlscan.io")

# Récupérer le choix réalisé
choix = input()
'''

#Début de theHarvester

import subprocess
import sys,os

# Entrée du nom de domaine
domaine = input("Entre le domaine de la cible : ")

# Entrée du nombre maximum de recherches via GOOGLE
limite = input("Entre le nombre maximum de résultats de recherches Google : ")

# test de lancement de theHarvester via subprocess
cherche_domaine = subprocess.run(["theharvester", "-d", domaine, "-b", "google", "-l", limite], capture_output=True, text=True)
print(cherche_domaine.stdout)

