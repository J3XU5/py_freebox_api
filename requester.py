import requests


class Requester:
    user = ''
    password = ''

    def __init__(self, user: str, password: str):
        try:
            response = requests.get('http://mafreebox.freebox.fr/api_version', timeout=5)
            if response.status_code == 200:
                print(response.json())
                self.user = user
                self.password = password
            else:
                print("Connexion à la Freebox impossible\nCode d'erreur : " + str(response.status_code))

        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requete : " + str(e))
