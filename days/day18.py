counter = 0
number = 7
while True:
    guess = int(input("What's your number"))
    if guess < number:
        print("Too low")
        counter += 1
        continue
    elif guess > number:
        print("Too high")
        counter += 1
        continue
    else:
        print("Got it, only took", counter, "attempts")
        break
        exit()