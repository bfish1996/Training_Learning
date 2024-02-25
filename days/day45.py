'''import os, time

#toDo = [['title 1', 'may', 'high'], ['title 2', 'may', 'medium'], ['title 3', 'may', 'high'], ['title 4', 'august', 'high'] ]

#def prettyPrint()

#def add():
 # time.sleep(3)
 # os.system("clear")
 # title = input("Add the title of your to do list: ")
 # due_date = input("Add the due date: ")
 # priority = input("Add the priority ").lower()
 # card = [title, due_date, priority]
 # toDo.append (card)
 # print("Added")
 # return card, toDo

#def view():
 # time.sleep(3)
 # os.system("clear")
 # view_option = input("Do you want to view all or view by priority?")
 # if view_option == "all":
 #   print(toDo)
 # if view_option == "priority":
  #  priority_option = input("What priority do you want to view?").lower()
  #  for card in toDo:
  #    if priority_option in card:
   #     for item in card:
   #       print(item, end= " | ")

#def remove():
  #time.sleep(3)
  #os.system("clear")
  #which_one = input("What title do you want to remove?")
  #for card in toDo:
  #  if which_one in card:
   #   toDo.remove(card)
   #   print(toDo)
 # return card, toDo

#while True:
  #menu = input(" 1.Add\n 2.View\n 3.Remove\n 4.Edit\n").lower()
 # if menu == "add":
  #  add()
 #if menu == "view":
 #   view()
  #if menu == "remove":
  #  remove()
  #if menu == "edit":
   # which_one = input("What title do you want to edit?")
   # for card in toDo:
     # if which_one in card:
     #   toDo.remove(card)
     #   title = input("Add the title of your to do list: ")
      #  due_date = input("Add the due date: ")
      #  priority = input("Add the priority ").lower()
      #  card = [title, due_date, priority]
      #  toDo.append (card)
       # print(toDo)
  #time.sleep(3)
  #os.system("clear") '''

# | Name | Date | Priority
import os, time
todo = []

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")