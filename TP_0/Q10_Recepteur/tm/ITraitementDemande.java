package tm ;

import javax.persistence.*;
import javax.ejb.Remote;

@Remote
public interface ITraitementDemande { 
	public void traitementMesage(Message message) ;
}