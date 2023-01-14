#Début de theHarvester

import os
import sys
import subprocess
import argparse

'''
def run_theharvester(options):
    try:
        subprocess.run(["python3","theHarvester.py"]+ options, check=True)
        print("[+] Informations collectées avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"[-] une erreur est apparue: {e}")
        return 1
    except FileNotFoundError as e:
        print(f"[-] theHarvester n'a pas été trouvé: {e}")
        return 1
    except Exception as e:
        print(f"[-] Une erreur inattendue est apparue: {e}")
        return 1
    return 0

def main():

    parser = argparse.ArgumentParser(description='Outil automatisé pour utiliser theHarvester')
    parser.add_argument('-d', '--domain', help='Domaine à chercher')
    parser.add_argument('-e', '--email', help='Email à chercher')
    parser.add_argument('-b', '--browsers', help='navigateurs à utiliser pour la recherche')
    parser.add_argument('-s', '--source', help='Source à utiliser')
    parser.add_argument('-l', '--limit', help='Nombre de résultats à afficher')
    parser.add_argument('-f', '--output', help='nom du fichier créé')
    parser.add_argument('-v', '--verbose', help='mode verbeux', action='store_true')
    args = parser.parse_args()

    options = []
    if args.domain:
        options += ['-d', args.domain]
    if args.email:
        options += ['-e', args.email]
    if args.browsers:
        options += ['-b', args.browsers]
    if args.source:
        options += ['-s', args.source]
    if args.limit:
        options += ['-l', args.limit]
    if args.output:
        options += ['-f', args.output]
    if args.verbose:
        options += ['-v']
    return run_theharvester(options)

if __name__ == "__main__":
    sys.exit(main())
'''


def theharvester():
	argscan = []
	while (1 not in argscan) or (1 in argscan):
		argscan = input("""
Quels arguments souhaitez-vous entrer dans votre commande ?
Entrez votre réponse comme ceci si vous souhaitez entrer plusieurs arguments : 1,3,8
Vous devez OBLIGATOIREMENT choisir le nombre 1 pour utiliser ce programme.

Voici les réponses possibles :
1. Scanner un domaine
2. Utiliser un navigateur : data source : baidu, bing, bingapi, dogpile, google, googleCSE, googleplus, google-profiles, linkedin, pgp, twitter, vhost,virustotal, threatcrowd, crtsh, netcraft, yahoo, all
3. Chercher une adresse email 
4. utilisation de shodan pour interroger les hôtes découverts
5. Nombre de résultats à afficher
6. Création d'un fichier XML et JSON de sortie 
7. Afficher le mode verbeux

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
            reponse = input("Quel navigateur souhaitez vous utiliser ?\nExemple : anubis, baidu, bevigil, binaryedge, bing, bingapi, bufferoverun, censys, certspotter, crtsh,dnsdumpster, duckduckgo, fullhunt,\ngithub-code, hackertarget, hunter, intelx,otx, pentesttools, projectdiscovery,qwant, rapiddns, rocketreach, securityTrails, sublist3r, threatcrowd, threatminer,urlscan, virustotal, yahoo, zoomeye \nVotre choix : ")
            PassingArguments += f'-b {reponse} '
            
		elif argscan[x] == 3 : # Sélection du mail à chercher
			reponse = input("Quel est le mail que vous souhaitez chercher ? :")
            PassingArguments += f'-e {reponse} '

		elif argscan[x] == 4 : # Utilisation de shodan
			PassingArguments += "-s "
		
		elif argscan[x] == 5 : # Nombre de résultats à afficher
            reponse = input("Quelle est la limite du nombre de résultats que vous souhaitez afficher? :")
			PassingArguments += f'-l {reponse} '

		elif argscan[x] == 6 : # Création d'un fichier de sortie
            reponse = input("Quel nom voulez vous donner à votre fichier ? :")
			PassingArguments += f'-f {reponse} '

		