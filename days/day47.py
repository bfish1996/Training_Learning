import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 44, "Guile": 50, "Baldness": 99}
trumps["Monica From Friends"] = {"Intelligence": 150, "Speed": 48, "Guile": 30, "Baldness": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 0, "Guile": 200, "Baldness": 101}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Select your character \n>")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)
  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")
  answer = input("> ")
  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")
  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")
  time.sleep(2)
  os.system("clear")