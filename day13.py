test = input("What's the test name? ")
score = int(input("What was your score? "))
max_score = int(input("What was the max score? "))
print()
final_score = (score/max_score) * 100
grade = round(final_score, 2)
if grade <= 50:
  print(f"You got a {grade}% on the {test} test. You failed.")
elif grade >50 and grade < 70:
  print(f"You got a {grade}% on the {test} test. You get a C.")
elif grade > 70 and grade <= 80:
  print(f"You got a {grade}% on the {test} test. You get a B.")
elif grade > 80:
  print(f"You got a {grade}% on the {test} test. You get an A.")
else:
  print("Try again!")