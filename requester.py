import requests
import time
import hmac, hashlib
import writer


# https://dev.freebox.fr/sdk/os/
class Requester:
    user = ''
    password = ''
    api_url = ''
    TOKEN = ''
    file = writer.Writer('log.authent')

    def initLink(self):
        try:
            response = requests.get('http://mafreebox.freebox.fr/api_version', timeout=5)
            if response.status_code == 200:
                print("API version : " + response.json()['api_version'])
                self.api_url = 'http://mafreebox.freebox.fr/api/v4/'

                session_token = {  # GET SESSION TOKEN
                    'app_id': 'freebox-api',
                    'password': self.file.reading()
                }

                response = requests.post(self.api_url + "login/session/", json=session_token)  # Open session

                if response.json()['success']:
                    self.TOKEN = self.file.reading()
                    return 200
                else:
                    data = {  # GET APP TOKEN
                        'app_id': 'freebox-api',
                        'app_name': 'py_freebox_api',
                        'app_version': '0.0.1',
                        'device_name': 'hugoravard.fr'
                    }
                    response = requests.post(self.api_url + "login/authorize/", json=data)
                    app_token = response.json()['result']['app_token']
                    track_id = response.json()['result']['track_id']

                    while (requests.get(self.api_url + "login/authorize/" + str(track_id)).json()['result']['status'] !=
                           'granted'):
                        time.sleep(1)

                    challenge = str(requests.get(self.api_url + "login/").json()['result']['challenge'])
                    salt = requests.get(self.api_url + "login/").json()['result']['password_salt']

                    session_token = {  # GET SESSION TOKEN
                        'app_id': 'freebox-api',
                        'password': hmac.new(bytes(app_token, 'latin-1'), bytes(challenge, 'latin-1'),
                                             hashlib.sha1).hexdigest()
                    }

                    response = requests.post(self.api_url + "login/session/", json=session_token)  # Open session

                    if response.json()['success']:
                        self.TOKEN = response.json()['result']['session_token']
                        self.file.writing(response.json()['result']['session_token'])
                        print("Les permissions pour l'application sont : " + str(
                            response.json()['result']['permissions']))
                        return 200
                    else:
                        print("Erreur lors de la récupération du token : " + str(response.json()['error_code']))
                        return -1

            else:
                print("Connexion à la Freebox impossible\nCode d'erreur :" + str(response.status_code))
                return -1

        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requete : " + str(e))
            return -1


    def getLanBrowser(self):
        try:
            response = requests.get(self.api_url + "lan/browser/interfaces/", headers=self.TOKEN)
            if response.status_code == 200:
                print("getLanBrowser is : " + str(response.json()))
                return 200
            else:
                print("Erreur dans la réponse :", str(response.status_code))
                return -1
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête : " + str(e))
            return -1
