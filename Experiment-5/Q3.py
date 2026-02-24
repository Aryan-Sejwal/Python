n=int(input('enter the number of scores = '))
scores = []
for i in range(n):
    value = int(input("Enter score = "))
    scores.append(value)
unique_scores = list(set(scores))
unique_scores.sort()
runner_up = unique_scores[-2]
print("Runner-up score =", runner_up)