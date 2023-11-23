import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

import time

def main():
    state = "on"

    while True:
        print(Fore.CYAN + Style.BRIGHT + f"The current state is {state}")
        print(Fore.BLACK + Style.BRIGHT + "Enter 'off' to turn it off, 'solve' to solve a problem, or 'exit' to quit:")
        user_input = input(Fore.CYAN + Style.BRIGHT + "> " + Fore.YELLOW + Style.BRIGHT)

        if user_input == "off":
            state = "off"
        elif user_input == "solve":
            solve_problem()  # Call the solve_problem function
        elif user_input == "exit":
            print(Fore.CYAN + Style.BRIGHT + "Exiting the program.")
            break
        else:
            print(Fore.CYAN + Style.BRIGHT + "Invalid input. Please enter 'off', 'solve', or 'exit'.")

def solve_problem():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "C4 is now online.")
        time.sleep(0.5)
        input(Fore.MAGENTA + Style.BRIGHT + "Please state your problem: " + Fore.YELLOW + Style.BRIGHT)
        
        # The amount of money you have
        time.sleep(0.5)
        money = float(input(Fore.MAGENTA + Style.BRIGHT + "Enter the amount of money you have: " + Fore.YELLOW + Style.BRIGHT + "₱"))

        # Price of an apple
        time.sleep(0.5)
        price_per_apple = float(input(Fore.MAGENTA + Style.BRIGHT + "Enter the price of an apple: " + Fore.YELLOW + Style.BRIGHT + "₱"))

        # Maximum number of apples you can buy
        max_apples = money // price_per_apple

        # Calculating the remaining money after buying apples
        remaining_money = money - (max_apples * price_per_apple)

        # Display the maximum number of apples and remaining money
        time.sleep(1)
        print(Fore.GREEN + Style.BRIGHT + f"With ₱{money:.2f}, you can buy {int(max_apples)} apples.")
        print(Fore.GREEN + Style.BRIGHT + f"You'll have ₱{remaining_money:.2f} remaining.")

        choice = input(Fore.MAGENTA + Style.BRIGHT + "Do you want to solve another problem? (yes/no): " + Fore.YELLOW + Style.BRIGHT)
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()
