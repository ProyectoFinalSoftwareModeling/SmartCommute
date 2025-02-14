/**
 * This is a data object class that represents the user data access object.
 * 
 * author: David Felipe Garcia Leon <davidfgarcial@udistrital.edu.co>
 */

package java_services.data_objects;

/**
 * This class represents the user data access object.
 * 
 * author: David Felipe Garcia Leon <davidfgarcial@udistrital.edu.co>
 */

public class UserDAO {

    public int id = 0;
    public String username = "";    
    public String password = "";
    public String card_number = "";

    public UserDAO(int id, String username, String password, String card_number) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.card_number = card_number;
    }

    
    
}
