"""
 Project 1 
 Sep 30 2026
 
 Goals: A simple CLI password checker and validator. 

 Structure:
    - main.py -> CLI entry point, handles inputs/flags, outputs report 
    - rules.py -> functions to test length, charset, and patterns
    - common_password.txt -> list of banned passwords
    - scoring.py -> logic to calculate score or entropy and returns a rating

 """

import string
import argparse # CLI parsing module
import getpass # prompt for password with echo turned off
from rules import rate_length, rate_div, calc_entropy
from common_passwords import read_seclist

def pw_report(pw_dict: dict, entropy_score: float, length_rating: str):


    print(f"\n--- Password Evaluation ---")
    print(f"Length: {pw_dict["length"]} --> ({length_rating})")
    print(f"Character Pool Size: {pw_dict["pool_size"]}")
    print(f"Entropy: {entropy_score:.2f} bits")



def main():
    # CLI entry point

    pw = getpass.getpass("Enter a password: ")
    if (pw in read_seclist()):
        while (pw in read_seclist()):
            print("Password unsecure (exists in secList 10k most common passwords), Try again...")
            pw = getpass.getpass("Enter a password: ")

    div_stats = rate_div(pw) # rates diversity of characters
    entropy = calc_entropy(len(pw), div_stats["pool_size"]) # calculates password entropy
    length_rating = rate_length(pw) # rates length of password string

    pw_report(div_stats, entropy, length_rating)

    # possible args
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-p", "--password", help="Read user provided passoword string", type=str)
    # parser.add_argument("-m", "--minimum", help="Set minimum length for password", type=int)
    # args = parser.parse_args()
    # print(args)


    



if __name__ == "__main__":
    main()
