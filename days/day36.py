rolodex = []

def print_list():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  first = input("First Name: ").strip().capitalize()
  last = input("Last Name: ").strip().capitalize()
  name = f"{first} {last}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("Error, Duplicate")
  print_list()