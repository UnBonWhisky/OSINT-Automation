#Début de theHarvester

import os
import sys
import subprocess

def STRtoINT(argument):
	for x in range(len(argument)) :
		argument[x] = int(argument[x])
	return argument

def theharvester():
	argscan = []
	while (1 not in argscan) :
		argscan = input("""
Quels arguments souhaitez-vous entrer dans votre commande ?
Entrez votre réponse comme ceci si vous souhaitez entrer plusieurs arguments : 1,3,8
Vous devez OBLIGATOIREMENT choisir le nombre 1 pour utiliser ce programme.

Voici les réponses possibles :
1. Scanner un domaine
2. Utiliser un navigateur : data source : baidu, bing, bingapi, dogpile, google, googleCSE, googleplus, google-profiles, linkedin, pgp, twitter, vhost,virustotal, threatcrowd, crtsh, netcraft, yahoo, all
3. Utiliser un serveur de résolution DNS différent de celui du système
4. Vérifier le nom d'hôte via la résolution DNS et rechercher des hôtes virtuels
5. Nombre de résultats à afficher (par défaut 500)
6. Création d'un fichier XML et JSON de sortie 
7. Vérifier si des domaines découverts sont vulnérables à des prises de contrôle
8. Activer la recherche de serveur DNS
9. Réaliser une force brute DNS sur le domaine
10. Définir un numéro de départ pour les résultats de la recherche

Votre choix : """)

		argscan = argscan.split(',')
		argscan = STRtoINT(argscan)

	PassingArguments = ""
	for x in range(len(argscan)):
		
		if argscan[x] == 1 : # Si on ne veut scanner qu'un seul domaine
			reponse = input("Quel est le domaine que vous souhaitez scanner ? :")
			PassingArguments += f"-d {reponse} "
			OutputDomaine = reponse

		elif argscan[x] == 2 : # Ajout d'un navigateur
			reponse = input("Quel navigateur souhaitez vous utiliser ?\nExemple : anubis, baidu, bevigil, binaryedge, bing, bingapi, bufferoverun, censys, certspotter, crtsh, dnsdumpster, duckduckgo, fullhunt,\ngithub-code, hackertarget, hunter, intelx,otx, pentesttools, projectdiscovery,qwant, rapiddns, rocketreach, securityTrails,\nsublist3r, threatcrowd, threatminer,urlscan, virustotal, yahoo, zoomeye \nVotre choix : ")
			PassingArguments += f'-b {reponse} '

		elif argscan[x] == 3 : #Spécification d'un serveur DNS
			reponse = input("Quel serveur de résolution DNS souhaitez-vous utiliser ?\nExemple : 1.1.1.1 ou 8.8.8.8\nVotre choix : ")
			PassingArguments += f'-e {reponse} '

		elif argscan[x] == 4 : #Vérification du nom d'hôte via la résolution DNS
			PassingArguments += "-v "

		elif argscan[x] == 5 : # Nombre de résultats à afficher
			reponse = input("Quelle est la limite du nombre de résultats que vous souhaitez afficher? :")
			PassingArguments += f'-l {reponse} '

		elif argscan[x] == 6 : # Création d'un fichier de sortie
			reponse = input("Quel nom voulez vous donner à votre fichier ? :")
			PassingArguments += f'-f {reponse} '

		elif argscan[x] == 7 : #Vérification des takeovers
			PassingArguments += "-r "

		elif argscan[x] == 8 : #Activation de la recherche de serveur DNS
			PassingArguments += "-n "

		elif argscan[x] == 9 : #Réalisation de force brute
			PassingArguments += "-c "

		elif argscan[x] == 10 : # Numéro de départ pour les résultats de recherche
			reponse = input("A quel numéro souhaitez vous reprendre votre recherche ? :")
			PassingArguments += f'-S {reponse} '

	# Ajout du choix pour un affichage dans la console ou dans un fichier
	choix = None
	while choix is None:
		try:
			choix = int(input("Souhaitez-vous obtenir le rendu dans la console ou dans un fichier ?\n1. Fichier\n2. Console\nVotre choix : "))
			if choix not in [1,2] :
				raise Error
		except:
			print("\nVous n'avez pas entré un chiffre entre 1 et 2.\nMerci de réessayer.\n")
			choix = None

	if choix == 1:
		PassingArguments += f"-o \"{directory}/{OutputDomaine}/theharvester-{datetime.datetime.now().strftime('%d%m%y')}.txt\""

		subprocess.Popen(f"mkdir \"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(f"python3 theHarvester.py {PassingArguments}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		print("theharvester est en cours d'execution, si vous ne voyez pas de contenu dans le fichier généré, merci de patienter quelques instants.")
	
	else :
		subprocess.Popen(f"python3 theHarvester.py {PassingArguments}", shell=True).communicate()

	return

theharvester()
