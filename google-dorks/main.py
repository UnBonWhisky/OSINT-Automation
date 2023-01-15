def google():
	argscan = []
	while (1 not in argscan and 2 not in argscan) or (1 in argscan and 2 in argscan):
		argscan = input("""
Quels arguments souhaitez-vous entrer dans votre commande ?
Entrez votre réponse comme ceci si vous souhaitez entrer plusieurs arguments : 1,3,8

Voici les réponses possibles :
1. Spécifier un fichier valide contenant Google dorks
2. Spécifier un nom de domaine pour définir la recherche Google dork (Pas obligatoire)
3. Le délai minimum entre les recherches de dork, en secondes. Doit être supérieur à 0 (par défaut 37)
4. Le délai maximum entre les recherches dorks, en secondes. Doit être supérieur à 0 (par défaut 60)
5. Désactiver la validation SSL/TLS. Parfois nécessaire si vous utilisez un proxy HTTPS avec des certificats auto-signés
6. Le nombre maximum de résultat de recherche url à retourner par dork, doit être supérieur à 0 (par défaut 100)
7. Une chaîne de proxy séparées par des virgules. Exemple :  https://myproxy:8080,socks5h://127.0.0.1:9050,socks5h://127.0.0.1:9051
8. Sauvegarde des données url chercher par dork dans un fichier JSON
9. Sauvgarde des données url chercher par dork dans un fichier texte
10.Activer le mode verbeux
Votre choix : """)
    
		argscan = argscan.split(',')
		argscan = STRtoINT(argscan)
    
	PassingArguments = ""
    for x in range(len(argscan)):
        
        if argscan[x] == 1 : # Pour spécifier si le fichier contient des google dorks
            reponse = input("Donner un fichier valide google dorks : ")
			PassingArguments += f"-g {reponse} "

        elif argscan[x] == 2 : # Pour spécifier un nom de domain afin de définir la recherche google dork
	        reponse = input("Quel est le nom de domaine que vous souhaitez spécifier : ")
            PassingArguments += f"-d {reponse} "
        
        elif argscan[x] == 3 : # Pour définir un délai minimum entre les recherches
			reponse = input("Quel est le délai minimum que vous voulez avoir (en secondes) : ")
            PassingArguments += f"-i {reponse} "
        
        elif argscan[x] == 4 : # Pour définir un délai maximum entre les recherches
			reponse = input("Quel est le délai maximum que vous voulez avoir (en secondes) : ")
            PassingArguments += f"-x {reponse} "
        
        elif argscan[x] == 5 : # Pour désactiver la validation SSL/TLS
            PassingArguments += "-l "
        
        elif argscan[x] == 6 : # Pour définir un nombre maximum de résultats de recherche url effectuer par dork
			reponse = input("Quel est le nombre de résultats attendus (doit être supérieur à 0) : ")
            PassingArguments += f"-m {reponse} "
        
        elif argscan[x] == 7 : # Pour définir une chaine de plusieurs prxy à la fois
			reponse = input("Quels sont les proxy que vous voulez utiliser (lien url): ")
            PassingArguments += f"-p {reponse} "
        
        elif argscan[x] == 8 : # Pour sauvegarder dans un fichier json
			reponse = input("Quel est le nom de dossier que vous voulez pour sauvegarder les données cherchées : ")
            PassingArguments += f"-o {reponse} "
        
        elif argscan[x] == 9 : # Pour sauvegarder dans un fichier txt
			reponse = input("Quel est le nom de dossier que vous voulez pour sauvegarder les données cherchées : ")
            PassingArguments += f"-s {reponse} "
        
        elif argscan[x] == 10 : # Pour activer le mode verbeux
            PassingArguments += "-v"

    # Ajout du choix pour un affichage dans la console ou dans un fichier
	OutputScan("google-dorks", OutputDomaine, f"google-dorks/pagodo.py {PassingArguments}")

    return