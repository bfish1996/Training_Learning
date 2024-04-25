f = open("days/day48.txt", "a+")
while True:
  whatText = input("> ")
  f.write(f"{whatText}\n")
  done = input("Done? y/n > ")
  if done == "y":
    f.close()
    break