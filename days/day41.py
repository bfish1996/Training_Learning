#website = {'name': None, 'URL' : None, 'description' : None, 'rating' : None}
#add_another = "Yes"

#def add_website(website):
  #for A, B in website.items():
   # website[A] = input(f"Enter {A}: ")
  #print(website)
  #return website

#while add_another == "Yes":
  #website = add_website(website)
  #print()
  #for A, B in website.items():
   # print(f"{A}: {B}")
  #print()
  #add_another = input("Add another? ")

website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")