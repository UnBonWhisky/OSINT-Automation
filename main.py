import os, sys, subprocess
directory = os.path.join(os.path.dirname(__file__))
sys.path.append(directory) # Ajout de l'emplacement du fichier au PATH pour le programme

print("""
    +===================================================================+
    |       ____  _____ _       __                                      |
    |      / __ \/ ___/(_)___  / /_                                     |
    |     / / / /\__ \/ / __ \/ __/                                     |
    |    / /_/ /___/ / / / / / /_                                       |
    |    \____//____/_/_/ /_/\__/                                       |
    |                                                                   |
    |        ___         __                        __  _                |
    |       /   | __  __/ /_____  ____ ___  ____ _/ /_(_)___  ____      |
    |      / /| |/ / / / __/ __ \/ __ `__ \/ __ `/ __/ / __ \/ __ \     |
    |     / ___ / /_/ / /_/ /_/ / / / / / / /_/ / /_/ / /_/ / / / /     |
    |    /_/  |_\__,_/\__/\____/_/ /_/ /_/\__,_/\__/_/\____/_/ /_/      |
    |                                                                   |
    +===================================================================+
""")
print("""
    Bonjour !
    Bienvenue sur le script d'automatisation OSINT de :
    - Amine LACHGAR (@Marokingu)
    - Alexi LOREAUX (@alexilrx)
    - Flavien FOUQUERAY (@ffouqueray)
""")

def start():
	choix = None
	while choix is None:
		try:
			choix = int(input("Quel programme souhaitez-vous lancer ?\n1. DNSCan\n2. Shodan\n3. theHarvester\n4. URLScan.io\nVotre choix : "))
		except:
			print("\nVous n'avez pas entré un chiffre entre 1 et 4.\nMerci de réessayer.\n")
	return choix

def STRtoINT(argument):
	for x in range(len(argument)) :
		argument[x] = int(argument[x])
	return argument

def dnscan():
	argscan = []
	while (1 not in argscan and 2 not in argscan) or (1 in argscan and 2 in argscan):
		argscan = input("""
Quels arguments souhaitez-vous entrer dans votre commande ?
Entrez votre réponse comme ceci si vous souhaitez entrer plusieurs arguments : 1,3,8
Vous devez OBLIGATOIREMENT choisir le nombre 1 OU le nombre 2 pour utiliser ce programme.

Voici les réponses possibles :
1. Scanner un domaine
2. Scanner une liste de domaines (avec un fichier .txt)
3. Utiliser une liste de mots personnalisée (avec un fichier .txt)
4. Threads à utiliser à la fois (entre 1 et 32, 8 par défaut)
5. Scanner les adresses IPv6
6. Effectuer un transfert de zone et quitter
7. Scanner les sous-domaines de manière récursive
8. Scan des alterations au niveau des noms de sous-domaines
9. Utiliser un serveur de résolution DNS différent de celui du système
10. Utiliser une liste de serveurs de résolution DNS (avec un fichier .txt)
11. Scanner le domaine auprès de tous les domaines de premier niveau
12. Ne pas checker les serveurs de nom avant le scan
13. Ne scanner que les zones de transfert et les sous-domaines
14. Ne pas afficher les adresses IP dans le rendu
15. Afficher le mode verbeux

Votre choix : """)
    
		argscan = argscan.split(',')
		argscan = STRtoINT(argscan)
    
	PassingArguments = ""
	for x in range(len(argscan)):
     
		if argscan[x] == 1 :
			reponse = input("Quel est le domaine que vous souhaitez scanner : ")
			PassingArguments += f"-d {reponse} "

		elif argscan[x] == 2 :
			ListeFichiers = []
			for filename in os.listdir(directory):
				if filename.endswith('.txt'):
					ListeFichiers.append(filename)
			print(f"Voici la liste des fichiers txt trouvés dans {directory}. Lequel choisissez-vous pour votre attaque ?")
			for x in range(len(ListeFichiers)):
				print(f"{x+1}. {ListeFichiers[x]}")
			try:
				reponse = int(input('Votre choix : '))
			except:
				reponse = -1

			while reponse < 1 or reponse > len(ListeFichiers) :
				try:
					reponse = int(input(f"Vous n'avez pas choisi un nombre dans l'intervale 1-{len(ListeFichiers)}.\nFaites votre choix : "))
				except:
					reponse = -1
			reponse -= 1
			PassingArguments += f"-l {directory}/{ListeFichiers[reponse]} "

		elif argscan[x] == 3 :
dnscan()