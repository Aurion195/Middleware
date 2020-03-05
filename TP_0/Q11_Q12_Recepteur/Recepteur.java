import javax.jms.* ;
import javax.naming.*;

public class Recepteur {
	public static void main(String[] args) {
		try {
			InitialContext messaging = new InitialContext();
			TopicConnectionFactory connectionFactory = (TopicConnectionFactory) messaging.lookup("jms/MonPremierTopic");
			Topic topic = (Topic) messaging.lookup("jms/MonPremierTopicDestination");
			TopicConnection connection = connectionFactory.createTopicConnection();
			TopicSession session = connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
			connection.start();

			TopicSubscriber subscriber =session.createSubscriber(topic);
			subscriber.setMessageListener(new ConsumerMessageListener()) ;
			//System.out.println(subscriber.receive()) ;

			Thread.sleep(50000);
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}
	}


	public static class ConsumerMessageListener implements MessageListener {
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
}