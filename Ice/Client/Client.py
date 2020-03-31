import sys, os, Ice

currentDir = os.path.join(os.path.dirname(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.insert(0, parrentDir)

import server

def init():
    global communicator
    global serveur 
    communicator = Ice.initialize(sys.argv)
    base = communicator.stringToProxy("Serveur:tcp -h 192.168.1.98 -p 10000")
    try:
        serveur = server.IAnnuairePrx.checkedCast(base)
    except:
        print("Vrou vr.... le serveur est eteint")
        communicator.destroy()
        exit()
    
    if not serveur:
        raise RuntimeError("Proxy invalide")

def ajoutAnnuaire():
    print("Entrer un nom")
    nom = raw_input("--->" )
    print("Entrer un numero de tel")
    tel = raw_input("---> ")
    if(serveur.ajoutAnnuaire(nom,tel)):
        print("Le contact a ete ajoute")
    else:
        print("Le contact n'a pas pu etre ajoute")

def suppressionEnregistrement():
    liste = serveur.getListe()
    if(len(liste) > 0):
        print("Selectionner un id")
        print(str(liste))
        id = input("--> ")
        print(serveur.suppressionEnregistrement(id))

def rechercherPersonne():
    print("Rechercher une personne")
    print("Entrer le nom")
    nom = raw_input("--> ")
    a = serveur.rechercherPersonne(nom)
    if(a.id == ""):
        print("Personne n'a ete trouve")
    else:
        print(str(a))

def display():
    serveur.display()
    
def menu(): 
    stop = False
    while not stop:
        print("Bienvenue, selectionner votre action")
        print("1 - ajouter un contact")
        print("2 - supprimer un contact")
        print("3 - rechercher un contact")
        print("4 - afficher annuaire")
        print("5 - exit")
        choix = str(input("--> "))
        
        if choix == "1":
            ajoutAnnuaire()
        elif choix == "2":
            suppressionEnregistrement()
        elif choix == "3":
            rechercherPersonne()
        elif choix == "4":
            display()
        elif choix == "5":
            sys.exit(0)


init()
menu()