package tm ;

import javax.ejb.*;
import javax.jms.* ;

@Stateless
public class TraitementDemande implements ITraitementDemande{
	public void traiterMessage(String msg) {
		System.out.println("Je suis le traiteur de message, voici le message \n" + msg) ;
	}
}
