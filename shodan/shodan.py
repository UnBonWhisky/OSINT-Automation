import shodan #chargement de la ibrairie shodan
import requests

#Pour que le script puisse utiliser l'API Shodan
SHODAN_API_KEY = "jegaSstSh2fo9zNqKNHn7puZKoSoakQT"

# -d / --domain: nom de domaine
# -i / --ip : adresse ip
# -o / --output-file : sortie dans un fichier

# if -d : rentrer dans ton pavé
# sinon : aller au host =

api = shodan.Shodan(SHODAN_API_KEY)

#Si un nom de domain est entré, Shodan récolte l'adresse IP
dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + domaine + '&key=' + SHODAN_API_KEY
resolved = requests.get(dnsResolve) #Récuperer la sortie de dnsResolve
ip = resolved.json()[domaine] #Récupération de l'adresse IP


#Analyse de l'adresse IP
host = api.host(a)

# Affichage des différentes informations récoltés par l'API Shodan
print("""
Informations Générale :
Adresse IP : {}
Nom de l'entreprise : {}
Systeme d'opération : {}
Numéro de Système Autonome (ASN) : {}
Fournisseur Internet : {}

Information de géolocalisation :
Pays : {}
Region : {}
Ville : {}
Code Postale : {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('asn', 'n/a'), host.get('isp', 'n/a'),
			host.get('country_name', 'n/a'), host.get('region_code', 'n/a'), host.get('city', 'n/a'), host.get('postal_code', 'n/a')))
