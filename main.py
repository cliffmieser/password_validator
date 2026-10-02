"""
 Project 1 
 Sep 30 2026
 
 Goals: A (very) simple CLI password checker and validator. 

 Structure:
    [*] main.py -> CLI entry point, handles inputs/flags, outputs report 
    [*] rules.py -> functions to test length, charset, and patterns
    [*] common_password.txt -> list of most common passwords
    [ ] scoring.py (WIP)-> logic to calculate score or entropy and returns a rating

 """

import sys
import argparse # CLI parsing module
import getpass # prompt for password with echo turned off
from rules import rate_length, rate_diversity, calc_entropy
from common_passwords import read_seclist

def pw_report(pw_dict: dict, entropy_score: float, length_rating: str):


    print(f"\n--- Password Evaluation ---")
    print(f"Length: {pw_dict["length"]} --> ({length_rating})")
    print(f"Character Pool Size: {pw_dict["pool_size"]}")
    print(f"Entropy: {entropy_score:.2f} bits")


def has_args() -> bool:
    """ Checks if args were passed to terminal"""
    if (len(sys.argv) <= 1):
        return False# no args provided
    else: return True


    

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Test password strength at the command line")
    parser.add_argument("-p", "--password", help="Read user provided passoword string", type=str)
    parser.add_argument("-m", "--minimum", help="Set minimum length for password", type=int)
    args = parser.parse_args()
    return args


def get_password() -> str: # returns a string representing passowrd
    pw = getpass.getpass("Enter a password: ")
    if (pw in read_seclist()):
        while (pw in read_seclist()):
            print("Password unsecure (exists in secList 10k most common passwords), Try again...")
            pw = getpass.getpass("Enter a password: ")
    else:
        return str(pw)

def get_scores(password: str) -> tuple:
        char_diversity_dict = rate_diversity(password) # rates diversity of characters
        entropy = calc_entropy(len(password), char_diversity_dict["pool_size"]) # calculates password entropy
        length_rating = rate_length(password) # rates length of password string

        return (char_diversity_dict, entropy, length_rating)

def main():
    # CLI entry point

    #call check_argparser function first check for args (if any)

    if (len(sys.argv) <= 1): # if no args providedk ==  vars(get_args())[k] and
        pw = get_password()

        scores = get_scores(pw)
        # char_diversity_dict = rate_diversity(pw) # rates diversity of characters
        # entropy = calc_entropy(len(pw), char_diversity_dict["pool_size"]) # calculates password entropy
        # length_rating = rate_length(pw) # rates length of password string
        pw_report(*scores)
    elif (has_args() == True and bool(args_filtered:= list(filter(lambda k: vars(get_args())[k] is not None, args_dict:= vars(get_args()))))): # args provided by user 
        # has arguments AND arguments dict has at least one non-None value
        # dictionary of arguments stored in args_dict
        result = {}
        for idx, arg in enumerate(args_filtered):
            # idx: index of item (int),  arg: the argument (str)
            match arg:
                case "password": 
                    pw = args_dict["password"]
                    result.update({"password": pw})
                    # scores = get_scores(pw)
                    # pw_report(*scores)
                case "minimum":
                    result.update({"minimum": args_dict[arg]})
                    if "password" not in result.keys():
                        # get the password
                        while (True): # loop for ensureing password length meets minimum required length
                            pw = get_password()
                            if len(pw) <  result["minimum"]:
                                print(f"Error: password must meet minium length requirement ({result["minimum"]})...")
                                pw = get_password()
                            else:
                                result.update({"password": pw})
                                break
                    else: continue # break out of loop

        scores = get_scores(pw)
        pw_report(*scores)
        
        # print(f"result -> {result}")


if __name__ == "__main__":


    main()
