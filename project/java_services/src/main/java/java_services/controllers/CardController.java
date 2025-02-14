/**
 * This file has the definition of endpoints for the card in the application.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

package java_services.controllers;

import org.springframework.web.bind.annotation.RestController;

import java_services.services.CardServices;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

import java_services.data_objects.CardDAO;


/**
 * This class has the definition of the card endpoints in the application.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

@RestController
@RequestMapping("v1/card")
public class CardController {

    @Autowired
    private CardServices cardServices;

    /**
     * This method is used to get card ammount by card_number.
     * @param card_number
     * @return ammount
     */
    @GetMapping("/get_ammount_by_card_number/{card_number}")
     public Optional<Integer> getAmmountByCardNumber (@PathVariable ("cardNumber") String card_number){
        return cardServices.getAmmountByCardNumber(card_number);
    }

    /**
     * This method is used to recharge ammount to card.
     * @param card_number
     * @param ammount
     * @return old and new ammount 
     */
    @GetMapping("/recharge_ammount/{card_number}/{ammount}")
    public Optional<Integer> rechargeAmmount (@PathVariable ("cardNumber") String card_number, @PathVariable ("ammount") int ammount){
        return cardServices.rechargeAmmount(card_number, ammount);
    }
}
