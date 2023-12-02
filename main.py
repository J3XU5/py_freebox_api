from requester import *

Re = Requester()
if Re.initLink() == -1:
    print("Fin du programme")
    exit(1)
else:
    Re.getLanBrowser()
