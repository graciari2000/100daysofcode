import java.util.Scanner;
class Random {
    public static void main(String args[] ) {
	int min = 10;
	int max = 100;
	System.out.println("Note: Random numbers should be in int from " + min + " to " + max + ":");
	int random_number = (int)Math.floor(Math.random() * (max - min  + 1) + min);
	Scanner myObj = new Scanner(System.in);

	while (true) {
	System.out.println("What number are we thinking of?: ");
	String userInputString = myObj.nextLine(); // Read user input as string
        int userInput;
	userInput = Integer.parseInt(userInputString); // Convert string to int

	if(userInput < random_number) {
	    System.out.println("This one is smaller think again");
	}
	else if(userInput > random_number) {
	    System.out.println("You are way off! A little bactracking please");
	}
	else if(Math.abs(userInput - random_number) == 1) {
	    System.out.println("oHoHo! Hot or Cold?");
	}
	else {
	    System.out.println("Congratulations! You guessed the correct number.");
                break;
	}
    }
}
}
