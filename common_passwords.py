# reads in a list of 10k most common passowrds 

def read_seclist():
    common_passwords = set()

    with open("10k-most-common.txt", 'r') as f:
        lines = f.readlines() # get every password in f


    for line in lines:
        common_passwords.add(line.rstrip())

    return common_passwords # return the set
    