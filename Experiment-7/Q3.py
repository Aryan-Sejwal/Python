with open('city.txt', 'r') as f:
    lines = f.readlines()
print("All city details:")
for line in lines:
    print(line.strip())
print("\nCities with population more than 10 lakhs:")
for line in lines:
    data = line.split()
    city = data[0]
    population = float(data[1])

    if population > 10:
        print(city)
total_area = 0
for line in lines:
    data = line.split()
    area = float(data[2])
    total_area += area

print("\nTotal area of all cities:", total_area)