ToDo = []

def printList(): 
  print()
  for item in ToDo:
    print(item)
  print()

while True:
  menu = input("View, Add or Remove? ")
  if menu == "add":
    item = input("What do you want to add?: ")
    ToDo.append(item)
  elif menu == "remove":
    item = input("What to remove? ")
    if item in ToDo:
      ToDo.remove(item)
    else:
      print(f"{item} was not in the list")
  elif menu == "view":
    printList()
  else:
    print("Invalid input")