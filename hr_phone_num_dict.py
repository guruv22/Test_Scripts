num_entries = input("Enter the number of elements:\n")
name_phone_hash = {}
for _ in range(int(num_entries)):
    name,phone = input("Enter name, phone number:\n").split(" ")
    name_phone_hash[name]=phone

for _ in range(int(num_entries)):
    name=input("Enter the name to be searched:\n")
    phone = name_phone_hash.get(name,"Not found")
    if phone == "Not found":
        print(phone)
    else:
        print("{}={}".format(name,phone))
