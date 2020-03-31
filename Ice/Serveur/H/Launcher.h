#pragma once
#include <iostream>
#include <vector>
#include <Ice/Ice.h>
#include <IAnnuaire.h>

using namespace server ;

class Launcher : public IAnnuaire {
    private : 
        static int cpt ;
        liste liste_ ;
    
    public :
        Launcher(const int size = 0) ;
        ~Launcher();
        bool ajoutAnnuaire(std::string nom, std::string numTel, const ::Ice::Current&) ;
        std::string suppressionEnregistrement(std::string id, const ::Ice::Current&) ;
        ::server:: liste getListe(const ::Ice::Current&) ;
        ::server:: Annuaire rechercherPersonne(std::string nom, const ::Ice::Current&) ;
        bool contactPresent(std::string nom, std::string numTel) ;
        void display(const ::Ice::Current&);
};