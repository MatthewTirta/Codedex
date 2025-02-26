import random

# Player stats
player_hp = 20

# Game introduction
print("Welcome to the Mini RPG Adventure!")
print("You find yourself in a mysterious forest. Choose your path wisely!")

# Main game loop
while True:
    print("\nWhat will you do?")
    print("1. Go deeper into the forest")
    print("2. Climb a tree to look around")
    print("3. Rest by the river")
    print("4. Quit the game")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Battle with an enemy
        print("\nYou venture deeper into the forest...")
        print("An enemy appears! Prepare for battle!")

        enemy_hp = random.randint(10, 20)  # Random enemy HP
        while player_hp > 0 and enemy_hp > 0:
            print(f"\nYour HP: {player_hp}")
            print(f"Enemy HP: {enemy_hp}")
            action = input("What will you do? (1) Attack (2) Heal: ")

            if action == "1":
                damage = random.randint(3, 6)  # Random player damage
                enemy_hp -= damage
                print(f"You dealt {damage} damage to the enemy!")
            elif action == "2":
                heal = random.randint(4, 8)  # Random heal amount
                player_hp += heal
                print(f"You healed yourself for {heal} HP!")
            else:
                print("Invalid choice! Try again.")
                continue

            if enemy_hp > 0:
                enemy_damage = random.randint(2, 5)  # Random enemy damage
                player_hp -= enemy_damage
                print(f"The enemy dealt {enemy_damage} damage to you!")

        if player_hp > 0:
            print("\nYou defeated the enemy! Well done!")
        else:
            print("\nYou were defeated... Game Over!")
            break

    elif choice == "2":
        # Climb a tree
        print("\nYou climb a tree and spot a treasure chest!")
        print("You gain 5 HP!")
        player_hp += 5
        print(f"Your HP is now {player_hp}")

    elif choice == "3":
        # Rest by the river
        print("\nYou rest by the river and feel refreshed.")
        player_hp = min(player_hp + 10, 20)  # Heal up to 20 HP
        print(f"Your HP is now {player_hp}")

    elif choice == "4":
        # Quit the game
        print("\nThanks for playing! Goodbye!")
        break

    else:
        print("\nInvalid choice. Try again!")