myUser = {"name" : "", "DOB" : "", "phone" : "", "email" : "", "address" : ""}
myUser["name"] = input("Please share your name")
myUser["DOB"] = input("Please share your date of birth")
myUser["phone"] = input("Please share your phone number")
myUser["email"] = input("Please share your email address")
print(myUser['name'], myUser['DOB'], myUser['phone'], myUser['email'])

#Or can do this way

#name = input("Name: ").strip().capitalize()
#dob = input("Date of Birth: ").strip()
#tel = input("Telephone number: ").strip()
#email = input("Email: ")
#address = input("Address: ")
#contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

#print()
#print(f"""Name: {contact["name"]}""")
#print(f"""DOB: {contact["dob"]}""")
#print(f"""Tel: {contact["tel"]}""")
#print(f"""Email: {contact["email"]}""")
#print(f"""Address: {contact["address"]}""")