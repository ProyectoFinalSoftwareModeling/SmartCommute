/**
 * This file has a data object class that represents the authentication data transfer object.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */


package java_services.data_objects;

/**
 * This class represents the authentication data transfer object.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

public class AuthDTO {

    private String username = "";
    private String password = "";

    
    public AuthDTO(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String getUsername() {
        return this.username;
    }

    public String getPassword() {
        return this.password;
    }
}
