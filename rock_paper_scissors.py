import random 

player_score = 0
computer_score = 0
options = ['rock', 'paper', 'scissors']
print("Welcome to Rock, Paper, Scissors!")

while True:
    user_input = input("Type Rock, Paper, or Scissors. Type 'Q' to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_input = options[random_number] 

    print(f"Computer chose {computer_input}.")

    if user_input == computer_input:
        print("It's a draw!")
    elif (user_input == 'rock' and computer_input == 'scissors') or \
         (user_input == 'paper' and computer_input == 'rock') or \
         (user_input == 'scissors' and computer_input == 'paper'):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
        
print(f"Final Score: You {player_score} - Computer {computer_score}")
print("Thanks for playing!")        