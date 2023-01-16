# TP2 - OSINT Automation
Ceci est un projet scolaire réalisé par :
- Amine LACHGAR ([@Marokingu](https://github.com/Marokingu))
- Alexi LOREAUX ([@alexilrx](https://github.com/alexilrx))
- Flavien FOUQUERAY ([@ffouqueray](https://github.com/ffouqueray))
--------------
## Utilité de cet outil
Cet outil a pour principale utilité de faciliter et accélérer l'utilisation des API / programmes suivants :
- [theHarvester](https://github.com/laramies/theHarvester)
- [DNSCan](https://github.com/rbsec/dnscan)
- [Shodan](https://www.shodan.io)
- [Google-Dorks](https://github.com/opsdisk/pagodo)
- [URLScan](https://urlscan.io)

Nous avons implémenté la plupart des fonctionnalités de celles-ci, ainsi que créé un dockerfile pour conteneuriser l'application.

Nous n'avons pas posté le conteneur sur le hub docker, mais il est toujours possible de le build puis l'installer.

Afin d'obtenir les résultats que pourraient produire les outils intégrés, vous pouvez ajouter un volume (aucune utilité si vous ne voulez que des résultats dans la console. Vous pouvez donc utiliser cette commande si vous souhaitez obtenir des sorties fichiers :
```docker
docker run -v path/to/your/folder:/app/output -it tp2osint:latest
```
--------------
## Comment executer notre outil
### Dans le cas où vous utilisez le code source lui-même
- Installez python 3.10+. Si ce n'est pas déjà fait, [voici un lien pour le télécharger](https://www.python.org/downloads/)
- Décompressez l'archive ZIP téléchargée en cliquant sur le bouton "Code" (avec 7zip, WinRAR ou gzip par exemple)
- Ouvrez un terminal dans le dossier décompressé précédemment
- utilisez pip pour installer les dépendances :  
    Pour Windows : `py -3 -m pip install -r requirements.txt`  
    Pour Linux : `python3 -m pip install -r requirements.txt`
- Lancez le programme python avec la commande suivante :  
  Pour Windows : `py -3 main.py`  
  Pour Linux : `python3 main.py`
---
### Dans le cas où vous utilisez Docker
- Installez [Docker](https://docs.docker.com/engine/install/)
- Décompressez l'archive ZIP téléchargée en cliquant sur le bouton "Code" (avec 7zip, WinRAR ou gzip par exemple)
- Ouvrez un terminal dans le dossier décompressé précédemment
- Tapez la commande suivante afin de build le dockerfile :  
  `docker build --pull --rm -f "Dockerfile" -t tp2osint:latest "."`
- Tapez ensuite la commande suivante pour lancer le container que vous venez de build :  
  `docker run -v path/to/your/folder:/app/output -it tp2osint:latest`  
  N'oubliez pas de changer le `path/to/your/folder` par un dossier de votre ordinateur
--------------
## Bug connu 
- theHarvester n'est pas compatible avec des versions antérieures à python 3.10
--------------
## Fonctionnalitées non disponibles
- Nous n'avons pas encore intégré l'ajout de clés d'API pour les API utilisées par theHarvester de manière simple (menu comme le reste de l'application). Il est donc nécessaire pour vous de les entrer à la main dans le fichier `/app/theharvester/api-keys.yaml` (docker) ou dans le fichier `theharvester/api-keys.yaml` (téléchargé)
