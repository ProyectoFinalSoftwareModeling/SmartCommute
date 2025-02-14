/**
 * This file has the definition of the user repositories in the application.
 * 
 * author: David Felipe Garcia Leon <davidfgarcial@udistrital.edu.co>
 */

package java_services.repositories;

import java.io.InputStream;
import java.io.FileNotFoundException;
import java.nio.charset.StandardCharsets;
import java.util.Optional;
import java.util.List;
import java.util.ArrayList;

import javax.annotation.PostConstruct;

import org.springframework.stereotype.Repository;

import org.json.JSONArray;
import org.json.JSONObject;

import java_services.data_objects.*;

@Repository
public class UserRepositories {

    private List<UserDAO> users = new ArrayList<UserDAO>();
    private final String filePath = "data/users.json";

    @PostConstruct
    public void init(){
        this.loadData();
    }

    private void loadData(){
        String path = "data/users.json";
        try(InputStream is = getClass().getClassLoader().getResourceAsStream(path)){
            if (is == null) {
                throw new FileNotFoundException("File not found: " + path);

            }
            String content = new String(is.readAllBytes(), StandardCharsets.UTF_8);
            JSONArray jsonArray = new JSONArray(content);
            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject jsonObject = jsonArray.getJSONObject(i);
                UserDAO user = new UserDAO(jsonObject.getInt("id"), jsonObject.getString("username"), jsonObject.getString("password"), jsonObject.getString("card_number"));
                users.add(user);
            }
        }   
        catch (Exception e) {
            e.printStackTrace();
        }
    }
    /**
     * This method gets an user based on the id.
     * @param id
     * @return The user found.
     */
    public Optional<UserDAO> getById(Integer id) {
        for (UserDAO user : users) {
            if (user.id == id) {
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }

    /**
     * This method is used to login users.
     * @param authData
     * @return The user loged in.
     */
    public Optional<UserDAO> login(AuthDTO authData) {
        for (UserDAO user : users) {
            if (user.username.equals(authData.getUsername()) && user.password.equals(authData.getPassword())) {
                return Optional.of(user);
            }
        }
        return Optional.empty();
    }

     /**
     * This method is used to add a new user in the application.
     *
     * @param userData
     * @return An object with user data.
     */
    public UserDAO addUser(UserDAO userDAO) {
        int last_id = -1;
        for (UserDAO user : this.users) {
            if (user.id > last_id) {
                last_id = user.id;
            }
        }

        userDAO.id = last_id + 1;
        this.users.add(userDAO);
        JSONOperations.saveData(this.filePath, this.users);

        return userDAO;
    }
}
