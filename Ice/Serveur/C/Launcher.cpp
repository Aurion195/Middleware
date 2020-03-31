#include <iostream>
#include <Launcher.h>

using namespace std;
using namespace server;

int Launcher::cpt = 0 ;

bool Launcher::contactPresent(string nom, string numTel) {
    if(liste_.size() == 0) return false ;

    for(int i = 0 ; i < liste_.size() ; i++) {
        if(liste_[i].nom.compare(nom) == 0) {
            if(liste_[i].numTel.compare(numTel) == 0) {
                return true ;
            }
        }
    }

    return false ;
}

Launcher::Launcher(int size) {
    this->liste_.resize(size) ;
}

Launcher::~Launcher() {

}

bool Launcher::ajoutAnnuaire(string nom, string numTel, const ::Ice::Current&) {
    Annuaire a ;

    if(!contactPresent(nom, numTel)) {
        a.id = cpt++;
        a.nom = nom ;
        a.numTel = numTel;
        liste_.push_back(a);
        return true ;
    }

    return false ;
}

string Launcher::suppressionEnregistrement(string id, const ::Ice::Current&) {
    if(liste_.size() == 0) {
        return "La liste est vide" ;
    }

    for(int i = 0 ; i < liste_.size() ; i++) {
        if(liste_[i].id.compare(id)) {
            liste_.erase(liste_.begin() + i) ;
            return "Le contact à été effacé";
        }
    }

    return "Le contact n'a pas été trouvé" ;
}

server::Annuaire Launcher::rechercherPersonne(string nom, const ::Ice::Current&) {
    Annuaire a ;
    for(int i = 0 ; i < liste_.size() ; i++) {
        if(liste_[i].nom.compare(nom) == 0) {
            return liste_[i] ;
        }
    }

    return a ;
}

server::liste Launcher::getListe(const ::Ice::Current&) {
    return this->liste_ ;
}

void Launcher::display(const ::Ice::Current&){
    cout << "Voici la liste des contacts disponibles" << endl ;
    for(int i = 0 ; i < liste_.size() ; i++) {
        Annuaire m = liste_[i] ;
        cout << "Contact : " << m.id << "  " << m.nom << "  " << m.numTel << endl ;
    }
}