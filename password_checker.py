import string
import math
from colorama import Fore, Style

def calculate_entropy(password):
    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char in string.punctuation for char in password):
        charset_size += len(string.punctuation)
    
    entropy = len(password) * math.log2(charset_size)
    return entropy

def time_to_crack(entropy):
    # Assuming a brute-force rate of 1 billion guesses per second
    guesses_per_second = 1e9
    seconds_to_crack = 2**entropy / guesses_per_second
    minutes = seconds_to_crack / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365
    return years

def check_password_strength(password):
    entropy = calculate_entropy(password)
    crack_time = time_to_crack(entropy)
    
    if len(password) < 8:
        print(Fore.RED + "Weak Password: Too short. Use at least 8 characters." + Style.RESET_ALL)
    elif crack_time < 1:
        print(Fore.RED + f"Weak Password: Could be cracked in less than a year! 🔓" + Style.RESET_ALL)
    elif crack_time < 100:
        print(Fore.YELLOW + f"Moderate Password: Could be cracked in about {int(crack_time)} years. 🔑" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"Strong Password! Estimated crack time: {int(crack_time)} years. 🛡️" + Style.RESET_ALL)

if __name__ == "__main__":
    print("🔐 Password Strength Checker with Time to Crack Estimation 🔐")
    password = input("Enter a password to test: ")
    check_password_strength(password)
