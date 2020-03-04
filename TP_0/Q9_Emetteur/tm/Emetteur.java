package tm;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.jms.* ;
import javax.naming.*;

public class Emetteur extends HttpServlet {

	@Resource(mappedName = "jms/MonPremierEssaiConnectionFactory")
	QueueConnectionFactory connectionFactory ;

	@Resource(mappedName = "jms/MonPremierEssaiDestination")
	Queue queue ;

	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		ServletContext scContect = getServletContext();
		PrintWriter out = response.getWriter();
		String destinataire = request.getParameter("Destinataire") ;
		String msgEcrit = request.getParameter("Message") ;

		try {
						QueueConnection connection = connectionFactory.createQueueConnection();
			QueueSession session = connection.createQueueSession(false,Session.AUTO_ACKNOWLEDGE);
			connection.start();
			

			QueueSender sender =session.createSender(queue);
			TextMessage msg = session.createTextMessage();
			
			msg.setText(msgEcrit);
			msg.setStringProperty("Destinataire", destinataire) ;
			sender.send(msg);

			out.println("Le message a été envoyé");
		}
		catch(Exception e) {
			System.out.println(e.getMessage()) ;
		}
	}
}