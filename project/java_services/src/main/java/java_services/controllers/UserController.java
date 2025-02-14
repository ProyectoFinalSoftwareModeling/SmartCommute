/**
 * This file has the definition of the user endpoints in the application.
 * 
 * author: David Felipe Garcia Leon <davidfgarcial@udistrital.edu.co>
 */

package java_services.controllers;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java_services.data_objects.AuthDTO;
import java_services.data_objects.UserDAO;
import java_services.services.UserServices;

/**
 * This class has the definition of the user endpoints in the application.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

@RestController
@RequestMapping("v1/user")
public class UserController {

    @Autowired
    private UserServices userServices;

    /**
     * This method is used to get users by id.
     * @param id
     * @return
     */

    @GetMapping("/get_by_id/{idUser}")   
    public Optional<UserDAO> getById (@PathVariable ("idUser") Integer id){
        return userServices.getById(id);
    }

    /**
     * This method is used to login users.
     * @param username
     * @return
     */
    @PostMapping("/login")
    public Optional<UserDAO> login(@RequestBody AuthDTO authData){
        return userServices.login(authData);
    } 

    
    /**
     * This method is used to create users.
     * @param user
     * @return The user created.
     */

     @PostMapping("/create")
        public UserDAO create(@RequestBody UserDAO user){
            return userServices.create(user);
        }
         
}
