/**
 * This file has the definition of the user repositories in the application.
 * 
 * author: David Felipe Garcia Leon <davidfgarcial@udistrital.edu.co>
 */

package java_services.services;

import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java_services.data_objects.*;
import java_services.repositories.UserRepositories;

/**
 * This class has the definition of the user services in the application.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

@Service
public class UserServices {

    @Autowired
    public UserRepositories userRepositories;

    /**
     * This method is used to get users by id.
     * @param id
     * @return The user found
     */
    public Optional<UserDAO> getById(Integer id) {
     if(id<0)
         return Optional.empty();
    return userRepositories.getById(id);
    }

    /**
     * This method is used to login users.
     * @param username
     * @return The user loged in
     */
    public Optional<UserDAO> login(AuthDTO authData) {
        if (authData.getPassword() == null || authData.getUsername() == null)
                return Optional.empty();
        return userRepositories.login(authData);
    }

    public UserDAO create(UserDAO user) {
        if (user.username == null || user.password == null || user.card_number == null)
                return null;
        return userRepositories.addUser(user);
    }

}
