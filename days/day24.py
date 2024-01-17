def accountDetails():
    while True:
        name = input("Enter your name: ")
        password = input("Enter password: ")
        if name != "Ben" and password != "Hi!":
            print("Try again")
            continue
        else:
            print("Welcome in!")
            break


print("Log in system")
accountDetails()
