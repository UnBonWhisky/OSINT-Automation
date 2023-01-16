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
## Bug connu 
- theHarvester n'est pas compatible avec des versions antérieures à python 3.10
--------------
## Fonctionnalitées non disponibles
- Nous n'avons pas encore intégré l'ajout de clés d'API pour les API utilisées par theHarvester de manière simple (menu comme le reste de l'application). Il est donc nécessaire pour vous de les entrer à la main dans le fichier `/app/theharvester/api-keys.yaml` (docker) ou dans le fichier `theharvester/api-keys.yaml` (téléchargé)
