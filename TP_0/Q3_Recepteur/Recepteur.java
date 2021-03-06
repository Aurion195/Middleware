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

			QueueReceiver receiver = session.createReceiver(queue, null);

			while(true) {
				System.out.println("Je suis le recepeteur -> " + cpt) ;
				cpt++;
				TextMessage msg = (TextMessage) receiver.receive();
				System.out.println(msg.getText()) ;
			}
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}

	}
}