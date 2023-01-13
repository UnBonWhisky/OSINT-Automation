import os, sys, subprocess
sys.path.append(os.path.join(os.path.dirname(__file__))) # Ajout de l'emplacement du fichier au PATH pour le programme

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
        
programnumber = start()

if programnumber == 1 :
    subprocess.Popen("python3 dnscan/dnscan.py", shell=True)