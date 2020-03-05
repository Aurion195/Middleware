package tm ;

import javax.jms.* ;
import javax.naming.*;
import javax.ejb.*;
import javax.annotation.Resource;

@MessageDriven(mappedName="jms/MonPremierEssaiDestination", activationConfig = {  
    @ActivationConfigProperty(propertyName = "messageSelector", propertyValue = "Destinataire='r1'"),  
}) 
public class Recepteur implements MessageListener {
	
@EJB
ITraitementDemande beanTraitementDemande;

	public void onMessage(Message msg) {
		try {
			TextMessage tmsg = null ;

			if(msg instanceof TextMessage) {
				tmsg = (TextMessage) msg;
				beanTraitementDemande.traiterMessage(tmsg.getText());
			}
			else {
				 System.out.println ("Message pas de type texte");
			}
		} 
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}
		
	}
}
