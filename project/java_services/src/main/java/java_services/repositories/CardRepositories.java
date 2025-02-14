/**
 * This file is used to provide the card repositories.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

package java_services.repositories;

import java.util.Optional;

import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.ArrayList;

import java_services.data_objects.CardDAO;


/**
 * This class is used to provide the card repositories.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */
@Repository
public class CardRepositories {

    private List<CardDAO> cards = new ArrayList<CardDAO>();

    /**
     * This method is used to verify if a card exists with the number.
     * 
     * @param card_number
     * @return true if the card exists, false otherwise
     */

    
    /**
     * This method is used to update the amount of a card.
     * 
     * @param card_number
     * @param amount
     * @return the new ammount of the card
     */

    public Optional <Integer> updateAmount(String card_number, int amount){
        for (CardDAO card : cards) {
            if (card.card_number.equals(card_number)) {
                card.amount = amount;
                return Optional.of(amount);
            }
        }
        return Optional.empty();
    }

    /**
     * This method is used to get the amount of a card.
     * 
     * @param card_number
     * @return the amount of the card
     */

    public Optional<Integer> getAmount(String card_number){
        for (CardDAO card : cards) {
            if (card.card_number.equals(card_number)) {
                return Optional.of(card.amount);
            }
        }
        return Optional.empty();
    }
}
