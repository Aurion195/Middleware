package tm ;

import javax.ejb.Local;
import javax.jms.Message;

@Local
public interface ITraitementDemande { 
	public void traiterMessage(String msg) ;
}
