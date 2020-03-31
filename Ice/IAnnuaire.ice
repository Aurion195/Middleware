module server {
    struct Annuaire {
        int id;
        string nom;
        string numTel ;
    };

    sequence<Annuaire> liste ;

    interface IAnnuaire {
        bool ajoutAnnuaire(string nom, string numTel) ;
        string suppressionEnregistrement(int id) ;
        Annuaire rechercherPersonne(string nom) ;
        liste getListe() ;
        void display();
    };
};