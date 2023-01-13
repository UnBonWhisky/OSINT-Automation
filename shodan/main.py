import shodan #chargement de la ibrairie shodan

#Pour que le script puisse utiliser l'API Shodan
SHODAN_API_KEY = "jegaSstSh2fo9zNqKNHn7puZKoSoakQT"

api = shodan.Shodan(SHODAN_API_KEY)


a = input ('Entrez l adresse IP ou le nom de domaine de votre choix :')

# Lookup the host
host = api.host(a)

# Print general info
print("""
        IP: {}
        Organization: {}
        Operating System: {}

        Location Information :
        Pays : {}
        Region : {}
        City : {}
        Code Postale : {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'),
                  host.get('country_name', 'n/a'), host.get('region_code', 'n/a'), host.get('city', 'n/a'), host.get('postal_code', 'n/a') ))
