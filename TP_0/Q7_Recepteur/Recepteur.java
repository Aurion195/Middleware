import javax.jms.* ;
import javax.naming.*;
import javax.ejb.*;

@MessageDriven(mappedName="jms/MonPremierEssaiDestination", activationConfig = {  
    @ActivationConfigProperty(propertyName = "acknowledgeMode", propertyValue = "Auto-acknowledge"),  
    @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue")  
}) 
public class Recepteur implements MessageListener {

	public void onMessage(Message msg) {
		TextMessage tmsg = null ;
		try {
			if(msg instanceof TextMessage) {
				tmsg = (TextMessage) msg;
				System.out.println("Message reçu : " + tmsg.getText());
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