from requester import *

Re = Requester()
if Re.initSession() == -1:
    print("Fin du programme")
    exit(1)
else:
    Re.getLanBrowser()
    exit(0)
