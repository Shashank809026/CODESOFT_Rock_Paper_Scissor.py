import random
import time
import os

CHOICES = ['rock', 'paper', 'scissor']
EMOJIS = {
    'rock': '🪨',
    'paper': '📄',
    'scissor': '✂️'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice():
    while True:
        print("\nChoose one:")
        for idx, option in enumerate(CHOICES, 1):
            print(f"{idx}. {option.title()} {EMOJIS[option]}")
        choice = input("\nEnter choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return CHOICES[int(choice) - 1]
        print("❌ Invalid input. Try again.\n")

def get_computer_choice():
    return random.choice(CHOICES)

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    win_map = {
        'rock': 'scissor',
        'paper': 'rock',
        'scissor': 'paper'
    }
    return "You Win!" if win_map[user] == computer else "Computer Wins"

def show_result(user, computer, result):
    print(f"\nYou chose     : {user.title()} {EMOJIS[user]}")
    print(f"Computer chose: {computer.title()} {EMOJIS[computer]}")
    print(f"\n🔔 Result: {result}")

def play_game():
    clear_screen()
    print("🎮 Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        print("\nComputer is choosing", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)
        clear_screen()
        show_result(user_choice, computer_choice, result)
        
        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        clear_screen()

if __name__ == "__main__":
    play_game()
