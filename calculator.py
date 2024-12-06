import random
import time

def ask_question():
    """Ask a random math question and return the question and correct answer."""
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    
    # Avoid division by zero
    if operation == '/':
        num2 = random.randint(1, 10)  # Ensure the second number is not zero

    question = f"What is {num1} {operation} {num2}?"
    
    # Calculate the correct answer
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':

        
        answer = num1 * num2
    elif operation == '/':
        answer = round(num1 / num2, 2)  # Round to 2 decimal places
    
    return question, answer

def play_game():
    """Start the game and keep asking questions until the player gets one wrong or runs out of time."""
    score = 0
    start_time = time.time()
    game_duration = 30  # Game duration in seconds

    print("Welcome to the Calculator Game!")
    print("You have 30 seconds to answer as many questions as possible.")
    print("Let's begin...\n")

    while True:
        # Check if the game time is over
        if time.time() - start_time > game_duration:
            print(f"\nTime's up! You scored {score} points!")
            break

        # Ask a new question
        question, correct_answer = ask_question()
        print(question)

        try:
            # Get player's answer
            player_answer = float(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the answer is correct
        if player_answer == correct_answer:
            score += 1
            print("Correct! Your score is:", score)
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            print(f"Game Over! Your final score is {score}.")
            break

if __name__ == "__main__":
    play_game()
