import javax.jms.* ;
import javax.naming.*;

public class Emetteur {
	public static void main(String[] args) {
		try {
			InitialContext messaging = new InitialContext();
			QueueConnectionFactory connectionFactory = (QueueConnectionFactory) messaging.lookup("jms/MonPremierEssaiConnectionFactory");
			Queue queue = (Queue) messaging.lookup("jms/MonPremierEssaiDestination");
			QueueConnection connection = connectionFactory.createQueueConnection();
			QueueSession session = connection.createQueueSession(false,Session.AUTO_ACKNOWLEDGE);
			connection.start();
			
			QueueSender sender =session.createSender(queue);
			Queue queueTempory = session.createTemporaryQueue();
			TextMessage msg = session.createTextMessage();
			msg.setJMSReplyTo(queueTempory) ;
			
			for(int i = 0 ; i < args.length ; i++) {
				msg.setText("je suis le message -> " + i);
				msg.setStringProperty("Destinataire", args[i]) ;
				sender.send(msg);
			}

			QueueReceiver receiver = session.createReceiver(queueTempory, null);
			TextMessage msgRecu = (TextMessage) receiver.receive();
			System.out.println(msgRecu.getText()) ;
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
			System.exit(0);
		}
	}
}