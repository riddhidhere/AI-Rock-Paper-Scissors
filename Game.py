import random

print("=== Welcome to the GKS AI Rock-Paper-Scissors Game ===")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

# 1. Available choices for the game
choices = ["rock", "paper", "scissors"]

# 2. Start an infinite loop so the game keeps running
while True:
    user_choice = input("\nYour Turn (rock/paper/scissors/quit): ").lower().strip()
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye.")
        break  # This breaks the loop and stops the game
        
    if user_choice not in choices:
        print("❌ Invalid input! Please check your spelling and try again.")
        continue  # Skips the rest of the code and asks for input again

    # 3. Computer AI chooses a random option
    computer_choice = random.choice(choices)
    print(f"🤖 AI Computer chose: {computer_choice}")

    # 4. Game Logic Matrix to find the winner
    if user_choice == computer_choice:
        print("🤝 It's a TIE!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You WIN! Excellent move.")
    else:
        print("💥 Computer AI Wins! Better luck next time.")
