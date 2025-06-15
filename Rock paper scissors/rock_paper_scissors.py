import random

choices = ("rock", "paper", "scissors")
computer_choices = random.choice(choices)

user_choices = input("Choose rock, paper or scissors:").lower()

while True:
    user_choices = input("Choose rock, paper or scissors:").lower()
    
    if user_choices not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choices = random.choice(choices)
    print(f"You chose: {user_choices}")
    print(f"Computer chose: {computer_choices}")

    if user_choices == computer_choices:
        print("It's a tie!")
    elif (user_choices == "rock" and computer_choices == "scissors") or \
         (user_choices == "paper" and computer_choices == "rock") or \
         (user_choices == "scissors" and computer_choices == "paper"):
        print("You win!")
    else:
        print("You lose!")
    print("Thanks for playing!")
    play_again = input("Want to play again? Y/N: ").strip().lower()
    if play_again != 'y':
        break
