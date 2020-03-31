module server {
    struct Annuaire {
        string id;
        string nom;
        string numTel ;
    };

    sequence<Annuaire> liste ;

    interface IAnnuaire {
        bool ajoutAnnuaire(string nom, string numTel) ;
        string suppressionEnregistrement(string id) ;
        Annuaire rechercherPersonne(string nom) ;
        liste getListe() ;
        void display();
    };
};