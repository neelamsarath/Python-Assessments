def login(func):
    def log():
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "Sarath" and password == "123456":
            print("Login successful!")
            func()
        else:
            print("Invalid username or password")
    return log

@login
def homepage():
    print("Welcome to our website!")

homepage()


def val(func):
    def res(age):
        if age >= 18:
            func(age)
        else:
            print("Invalid... Age must be 18 or above.")

    return res

@val
def login(age):
    print("login successful!")

login(21)
login(16)
