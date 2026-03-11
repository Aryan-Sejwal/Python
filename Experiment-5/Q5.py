n = int(input("Enter number of movies: "))
movies = {}
for i in range(n):
    name = input("\nMovie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Cost: "))
    earn = float(input("Earning: "))
    movies[name] = [year, director, cost, earn]
print("\nAll movie details:", movies)
print("\nBefore 2015:")
for m in movies:
    if movies[m][0] < 2015:
        print(m)
print("\nProfit movies:")
for m in movies:
    if movies[m][3] > movies[m][2]:
        print(m)
d = input("\nEnter director: ")
for m in movies:
    if movies[m][1].lower() == d.lower():
        print(m)