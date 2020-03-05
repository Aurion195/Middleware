package tm;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.jms.* ;
import javax.naming.*;

public class Emetteur extends HttpServlet {	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		try {
			InitialContext messaging = new InitialContext();
			QueueConnectionFactory connectionFactory = (QueueConnectionFactory) messaging.lookup("jms/MonPremierEssaiConnectionFactory");
			Queue queue = (Queue) messaging.lookup("jms/MonPremierEssaiDestination");

			String destinataire = request.getParameter("Destinataire") ;
			String msgEcrit = request.getParameter("Message") ;

			QueueConnection connection = connectionFactory.createQueueConnection();
			QueueSession session = connection.createQueueSession(false,Session.AUTO_ACKNOWLEDGE);
			connection.start();
			

			QueueSender sender =session.createSender(queue);
			TextMessage msg = session.createTextMessage();
			
			msg.setText(msgEcrit);
			msg.setStringProperty("Destinataire", destinataire) ;
			sender.send(msg);
			System.out.println("Message envoye");
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}
	}
}
