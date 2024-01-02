movie = input("What's your fav movie? ")
if movie == "Ironman":
  print("I love Ironman!")
  ironman = input("Which Ironman? ")
  if ironman == "1":
    print("Ironman 1 is always a classic")
  else:
    print("Ironman 2 is the best")
elif movie == "Thor":
  print("Thor is awesome")
  thor = input("Which Thor?")
  if thor == "1":
    print("Thor 1 is the best!")
  else:
    print("Thor 2 is the best!")
elif movie == "Captain America":
  print("Captain America is awesome")
  captain = input("Which one?")
  if captain == "1":
    print("Captain America 1 is the best!")
  else: 
    print("meh...")
else:
  print("I don't know that movie")