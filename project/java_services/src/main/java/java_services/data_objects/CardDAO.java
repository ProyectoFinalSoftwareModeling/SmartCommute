/**
 * This is a data object class that represents the card data access object.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

package java_services.data_objects;

/**
 * This class represents the card data access object.
 * 
 * author: David Felipe Garcia Leon <dfgarcial@udistrital.edu.co>
 */

public class CardDAO {

    public int id=0;
    public String card_number="";
    public int amount=0;

    public CardDAO(int id, String card_number, int amount) {
        this.id = id;
        this.card_number = card_number;
        this.amount = amount;
    }
    
}
