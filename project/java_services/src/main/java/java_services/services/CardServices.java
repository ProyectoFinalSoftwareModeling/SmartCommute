/**
 * This class is used to provide services for the card entity.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

package java_services.services;

import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java_services.data_objects.CardDAO;
import java_services.repositories.*;

/**
 * This class is used to provide services for the card entity.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@uditrtital.edu.co
 */
@Service
public class CardServices {
    
    @Autowired
    private CardRepositories cardRepositories;
    
    /**
     * This method is used to get ammount of money in the card by card number.
     * 
     * @param cardNumber
     */
    public Optional<Integer> getAmmountByCardNumber(String cardNumber) {
        if (cardNumber == null) {
            return Optional.empty();
        }
        return cardRepositories.getAmount(cardNumber);
    }

    /**
     * This method is used to recharge the ammount of money in the card.
     * 
     * @param cardNumber
     * @param ammount
     */
    public Optional<Integer> rechargeAmmount(String cardNumber, int ammount) {
        if (cardNumber == null || ammount <= 0) {
            return Optional.empty();
        }
        return cardRepositories.updateAmount(cardNumber, ammount);
    }
}
