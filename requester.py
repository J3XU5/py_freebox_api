import requests


class Requester:
    user = ''
    password = ''

    def __init__(self, user: str, password: str):
        try:
            response = requests.get('http://mafreebox.freebox.fr/api_version', timeout=5)
            if response.status_code == 200:
                print("API version : " + response.json()['api_version'])
                self.user = user
                self.password = password
            else:
                print("Connexion à la Freebox impossible\nCode d'erreur : " + str(response.status_code))

        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requete : " + str(e))

    def getLanBrowser(self):
        try:
            response = requests.get("http://mafreebox.freebox.fr/api/v4/lan/browser/interfaces/")
            if response.status_code == 200:
                print("getLanBrowser is : " + response.json())
            else:
                print("Erreur dans la réponse : ", str(response.status_code))
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête : " + str(e))
