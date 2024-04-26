# Math-Game
Implements a math game where users solve randomly generated arithmetic problems, earning points for correct answers. It handles errors and provides a final score.

Here's a step-by-step description of the provided math game code:

Import Modules:
The code imports the random module to generate random numbers and the operator module to perform arithmetic operations.

Define errorHandle Function:
This function handles errors when the user enters an invalid answer.
It prompts the user to input a valid answer until a float is entered.

Define random_problem Function:
This function generates a random arithmetic problem.
It randomly selects two numbers between 1 and 10 and an arithmetic operation from addition, subtraction, multiplication, or division.
It calculates the answer to the problem using the selected operation and returns it.

Define ask_question Function:
This function presents the user with a random arithmetic problem and prompts them to input an answer.
It handles errors if the user's input is not a float, using the errorHandle function.
It returns True if the user's guess matches the correct answer, otherwise False.

Define game Function:
This function initiates the math game.
It initializes the score to 0.
It runs a loop where it asks questions using the ask_question function.
If the user answers correctly, it increments the score and prints "Correct!". If the user answers incorrectly, it breaks out of the loop.
After the loop ends, it prints the final score and a message encouraging the user to continue.

Execute game Function:
The game function is called to start the game when the script is run.
This code provides a simple math game where users solve random arithmetic problems and earn points for correct answers. It handles errors in user input and provides feedback on the correctness of answers.

DEMO:

![image](https://github.com/arshasuresh03/Math-Game/assets/160167081/44278c62-a6b1-4323-9e34-ca5b95d57e66)
