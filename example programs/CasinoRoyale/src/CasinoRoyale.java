/*EDITED BY GABRIEL SMITH
* DATE: 9/20/19
* DESCRIPTION: This is an app which allows players to play a number guessing game and wager certain amounts of money that they bring to the table.
* This is the main class of that app and it will be initialized and added to an arraylist for each time the game is played.
* Since each game is totally seperate and stored in seperate object variables, they could all be displayed at the end of the session.
* However, this functionality was not implemented as it was not part of the assignment. This class uses the default constructor and has 3 instance
* variables and 9 methods, including the main method.
*/
import java.util.Random; //needed to generate random numbers
import java.util.ArrayList; //needed to use arraylists
import java.util.LinkedList; //needed to use linkedlists

public class CasinoRoyale implements Printer{//must implement the printer interface to inherit the printplayers method
    //INSTANCE VARIABLES FOR EACH GAME THAT IS PLAYED
    protected int playerCount;//this instance variable holds the number of players
    protected ArrayList<Player> players = new ArrayList<>(5);//this arraylist holds the player objects and all their variables
    protected LinkedList<Integer> winningNums = new LinkedList<>();//this linkedlist holds the winning numbers
    
    //MAIN METHOD
    public static void main(String[] args) {//this is the main method, since it is static, it doesn't reallt matter that we are instantiating the class multiple times
        String cont;//this string is the sentinel for the main loop to see if another game will be played
        int j = 0;//this is the counter variable to make sure we are only using player objects from the current session
        ArrayList<CasinoRoyale> games = new ArrayList<>(5);//this is the arraylist for games, it is a default size of 5, but could grow indefinitely
        do {//loop while loop for the game since it must run once 
            int playerIterator;//this is the counter to count through the players inside inner loops
            games.add(new CasinoRoyale());//add a new object which is an instance of this class to the game arraylist
            games.get(j).welcome();//call the welcome method of the new games object which will accept and validate input
            for(int i = 0; i < games.get(j).playerCount; i++){//for loop to add player objects to the players arraylist
                games.get(j).createPlayer(i);//call of the createplayer function which accepts input and validates it and adds new players to the instance arraylist
            }
            System.out.println();//print a blank line to match formatting
            playerIterator = 0;//reset player interator
            for(Player p : games.get(j).players){//advanced loop to iterate through players arraylist 
                games.get(j).createGuesses(p, playerIterator);//call function to create player guesses
                System.out.println();//print a blank line to match formatting
                playerIterator++;//increase player interator
            }
            playerIterator = 0;//reset player iterator
            for(Player p : games.get(j).players){//advanced loop to iterate through players arraylist
                games.get(j).createWager(p, playerIterator);//call function to create player wagers
                System.out.println();//print a blank line to match formatting
                playerIterator++;//increase player iterator
            }
            games.get(j).createWinningNums();//run the random number gen to fill the linkedlist
            System.out.println();//print a blank line to match formatting
            playerIterator = 0;//reset player iterator
            for(Player p : games.get(j).players){//advanced loop to iterate through players arraylist
                games.get(j).checkGuesses(p, playerIterator);
                System.out.println();//print a blank line to match formatting
                playerIterator++;//increase player iterator
            }
            cont = games.get(j).playAgain();//call the playagain function which checks if the player wants to play again and prints a summary of the outcome of the game
            //TESTING         These few lines just made sure values were getting assigned correctly
//            System.out.print(games.get(j).winningNums.toString()); //This is a useful check to see if the winning numbers are being stored correctly
//            for(Player p : games.get(j).players){
//                System.out.println(p.getName() + " " + p.getMoney() + " " + p.getWager() + " " + p.getGuesses(0) + p.getGuesses(1) + p.getGuesses(2));
//            }
            j++;//increase the game counter
        } while(cont.equals("yes"));//loop only if yes was entered
    }
    
    //ADDITIONAL METHODS
    public void createWinningNums(){
        Random numMaker = new Random();//instantiate a new random math object 
        System.out.println("Very good. Spinning the wheel.....");//output to let player know numbers are being picked
        for (int i = 0; i < 3; i++){//simple for loop
            winningNums.add(numMaker.nextInt(21));//add the numbers to the instance linkedlist
        }
    }    
    
    public void welcome(){
        System.out.println("Welcome to Casino Royal");//message to user
        System.out.println("++++++++++++++++++++++++");//formatting
        playerCount = Console.getInt("How many players are in the game? ", 0);//get a number of players greater than 0
    }    
    
    public void checkGuesses(Player p, int index){//this method accepts the player object of the advanced loop and an index number so it can reference the actual player object too
       boolean win = false;//default value is false
       System.out.println("The winning numbers are: " + winningNums.get(0) + ", " + winningNums.get(1) + ", " + winningNums.get(2));//print winning nums
       System.out.println();//formatting
       for (int winNum : winningNums) {//loop through each winningnum
           for (int guessNum : p.getGuesses()) {//loop through each user guess
               if (guessNum == winNum) {// check for equality
                   win = true;//set win as true if a match is found
                   break;//break because only one hit is necessary
               }
           }
       }
       if (win == true) {//if a hit was found
           players.get(index).setMoney(players.get(index).getMoney() + players.get(index).getWager());//old system which added wager amount to total
           //players.get(index).setMoney(players.get(index).getMoney() + 300);//new method from clarification, I misunderstood the clarification and reimplemented the old system
           System.out.println("Congratulations " + p.getName() + ", you have a winning number. You now have $" + players.get(index).getMoney() + " on the table.");//let the player know they won
           //System.out.println("Congratulations " + p.getName() + ", you have a winning number. You now have $" + players.get(index).getMoney() + " on the table.");//let the player know they won
       } else {
           players.get(index).setMoney(players.get(index).getMoney() - players.get(index).getWager());//subtract wager from money of the player
           System.out.println("Sorry " + p.getName() + ", you lose. You have $" + players.get(index).getMoney() + " left on the table.");//let the player know they lost           
       }
    }
    
    public void createWager(Player p, int index){//accept both the p object from the advanced loop and the index of the actual player number
        System.out.println(p.getName() + ", you can now place a single bet of any size on these numbers ");//prompt
        System.out.println("as long as you have that much money on the table.");//prompt
        players.get(index).setWager(Console.getDouble(p.getName() + ", how much do you wager? ", 0, p.getMoney(), p.getName()));//this modified console method will accept and validate wagers
    }
    
    public void createGuesses(Player p, int index){//accept both the p object from the advanced loop and the index of the actual player number
        System.out.println(p.getName() + ", you must play three numbers at a time.");//prompt
        System.out.println("The valid numbers are between 0 and 20 inclusive.");//prompt
        for(int k = 0; k < 3; k++){//loop for 3 guesses
            players.get(index).setGuesses(Console.getInt(p.getName() + ", enter your number? ", -1, 21), k);//iterate through guess entries and validate data
        }
    }
    
    public void createPlayer(int index){//create players at specified indexes
        players.add(new Player(Console.getString("Enter a player’s name: ")));//pass name entry into constructor and add the player object to the array
        players.get(index).setMoney(Console.getDouble("How much money is " + players.get(index).getName() + " willing to put on the table? ", 0));//set the money instance variable        
    }
    
    public String playAgain(){//accept a string to see if the player wants to play again
        String cont = Console.getCont("Play Again? (yes/no) ");//only accept yes or no
        System.out.println();//formatting
        printPlayers(players);//call the printplayers method for summary
        return cont;//return the sentinel value
    }
    
    @Override
    public void printPlayers(ArrayList<Player> players){//this method accepts the players arraylist
        System.out.println("These are the players and their ending balances: ");//message
        for(Player p : players){//advanced loop for players
            System.out.println(p.getName() + "'s balance is $" + p.getMoney());//print names and balances
        }
        System.out.println("Take your money off the table when you leave. Come back soon.");//goodbye message
        System.out.println();//formatting
    }
}
