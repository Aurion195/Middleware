import javax.jms.* ;
import javax.naming.*;

public class Recepteur {
	public static void main(String[] args) {
		int cpt = 0 ;

		try {
			InitialContext messaging = new InitialContext();
			QueueConnectionFactory connectionFactory = (QueueConnectionFactory) messaging.lookup("jms/MonPremierEssaiConnectionFactory");
			Queue queue = (Queue) messaging.lookup("jms/MonPremierEssaiDestination");
			QueueConnection connection = connectionFactory.createQueueConnection();
			QueueSession session = connection.createQueueSession(false,Session.AUTO_ACKNOWLEDGE);
			connection.start();

			String select = "null" ;
			if(args.length > 0) {
				select = "Destinataire='" + args[0] +"'" ;
				for(int i = 0 ; i < args.length ; i++) {
					select += "OR Destinataire='" + args[i] + "'" ;
				}
			}

			QueueReceiver receiver = session.createReceiver(queue, select);
			TextMessage msg = (TextMessage) receiver.receive();
			System.out.println(msg.getText()) ;
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}

	}
}