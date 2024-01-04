year = int(input("What year were you born in? "))
if year < 1925:
    print("You're ancient!")
elif year <= 1946:
    print("You're a traditionalist!")
elif year <= 1964:
    print("You're a Baby boomer! ")
elif year <= 1981:
    print("You're a GenX ")
elif year <= 1995:
    print("You're a Millenial ")
elif year <= 2015:
    print("You're a GenZ ")
else:
    print("You're too young")
