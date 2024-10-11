class Login:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.attempts = 0
        self.AttemptsAllowed = 3
        self.passwordRetyped = ""

    def fetchUserName(self):
        self.username = input("Enter username -> ")

    def validate_password(self):
        if self.password != self.passwordRetyped:
            print("Passwords do not match. Please try again.")
            return False
        return True

    def login(self):
        self.displayLogin()
        self.fetchUserName()
        while self.attempts < self.AttemptsAllowed:
            self.fetchPassword()
            self.fetchPasswordReentered()
            if self.validate_password():
                print("Login successful!")
                break
            else:
                self.attempts += 1
                print("Incorrect password. Attempts remaining:"+str(self.AttemptsAllowed - self.attempts))

        if self.attempts == self.AttemptsAllowed:
            print("Maximum attempts exceeded. Login failed.")
    
    def displayLogin(self):
        print("-----------")
        print("Login Main Page")
        print("-----------")
    
    def fetchPassword(self):
        self.password = input("Enter password -> ")

    def fetchPasswordReentered(self):
        self.passwordRetyped = input("Re-entered password ->")

Login().login()