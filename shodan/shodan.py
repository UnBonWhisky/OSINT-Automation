import shodan #chargement de la ibrairie shodan
import requests

#Pour que le script puisse utiliser l'API Shodan
SHODAN_API_KEY = "jegaSstSh2fo9zNqKNHn7puZKoSoakQT"

api = shodan.Shodan(SHODAN_API_KEY)

print ("""Pour utiliser Shodan nous avons besoin d une adresse IP ou d un nom de domaine exacte
                Veuillez taper :
                '1' pour avoir des informations sur une adresse IP
                '2' pour avoir des informations sur un nom de domaine
                '3' pour quitter shodan  """)
choix = int (input  ('Faites votre choix :'))

if choix > 3 :
	choix = int (input  ('Faites votre choix seulement en tapant 1, 2 ou 3:'))

if choix == 1 :
	a = input ('Veuillez entrer une adresse IP de votre choix : ')

elif choix == 2 :
	a = input ('Veuillez entrer un nom de domaine de votre choix : ')
	#Si un nom de domain est entré, Shodan récolte l'adresse IP
	dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + a + '&key=' + SHODAN_API_KEY
	resolved = requests.get(dnsResolve) #Récuperer la sortie de dnsResolve
	hostIP = resolved.json()[a] #Récupération de l'adresse IP
	a = hostIP

elif choix == 3 :
	quit()

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
