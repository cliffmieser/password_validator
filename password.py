





class Password:
    def __init__(self, pass_w: str):
        """
            Creates an instance of Password 

            pass_w: A string representing usr provided password
        """
        self.password = pass_w
        self.is_banned =  False

    def check_banned_pw(self):
        # checks list of banned passwords, sets boolean if in list 
        return 

    def get_password(self):
        # gets usr input, stores it in self.password attribute
        self.password = input("Enter a password: ")
        
    @property
    def size(self):
        return f"String length: {len(self.password)}"
