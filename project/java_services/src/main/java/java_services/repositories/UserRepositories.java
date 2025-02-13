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
     * This method creates a new user.
     * @param user
     * @return The user created.
     */
    public Optional<UserDAO> create(UserDAO user) {
        int lastId = -1;
        for (UserDAO u : users) {
            if (u.id > lastId) {
                lastId = u.id;
            }
        }
        UserDAO newUser = new UserDAO(
            lastId,
            user.Username(),
            user.Password(),
            user.CardNumber()
        );
        this.users.add(newUser);

        //TODO: Save the new user in the JSON file.
        return Optional.of(newUser);
    }
}
