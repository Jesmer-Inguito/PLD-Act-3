import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import time

def calculate_cost(apple_quantity, orange_quantity):
    apple_price = 20
    orange_price = 25

    total_cost = (apple_quantity * apple_price) + (orange_quantity * orange_price)
    return total_cost

def main():
    shop_name = ("Welcome to J's Fruit Shop!")
    print(Fore.CYAN + Style.BRIGHT + shop_name)
    input(Fore.GREEN + Style.BRIGHT + "How can I help you? " + Fore.YELLOW + Style.BRIGHT)
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "Certainly! ")

    time.sleep(1)
    apples = int(input(Fore.MAGENTA + Style.BRIGHT + "How many apples do you want to buy? " + Fore.YELLOW + Style.BRIGHT))
    time.sleep(0.5)
    oranges = int(input(Fore.MAGENTA + Style.BRIGHT + "How many oranges do you want to buy? " + Fore.YELLOW + Style.BRIGHT))

    time.sleep(1)
    total = calculate_cost(apples, oranges)
    print(Fore.MAGENTA + Style.BRIGHT + f"The total amount to pay is: {Fore.GREEN + Style.BRIGHT}{total} pesos")

if __name__ == "__main__":
    main()