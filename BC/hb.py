import time
import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_confetti():
    """Prints random confetti animation."""
    confetti_colors = ['🎉', '✨', '🎊', '🥳', '💫', '🌟', '🎈', '🍾']
    for _ in range(20):
        print(''.join(random.choices(confetti_colors, k=30)))
        time.sleep(0.1)
        clear_console()

def birthday_cake(name):
   
    return f"""
       🎂   🎂   🎂   🎂
      ~ HAPPY BIRTHDAY ~
     🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈
            {name}
    """

def countdown():
    """Countdown before the surprise."""
    for i in range(5, 0, -1):
        print(f"🎁 Get ready in... {i}! 🎉")
        time.sleep(1)
        clear_console()

def birthday_message(name):
    """Displays the cool birthday message."""
    clear_console()
    clear_console()
    print_confetti()
    countdown()
    clear_console()
    print(birthday_cake(name))
    print(f"\n🎂✨ Happy Birthday, {name}! ✨🎂")
    print("💫 Wishing you a day filled with magic, joy, and laughter! 🎊🎈\n")


if __name__ == "__main__":
    birthday_person = "tanuska"
    birthday_message(birthday_person)
