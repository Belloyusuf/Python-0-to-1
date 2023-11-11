# simple string tester

def ask_name():
    username = input("Enter your name: ")
    print("My name is ", username + " and name type is ", type(username))

if __name__ == "__main__":
    ask_name()