/*EDITED BY GABRIEL SMITH
* DATE: 9/20/19
* DESCRIPTION: This is the player class and the blue print for our player objects, it contains 4 instance variables.
* It also contains getters and setters for those values and 3 constructors. It has an overloaded get method for the array of 
* integers since you can either get the whole array or just one specific value.
*/
public class Player {
    private String name; //instance variable for the name
    private double money;//instance variable for the money a player has
    private int[] guesses = new int[3];//instance array for the guesses a palyer makes
    private double wager;//instance variable for the wager a player places
    
    public Player(){//default constructor
    }
    
    public Player(String name){//constructor which accepts a name as a param
        this.name = name;
    }
    
    public Player(String name, double money){//constructor which accepts name and money as params
        this.name = name;
        this.money = money;
    }
    
    
    public void setName(String name){//setter for name
        this.name = name;
    }
    
    public String getName() {//getter for name
        return name;
    }
    
    public void setMoney(double money){//setter for money
        this.money = money;
    }
    
    public double getMoney() {//getter for money
        return money;
    }    
    
    public void setGuesses(int guess, int index){//setter for guesses, accepts the value and the index number
        guesses[index] = guess;
    }
    
    public int getGuesses(int index) {//getter which returns a single value from the guess array
        return guesses[index];
    }     
    
    public int[] getGuesses() {//getter which returns the whole array
        return guesses;
    }    

    public void setWager(Double wager){//setter for wager
        this.wager = wager;
    }

    public double getWager() {//getter for wager
        return wager;
    }    
}
