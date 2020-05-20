/*EDITED BY GABRIEL SMITH
* DATE: 9/20/19
* DESCRIPTION: This is the console class, it instantiates a scanner object and then has several methods which accept and validate user input.
* I've modified a few of these methods to match the specifications of our current app. Some only accept certain strings now and some have
* slightly different parameters.
*/
import java.util.Scanner;

public class Console {
    
    private static Scanner sc = new Scanner(System.in);

    public static String getString(String prompt) {
        System.out.print(prompt);
        String s = sc.next();  // read user entry
        sc.nextLine();  // discard any other data entered on the line
        return s;
    }
    
    public static String getCont(String prompt) {
        String s = "";
        boolean isValid = false;
        while (!isValid) {
            System.out.print(prompt);
            if (sc.hasNext("yes") || sc.hasNext("no")) {//only accept yes or no
                s = sc.next();  // read user entry
                isValid = true;
            } else {
                System.out.println("You must enter yes or no. Try again.");
            }
            sc.nextLine();  // discard any other data entered on the line
        }
        return s;
    }

    public static int getInt(String prompt) {
        int i = 0;
        boolean isValid = false;
        while (!isValid) {
            System.out.print(prompt);
            if (sc.hasNextInt()) {
                i = sc.nextInt();
                isValid = true;
            } else {
                System.out.println("Error! Invalid integer. Try again.");
            }
            sc.nextLine();  // discard any other data entered on the line
        }
        return i;
    }

    public static int getInt(String prompt, int min, int max) {
        int i = 0;
        boolean isValid = false;
        while (!isValid) {
            i = getInt(prompt);
            if (i <= min) {
                System.out.println(
                        "Error! Number must be greater than " + min + ".");
            } else if (i >= max) {
                System.out.println(
                        "Error! Number must be less than " + max + ".");
            } else {
                isValid = true;
            }
        }
        return i;
    }
    
    public static int getInt(String prompt, int min) {//overloaded method of get int with a minimum value but no max
        int i = 0;
        boolean isValid = false;
        while (!isValid) {
            i = getInt(prompt);
            if (i <= min) {
                System.out.println(
                        "Error! Number must be greater than " + min + ".");
            } else {
                isValid = true;
            }
        }
        return i;
    }

    public static double getDouble(String prompt) {
        double d = 0;
        boolean isValid = false;
        while (!isValid) {
            System.out.print(prompt);
            if (sc.hasNextDouble()) {
                d = sc.nextDouble();
                isValid = true;
            } else {
                System.out.println("Error! Invalid number. Try again.");
            }
            sc.nextLine();  // discard any other data entered on the line
        }
        return d;
    }

    public static double getDouble(String prompt, double min, double max, String name) {//overloaded method of getdouble to accept a name string to address the player
        double d = 0;
        boolean isValid = false;
        while (!isValid) {
            d = getDouble(prompt);
            if (d <= min) {
                System.out.println(
                        name + ", you cannot wager less than 0 dollars. Try a higher wager.");//custom prompt
            } else if (d > max) {
                System.out.println(
                        name + ", you did not have $" + d + " on the table to bet. Try a lower wager.");//custom prompt
            } else {
                isValid = true;
            }
        }
        return d;
    }
    
    public static double getDouble(String prompt, double min) {//overloaded getdouble method to accept any value greater than 0
        double d = 0;
        boolean isValid = false;
        while (!isValid) {
            d = getDouble(prompt);
            if (d <= min) {
                System.out.println(
                        "Error! Number must be greater than " + min + ".");
            } else {
                isValid = true;
            }
        }
        return d;
    }
}