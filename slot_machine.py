# Write code below 💖
import random

def play():
    symbols = ['🍒','🍇', '🍉', '7️⃣']
    results = random.choices(symbols, k=3)
    print(f"{results[0]} | {results[1]} | {results[2]}")
    if all(symbol == '7️⃣' for symbol in results):
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

def main():
    print("Welcome to the Slot Machine Game!")
    
    playing = True
    while playing:
        print("\n--- New Round ---")
        play()
        
        while True:
            continue_playing = input("\nDo you want to play again? (Y/N): ").upper()
            if continue_playing == 'Y':
                break
            elif continue_playing == 'N':
                playing = False
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
    
    print("Thanks for playing! Come back soon!")

main()
