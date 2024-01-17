counter = 0
mult = int(input("Enter a number you want to multiply "))
for i in range(1, 11):
    Question = int(input("What is " + str(mult) + " x " + str(i) + " "))
    if Question == (mult * i):
        print("Correct")
        counter += 1
        continue
    else:
        print("Incorrect")
        continue
else:
    print("Nice job!")
    print("You got " + str(counter) + " out of 10")
