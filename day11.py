seconds = 1
minute = 60 * seconds
hour = 60 * minute
day = 24 * hour
week = 7 * day
month = 31 * day
year = 365 * day
leap_year = 366 * day
days_in_year = int(input("Enter the number of days in the year: "))
if days_in_year == 365:
  print(year)
elif days_in_year == 366:
  print(leap_year)
else:
  print("That's not a real year")