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
import os.path
import sys
from password import Password # class defination & class methods to hold info about password string 



def main():
    # CLI entry point
    if (len(sys.argv) > 0): # get usr input from cli
        usr_password = Password( pass_w = sys.argv[1])
    else:
        usr_password = Password("")
        usr_password.get_password()

    print(usr_password.size)


if __name__ == "__main__":
    main()
