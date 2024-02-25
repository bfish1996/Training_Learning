#print("MokéBeast")
#print()

#beast = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

#def add_beast():
  ##for name, value in beast.items():
    #  beast[name] = input(f"{name}:\t").strip().title()

#while True:
  #add_beast()
  #add_another = input("Add another?").lower()
  #if add_another == "yes":
  #  continue
  #if add_another == "no":
  #  break

#mokedex = {"Beast":beast}

#print(beast)
#print(mokedex)

#if mokedex["Type"]=="Earth":
  #print("\033[32m", end="")
#elif mokedex["Type"]=="Air":
  #print("\033[37m", end="")
#elif mokedex["Type"]=="Fire":
 # print("\033[31m", end="")
#elif mokedex["Type"]=="Water":
#  print("\033[34m", end="")
#else:
#  print("\033[33m", end="")

#for name, value in mokedex.items():
#  print(f"{name:<15}: {value}")

import os, time

mokedex = {}

def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()