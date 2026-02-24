def create_dict(list1, list2):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = list2[i]
    return d
list1 = []
list2 = []

n = int(input("Enter number of elements: "))
print("Enter elements of list1:")
for i in range(n):
    x = input()
    list1.append(x)
print("Enter elements of list2:")
for i in range(n):
    y = input()
    list2.append(y)
result = create_dict(list1, list2)

print("Dictionary =", result)