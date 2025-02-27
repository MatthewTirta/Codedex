import random

def fortune():
    # Define a list of fortune messages.
    fortunes = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!"
    ]
    
    total_fortunes = len(fortunes)
    random_index = random.randint(0, total_fortunes - 1)

    selected_fortune = fortunes[random_index]
    return selected_fortune

print(fortune())
