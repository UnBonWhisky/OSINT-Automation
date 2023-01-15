import os, sys, subprocess, datetime
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
			choix = int(input("\nQuel programme souhaitez-vous lancer ?\n1. DNSCan\n2. Shodan\n3. theHarvester\n4. URLScan.io\n5. Google-Dorks\n6. Quitter\nVotre choix : "))
			if choix < 1 or choix > 6 :
				raise Exception
		except:
			print("\nVous n'avez pas entré un chiffre entre 1 et 6.\nMerci de réessayer.\n")
			choix = None
	return choix

def STRtoINT(argument):
	for x in range(len(argument)) :
		argument[x] = int(argument[x])
	return argument

def OutputScan(NomProgramme, OutputDomaine, commande):
    # Ajout du choix pour un affichage dans la console ou dans un fichier
	choix = None
	while choix is None:
		try:
			choix = int(input("Souhaitez-vous obtenir le rendu dans la console ou dans un fichier ?\n1. Fichier\n2. Console\nVotre choix : "))
			if choix not in [1,2] :
				raise Exception
		except:
			print("\nVous n'avez pas entré un chiffre entre 1 et 2.\nMerci de réessayer.\n")
			choix = None

	if choix == 1:
		commande += f"-o \"{directory}/output/{OutputDomaine}/{NomProgramme}-{datetime.datetime.now().strftime('%d%m%y')}.txt\""

		if os.name == 'nt':
			subprocess.Popen(f"mkdir output\\\"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			subprocess.Popen(f"python3 {commande}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()

		else:
			subprocess.Popen(f"mkdir -p output/\"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			subprocess.Popen(f"python3 {commande}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()

		print(f"\n{NomProgramme} vient de terminer son execution, vous pouvez observer les résultats\nLe fichier est situé dans output/\"{OutputDomaine}/dnscan-{datetime.datetime.now().strftime('%d%m%y')}.txt\"")

	else :
		subprocess.Popen(f"python3 {commande}", shell=True).communicate()

	return

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
3. Utiliser une liste de sous-domaines personnalisée (avec un fichier .txt)
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
     
		if argscan[x] == 1 : # Si on ne veut scanner qu'un seul domaine
			reponse = input("Quel est le domaine que vous souhaitez scanner : ")
			PassingArguments += f"-d {reponse} "
			OutputDomaine = reponse

		elif argscan[x] == 2 : # Si on veut scanner plusieurs domaines
			ListeFichiers = []
			for filename in os.listdir(directory):
				if filename.endswith('.txt'):
					ListeFichiers.append(filename)
			print(f"Voici la liste des fichiers txt trouvés dans {directory}.\nLequel contient votre liste de noms de domaines ?")
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
   
			with open(f'{directory}/{ListeFichiers[reponse]}') as f:
				OutputDomaine = f.readline().strip("\n")
				OutputDomaine = f'{OutputDomaine} and more'

		elif argscan[x] == 3 : # Ajout d'une wordlist personnalisée
			ListeFichiers = []
			for filename in os.listdir(directory):
				if filename.endswith('.txt'):
					ListeFichiers.append(filename)
			for filename in os.listdir(f"{directory}/dnscan"):
				if filename.startswith('subdomains'):
					ListeFichiers.append(f"dnscan/{filename}")
			print(f"Voici la liste des fichiers txt trouvés dans {directory}.\nLes fichiers de dnscan par défaut sont aussi affichés.\nLequel contient votre liste de sous-domaines ?")
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
			PassingArguments += f"-w {directory}/{ListeFichiers[reponse]} "

		elif argscan[x] == 4 : # Sélection du nombre de threads
			reponse = None
			while reponse is None:
				try:
					reponse = int(input("Combien de threads souhaitez-vous utiliser à la fois ? (1-32, 8 par défaut)\nVotre choix : "))
					if reponse < 1 or reponse > 32 :
						raise Exception
				except:
					print("\nVous n'avez pas entré un chiffre entre 1 et 32.\nMerci de réessayer.\n")
					reponse = None
			PassingArguments += f"-t {reponse} "
		
		elif argscan[x] == 5 : # Ajout de la recherche IPv6
			PassingArguments += "-6 "
		
		elif argscan[x] == 6 : # Tentative du transfert de zone
			PassingArguments += "-z "

		elif argscan[x] == 7 : # Recursivité de la recherche des sous-domaines
			PassingArguments += '-r '

		elif argscan[x] == 8 : # Scan des sous-domaines avec alteration
			PassingArguments += '-a '
	
		elif argscan[x] == 9 : # Spécification d'un serveur DNS
			reponse = input("Quel serveur de résolution DNS souhaitez-vous utiliser ?\nExemple : 1.1.1.1 ou 8.8.8.8\nVotre choix : ")
			PassingArguments += f'-R {reponse} '

		elif argscan[x] == 10 : # Spécification de plusieurs serveurs DNS
			ListeFichiers = []
			for filename in os.listdir(directory):
				if filename.endswith('.txt'):
					ListeFichiers.append(filename)
			print(f"Voici la liste des fichiers txt trouvés dans {directory}.\nLequel contient votre liste de serveurs DNS ?")
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
			PassingArguments += f"-L {directory}/{ListeFichiers[reponse]} "

		elif argscan[x] == 11 : # Scanner le domaine dans tous les DNS de 1er niveau
			PassingArguments += "-T "
   
		elif argscan[x] == 12 : # Ne pas checker les serveurs de nom avant le scan
			PassingArguments += "-n "
   
		elif argscan[x] == 13 : # Ne scanner que les zones de transfert et les sous-domaines
			PassingArguments += '-q '
   
		elif argscan[x] == 14 : # Ne pas afficher les adresses IP dans le rendu
			PassingArguments += '-q '
   
		elif argscan[x] == 15 : # Activer le mode verbeux
			PassingArguments += '-v '

	# Ajout du choix pour un affichage dans la console ou dans un fichier
	OutputScan("DNSCan", OutputDomaine, f"dnscan/dnscan.py {PassingArguments}")

	return


def shodan():
	choix = None
	while choix is None :
		try: 
			choix = int(input("""
Pour utiliser Shodan nous avons besoin d'une adresse IP ou d'un nom de domaine exacte
Veuillez taper :
1. Avoir des informations sur une adresse IP
2. Avoir des informations sur un nom de domaine
Votre choix : """))
			if choix not in [1,2]:
				raise Exception
		except :
			print("Vous n'avez pas entré un nombre dans l'intervale 1-2")
			choix = None
	PassingArguments = ""
	if choix == 1 : # Si on choisit de fournir un adresse IP
		reponse = None
		while reponse is None :
			try :
				reponse = input('Veuillez entrer l\'adresse IPv4 de votre choix : ')
				IPreponse = reponse.split(".")

				for x in range(len(IPreponse)):
					IPreponse[x] = int(IPreponse[x])

				if len(IPreponse) != 4:
					raise Exception
			except:
				print("Vous n'avez pas rentré une adresse IPv4 correcte.")
				reponse = None
		PassingArguments += f"-i {reponse} "

	if choix == 2 : # Si on choisit de fournir un nom de domaine
		reponse = input('Veuillez entrer le nom de domaine de votre choix : ')
		PassingArguments += f"-d {reponse} "

	# Ajout du choix pour un affichage dans la console ou dans un fichier
	OutputScan("Shodan", reponse, f"shodan/shodan-io.py {PassingArguments}")

	return

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
11. Utiliser des proxies pour les requêtes effectués

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

		elif argscan[x] == 11 : # Utilisation de proxies
			ListeFichiers = []
			for filename in os.listdir(directory):
				if filename.endswith('.yaml'):
					ListeFichiers.append(filename)
			print(f"Voici la liste des fichiers .yaml trouvés dans {directory}.\nLequel contient votre liste de proxies ?")
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
			PassingArguments += f"-p {directory}/{ListeFichiers[reponse]} "
   
			with open(f'{directory}/{ListeFichiers[reponse]}') as f:
				proxies = f.readline().strip("\n")
				proxies = f'{proxies} and more'		

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
		PassingArguments += f"-o \"{directory}/{OutputDomaine}/theHarvester.py-{datetime.datetime.now().strftime('%d%m%y')}.txt\""

		subprocess.Popen(f"mkdir \"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(f"python3 theharvester/theHarvester.py {PassingArguments}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		print("theharvester est en cours d'execution, si vous ne voyez pas de contenu dans le fichier généré, merci de patienter quelques instants.")
	
	else :
		subprocess.Popen(f"python3 theharvester/theHarvester.py {PassingArguments}", shell=True).communicate()

	return

def programme():
	ALancer = 0
	while ALancer != 6 :
		ALancer = start()
		if ALancer == 1 :
			dnscan()
		elif ALancer == 2 :
			shodan()
		elif ALancer == 3 :
			theharvester()

programme()