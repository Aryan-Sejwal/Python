contacts = {}
for i in range(10):   
    print("\n1.Add  2.Search  3.Update  4.Delete  5.Show")
    ch = input("Enter choice: ")
    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif ch == "2":
        name = input("Search name: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Not found")
    elif ch == "3":
        name = input("Update name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
        else:
            print("Not found")
    elif ch == "4":
        name = input("Delete name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Not found")
    elif ch == "5":
        for n, p in contacts.items():
            print(n, ":", p)