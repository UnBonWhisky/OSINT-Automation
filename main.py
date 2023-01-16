import os, sys, subprocess, datetime, requests, json, colorama
directory = os.path.join(os.path.dirname(__file__))
sys.path.append(directory) # Ajout de l'emplacement du fichier au PATH pour le programme

file = open("data.json", 'r+', encoding="utf-8") # On ouvre le fichier JSON
data = json.load(file)

def save_auth(key, value): # On sauvegarde les clés d'API
    data[key] = value
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()

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

def OutputScan(NomProgramme, OutputDomaine, commande, argumentOutput):
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
		if NomProgramme == "urlscan":
			if os.name == "nt":
				subprocess.Popen(f"mkdir output\\\"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()
			else:
				subprocess.Popen(f"mkdir -p output/\"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()

			with open(f"{directory}/output/{OutputDomaine}/{NomProgramme}-{datetime.datetime.now().strftime('%d%m%y')}.txt", 'w+', encoding='utf-8') as f :
				f.write(commande)
				f.close()
		else:
			commande += f"{argumentOutput} \"output/{OutputDomaine}/{NomProgramme}-{datetime.datetime.now().strftime('%d%m%y')}.txt\""

			if os.name == 'nt':
				subprocess.Popen(f"mkdir output\\\"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()
				subprocess.Popen(f"py -3 {commande}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()

			else:
				subprocess.Popen(f"mkdir -p output/\"{OutputDomaine}\"", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()
				subprocess.Popen(f"python3 {commande}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()

		print(f"\n{NomProgramme} vient de terminer son execution, vous pouvez observer les résultats\nLe fichier est situé dans output/{OutputDomaine}/{NomProgramme}-{datetime.datetime.now().strftime('%d%m%y')}\"")

	else :
		if NomProgramme == "urlscan":
			print(f"\nL'URL de votre résultat est disponible ici :\n{commande}")
		else:
			if os.name == 'nt':
				subprocess.Popen(f"py -3 {commande}", shell=True). communicate()
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
		if len(argscan) > 0 and argscan[0] != '' :
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
	OutputScan("DNSCan", OutputDomaine, f"dnscan/dnscan.py {PassingArguments}", '-o')

	return


def shodan():
	# Import de la clé d'API de l'utilisateur pour faire fonctionner Shodan
	if data["shodankey"] is None :
		cle = input("""
Merci d'entrer votre clé d'API pour faire fonctionner shodan.
Attention, vous ne pourrez pas la modifier en cas de non fonctionnement de celle-ci.
Vous devrez refaire l'entièreté du container (si Docker), ou modifier le fichier en lignes de commandes. (le fichier est data.json)
Votre clé : """)

		save_auth("shodankey", cle)
 
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
	OutputScan("Shodan", reponse, f"shodan/shodan-io.py {PassingArguments}", '-o')

	return

def theharvester():
	argscan = []
	argscan = input(f"""
Quels arguments souhaitez-vous entrer dans votre commande ?
Entrez votre réponse comme ceci si vous souhaitez entrer plusieurs arguments : 1,3,8

Voici les réponses possibles :
1. Choix du navigateur (certains navigateurs nécessitent une clé d'API à entrer dans le fichier suivant : {directory}/theHarvester/api-keys.yaml )
2. Utiliser un serveur de résolution DNS différent de celui du système
3. Vérifier le nom d'hôte via la résolution DNS et rechercher des hôtes virtuels
4. Nombre de résultats à afficher (par défaut 500)
5. Vérifier si des domaines découverts sont vulnérables à des prises de contrôle
6. Activer la recherche de serveur DNS
7. Réaliser une force brute DNS sur le domaine
8. Définir un numéro de départ pour les résultats de la recherche
9. Utiliser des proxies pour les requêtes effectuées (Ajoutez un fichier proxies.yaml à la racine du dossier ou utiliser celui dans le dossier theharvester)
Votre choix : """)

	argscan = argscan.split(',')
	if len(argscan) > 0 and argscan[0] != '' :
		argscan = STRtoINT(argscan)

	PassingArguments = ""
	reponse = input("Quel est le domaine que vous souhaitez scanner ? : ") # Obligatoirement ajout d'un domaine
	PassingArguments += f"-d {reponse} "
	OutputDomaine = reponse

	for x in range(len(argscan)):
		if argscan[x] == 1 : # Ajout d'un navigateur
			Navigateurs = ["all", "anubis", "baidu", "bevigil\t\t(Nécessite une clé d'API)", "binaryedge\t\t(Nécessite une clé d'API)", "bing", "bingapi\t\t(Nécessite une clé d'API)", "bufferoverun\t\t(Nécessite une clé d'API)", "censys\t\t(Nécessite une clé d'API)", "certspotter", "crtsh", "dnsdumpster", "duckduckgo", "fullhunt\t\t(Nécessite une clé d'API)","github-code\t\t(Nécessite une clé d'API)", "hackertarget", "hunter\t\t(Nécessite une clé d'API)", "intelx\t\t(Nécessite une clé d'API)", "otx", "pentesttools\t(Nécessite une clé d'API)", "projectdiscovery\t(Nécessite une clé d'API)", "qwant", "rapiddns", "rocketreach\t\t(Nécessite une clé d'API)", "securityTrails\t(Nécessite une clé d'API)", "sublist3r", "threatcrowd", "threatminer", "urlscan", "virustotal\t\t(Nécessite une clé d'API)", "yahoo", "zoomeye\t\t(Nécessite une clé d'API)"]
			print("Quel navigateur souhaitez vous utiliser ?")
			for x in range(len(Navigateurs)):
				print(f"{x+1}. {Navigateurs[x]}")
			reponse = None
			while reponse is None:
				try:
					reponse = int(input("Votre choix : "))
					if reponse < 1 or reponse > len(Navigateurs) :
						raise Exception
				except :
					print(f"Ce nombre n'est pas dans la liste, choisissez un nombre dans l'intervale 1-{len(Navigateurs)}")
					reponse = None
			reponse = Navigateurs[reponse-1]
			reponse = reponse.split('\t')[0]
			PassingArguments += f'-b {reponse} '

		elif argscan[x] == 2 : #Spécification d'un serveur DNS
			reponse = input("Quel serveur de résolution DNS souhaitez-vous utiliser ?\nExemple : 1.1.1.1 ou 8.8.8.8\nVotre choix : ")
			PassingArguments += f'-e {reponse} '

		elif argscan[x] == 3 : #Vérification du nom d'hôte via la résolution DNS
			PassingArguments += "-v "

		elif argscan[x] == 4 : # Nombre de résultats à afficher
			reponse = input("Quelle est la limite du nombre de résultats que vous souhaitez afficher ? (500 par défaut)\nVotre choix : ")
			PassingArguments += f'-l {reponse} '

		elif argscan[x] == 5 : #Vérification des takeovers
			PassingArguments += "-r "

		elif argscan[x] == 6 : #Activation de la recherche de serveur DNS
			PassingArguments += "-n "

		elif argscan[x] == 7 : #Réalisation de force brute
			PassingArguments += "-c "

		elif argscan[x] == 8 : # Numéro de départ pour les résultats de recherche
			reponse = input("A quel numéro souhaitez vous reprendre votre recherche ?\nVotre choix : ")
			PassingArguments += f'-S {reponse} '

		elif argscan[x] == 9 : # Utilisation de proxies
			PassingArguments += "-p "

	# Ajout du choix pour un affichage dans la console ou dans un fichier
	OutputScan("theHarvester", OutputDomaine, f"theharvester/theHarvester.py {PassingArguments}", "-f")

	return

def urlscan():
	# Récupération de la clé d'API urlscan
	if data["urlscankey"] is None :
		cle = input("""
Merci d'entrer votre clé d'API pour faire fonctionner URLScan.
Attention, vous ne pourrez pas la modifier en cas de non fonctionnement de celle-ci.
Vous devrez refaire l'entièreté du container (si Docker), ou modifier le fichier en lignes de commandes. (le fichier est data.json)
Votre clé : """)
		save_auth("urlscankey", cle)

		data["urlscankey"] = cle

	headers = {'API-Key': data["urlscankey"], 'Content-Type':'application/json'}

	url = input("Entrez l'URL à scanner : ")
	jsondata = {"url": url, "visibility": "public"}

	response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(jsondata))

	if response.status_code != 200:
		print("La clé d'API ou le lien scanné est incorrect.")
	else:
		OutputScan("urlscan", url, response.json()['result'], None)

def GoogleDorks():
	argscan = []
	argscan = input("""
Quels arguments souhaitez-vous entrer dans votre commande ?
Entrez votre réponse comme ceci si vous souhaitez entrer plusieurs arguments : 1,3,8

Voici les réponses possibles :
1. Spécifier un nom de domaine pour définir la recherche Google dork
2. Le délai minimum entre les recherches de dork, en secondes. Doit être supérieur à 0 (par défaut 37)
3. Le délai maximum entre les recherches dorks, en secondes. Doit être supérieur à 0 (par défaut 60)
4. Désactiver la validation SSL/TLS. Parfois nécessaire si vous utilisez un proxy HTTPS avec des certificats auto-signés
5. Le nombre maximum de résultat de recherche url à retourner par dork, doit être supérieur à 0 (par défaut 100)
6. Une chaîne de proxy séparées par des virgules. Exemple :  https://myproxy:8080,socks5h://127.0.0.1:9050,socks5h://127.0.0.1:9051
Votre choix : """)

	argscan = argscan.split(',')
	if len(argscan) > 0 and argscan[0] != '' :
		argscan = STRtoINT(argscan)
    
	PassingArguments = ""

	# Passage d'un google dorks (obligatoire)
	ListeFichiers = []
	reponse = print("Voici les différents Google Dorks qui sont disponibles :")
	for filename in os.listdir(f"{directory}/google-dorks/dorks"):
		if filename.endswith('.txt') or filename.endswith('.dorks'):
			ListeFichiers.append(filename)

	for x in range(len(ListeFichiers)):
		print(f"{x+1}. {ListeFichiers[x]}")

	reponse = None
	while reponse is None :
		try:
			reponse = int(input("Quel fichier souhaitez-vous utiliser ?\nVotre choix : "))
			if reponse < 1 or reponse > len(ListeFichiers) :
				raise Exception
		except:
			print(f"Vous n'avez pas entré un nombre entre 1 et {len(ListeFichiers)}\n")
			reponse = None

	PassingArguments += f"-g {directory}/google-dorks/dorks/{ListeFichiers[reponse-1]} "

	if 1 not in argscan :
		OutputDomaine = "google-dorks.result"

	for x in range(len(argscan)):

		if argscan[x] == 1 : # Pour spécifier un nom de domain afin de définir la recherche google dork
			reponse = input("Quel est le nom de domaine que vous souhaitez spécifier : ")
			PassingArguments += f"-d {reponse} "
			OutputDomaine = reponse
		
		elif argscan[x] == 2 : # Pour définir un délai minimum entre les recherches
			reponse = input("Quel est le délai minimum que vous voulez avoir (en secondes) : ")
			PassingArguments += f"-i {reponse} "
		
		elif argscan[x] == 3 : # Pour définir un délai maximum entre les recherches
			reponse = input("Quel est le délai maximum que vous voulez avoir (en secondes) : ")
			PassingArguments += f"-x {reponse} "
		
		elif argscan[x] == 4 : # Pour désactiver la validation SSL/TLS
			PassingArguments += "-l "
		
		elif argscan[x] == 5 : # Pour définir un nombre maximum de résultats de recherche url effectuer par dork
			reponse = input("Quel est le nombre de résultats attendus (doit être supérieur à 0) : ")
			PassingArguments += f"-m {reponse} "
		
		elif argscan[x] == 6 : # Pour définir une chaine de plusieurs prxy à la fois
			reponse = input("Quels sont les proxy que vous voulez utiliser (lien url): ")
			PassingArguments += f"-p {reponse} "

	# Ajout du choix pour un affichage dans la console ou dans un fichier
	OutputScan("google-dorks", OutputDomaine, f"google-dorks/pagodo.py {PassingArguments}", '-s')

	return

def programme():
	ALancer = 0
	while ALancer != 6 :
		print(colorama.Style.RESET_ALL + colorama.Fore.RESET + colorama.Back.RESET, end="")
		ALancer = start()
		if ALancer == 1 :
			dnscan()
		elif ALancer == 2 :
			shodan()
		elif ALancer == 3 :
			theharvester()
		elif ALancer == 4 :
			urlscan()
		elif ALancer == 5 :
			GoogleDorks()

programme()