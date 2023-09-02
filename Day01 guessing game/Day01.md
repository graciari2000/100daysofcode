# Number Guessing Game

This is a simple command-line number guessing game written in Java. The game generates a random number between 10 and 100, and the player's task is to guess the correct number. The game provides feedback based on the player's guesses.

## How to Play

1. Clone this repository to your local machine:

   
   git clone 
https://github.com/graciari2000/100daysofcode/blob/main/Day01%20guessing%20game/guessing_game.java   

2. Compile the Java program:

   
   javac guessing_game.java
   

3. Run the game:

   
   java Random
   

4. The game will display a message like this:

   What number are we thinking of?:
   

5. Enter your guess as an integer and press Enter.

6. The game will provide feedback based on your guess, such as whether the guessed number is smaller or larger than the target number, or if you are very close ("Hot") to the target number.

7. Keep guessing until you correctly guess the number. The game will display a congratulatory message when you guess correctly.

## Example Gameplay


Random numbers should be in int from 10 to 100:
What number are we thinking of?:
50
You are way off! A little backtracking please
What number are we thinking of?:
25
This one is smaller. Think again
What number are we thinking of?:
35
This one is smaller. Think again
What number are we thinking of?:
45
This one is smaller. Think again
What number are we thinking of?:
55
This one is smaller. Think again
What number are we thinking of?:
65
This one is smaller. Think again
What number are we thinking of?:
75
This one is smaller. Think again
What number are we thinking of?:
85
This one is smaller. Think again
What number are we thinking of?:
95
This one is smaller. Think again
What number are we thinking of?:
105
You are way off! A little backtracking please
What number are we thinking of?:
90
This one is smaller. Think again
What number are we thinking of?:
80
This one is smaller. Think again
What number are we thinking of?:
70
This one is smaller. Think again
What number are we thinking of?:
60
You are way off! A little backtracking please
What number are we thinking of?:
64
oHoHo! Hot or Cold?
What number are we thinking of?:
63
Congratulations! You guessed the correct number.


Enjoy the game and happy guessing!