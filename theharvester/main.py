#Début de theHarvester
'''
import subprocess
import sys,os

# Entrée du nom de domaine
domaine = input("Entre le domaine de la cible : ")

# Entrée du nombre maximum de recherches via GOOGLE
limite = input("Entre le nombre maximum de résultats de recherches Google : ")

# test de lancement de theHarvester via subprocess
cherche_domaine = subprocess.run(["theHarvester.py", "-d", domaine, "-b", "google", "-l", limite], capture_output=True, text=True)
print(cherche_domaine.stdout)
'''
'''
import os
import sys
import subprocess
import argparse


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
    parser.add_argument('-l', '--limit', help='Number de résultats à afficher')
    parser.add_argument('-f', '--output', help='nom du fichier créé')
    parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
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

import subprocess
import sys

def run_theharvester(domain,outfile, sources):
    try:
        sources_args = '-b ' + sources
        subprocess.run(["theharvester", "-d", domain, sources_args,"-l", "500", "-f", outfile], check=True)
        print("[+] Information successfully collected.")
    except subprocess.CalledProcessError as e:
        print(f"[-] An error occured: {e}")
        return 1
    except FileNotFoundError as e:
        print(f"[-] TheHarvester not found: {e}")
        return 1
    except Exception as e:
        print(f"[-] An unexpected error occured: {e}")
        return 1
    return 0

def main():
    domain = sys.argv[1]
    outfile = sys.argv[2]
    sources = sys.argv[3]
    return run_theharvester(domain,outfile, sources)

'''if __name__ == "__main__":
    sys.exit(main())'''

