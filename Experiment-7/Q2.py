with open('numbers.txt', 'r') as f:
    numbers = f.read().splitlines()
numbers = [int(num) for num in numbers]
max_num = max(numbers)
print("Maximum number:", max_num)
average = sum(numbers) / len(numbers)
print("Average:", average)
count = 0
for num in numbers:
    if num > 100:
        count += 1

print("Numbers greater than 100:", count)