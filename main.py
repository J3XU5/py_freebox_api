from requester import *

Re = Requester()
if Re.initLink() == -1:
    print("Fin du programme")
else:
    Re.getLanBrowser()
