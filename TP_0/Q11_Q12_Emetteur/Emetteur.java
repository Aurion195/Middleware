import javax.jms.* ;
import javax.naming.*;

public class Emetteur {
	public static void main(String[] args) {
		try {
			InitialContext messaging = new InitialContext();
			TopicConnectionFactory connectionFactory = (TopicConnectionFactory) messaging.lookup("jms/MonPremierTopic");
			Topic topic = (Topic) messaging.lookup("jms/MonPremierTopicDestination");
			TopicConnection connection = connectionFactory.createTopicConnection();
			TopicSession session = connection.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);
			connection.start();

			TopicPublisher publisher = session.createPublisher(topic);
			TextMessage msg = session.createTextMessage();

			for(int i = 0 ; i < 5 ; i++) {
				msg.setText("Je suis le message -> " + i) ;
				publisher.publish(msg);
				Thread.sleep(1000);
			}
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}
	}
}