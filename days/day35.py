ToDo = []


def printList():
    print()
    for item in ToDo:
        print(item)
    print()


def edit():
    print()
    item = input("What do you want to edit?\n")
    if item in ToDo:
        new = input("What do you want to change it to?\n")
        for i in range(0, len(ToDo)):
            if ToDo[i] == item:
                ToDo[i] = new
    else:
        print(f"Sorry, {item} is not in the list")


while True:
    menu = input("View, Add, Remove, Edit or Delete All? ")
    if menu == "add":
        item = input("What do you want to add?: ")
        if item in ToDo:
            print("Item already in list")
        else:
            ToDo.append(item)
    elif menu == "remove":
        item = input("What to remove? ")
        sure = input("Are you sure? ")
        if sure == "yes":
            if item in ToDo:
                ToDo.remove(item)
        else:
            print(f"{item} was not in the list")
    elif menu == "view":
        printList()
    elif menu == "edit":
        edit()
    elif menu == "delete all":
        ToDo = []
    else:
        print("Invalid input")
