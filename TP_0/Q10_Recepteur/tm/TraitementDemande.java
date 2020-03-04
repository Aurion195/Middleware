package tm ;

import javax.persistence.*;
import javax.ejb.*;
import javax.annotation.*;

@Stateful
public class TraitementDemande implements ITraitementDemande {

	@PersistenceContext(unitName = "bookstorePU")
	private EntityManager managerGestionEmprunt ;

	private EntityEmprunteur sessionEmprunteur ;

	@Resource
	SessionConext sc ;


}