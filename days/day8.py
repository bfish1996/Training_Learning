print("Howdy partner, welcome!")
print()
print("We're going to go on a journey!")
name = input("Let's start with your name: ")
print("Hey" + " " + name + "!")
print()
day = input("What day is it today? ")
print("So it's" + " " + day + "?")
if day == "Monday" or day == "monday":
  print ("Monday is a cool day!" + " " + name)
elif day == "Tuesday" or day == "tuesday":
  print ("Tuesday boo day!")
elif day == "Wednesday":
      print ("Wednesday is the middle of the week!")
      weds_task = input("What do you want to do today? ")
      if weds_task == "Go to the park":
          print("I love the park!")
      elif weds_task == "Ride":
          print("Woooohoooo")
      else:
          print ("Wow," + " " + weds_task + " " + "is a cool thing!")
elif day == "Thursday":
  print ("Thursday is almost over! So close!!!!")
elif day == "Friday":
  print ("It's Friday again!")
elif day == "Saturday":
  print ("Sat is the best!")
elif day == "Sunday":
  print ("Sunday funday!")
else:
  print("Are you sure that day exists??")
