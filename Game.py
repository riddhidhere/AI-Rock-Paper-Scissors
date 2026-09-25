import random

print("=== Welcome to the GKS AI Rock-Paper-Scissors Match ===")
print("Instructions: Type 'rock', 'paper', or 'scissors'. Type 'quit' to exit.")

choices = ["rock", "paper", "scissors"]

# 1. Initialize Score Tracker Variables
user_score = 0
computer_score = 0

while True:
    user_choice = input("\nYour Turn (rock/paper/scissors/quit): ").lower().strip()
    
    if user_choice == "quit":
        print("\n=== MATCH OVER ===")
        print(f"Final Score -> You: {user_score} | 🤖 AI: {computer_score}")
        if user_score > computer_score:
            print("🏆 You won the overall match! Brilliant job.")
        elif user_score < computer_score:
            print("🤖 AI won the overall match. Practice makes perfect!")
        else:
            print("🤝 The overall match ended in a tie!")
        break
        
    if user_choice not in choices:
        print("❌ Invalid input! Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"🤖 AI Computer chose: {computer_choice}")

    # 2. Logic Matrix with Live Score Updates
    if user_choice == computer_choice:
        print("🤝 It's a TIE!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You WIN this round!")
        user_score += 1  # Adds 1 point to your score
    else:
        print("💥 Computer AI Wins this round!")
        computer_score += 1  # Adds 1 point to the AI's score
        
    # 3. Print current score after every round
    print(f"📊 Current Score -> You: {user_score} | 🤖 AI: {computer_score}")
