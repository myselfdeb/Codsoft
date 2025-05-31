import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    user_choice = ""

    while user_choice not in choices:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    print("\nWelcome to Rock-Paper-Scissors!")

    while True:
        result = play_round()

        if result == "win":
            print("You win this round!")
            user_score += 1
        elif result == "lose":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"\n--- Score ---")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("---" * 5)

        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThanks for playing!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors_game()