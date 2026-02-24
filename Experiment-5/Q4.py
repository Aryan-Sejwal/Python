n = int(input("Enter number of persons = "))
D = {}
for i in range(n):
    name = input("Enter name = ")
    city = input("Enter city = ")
    D[name] = city
print("\nNames:", list(D.keys()))
print("Cities:", list(D.values()))
print("\nName and City:")
for k, v in D.items():
    print(k, "-", v)
count = {}
for city in D.values():
    count[city] = count.get(city, 0) + 1
print("\nCity count:", count)