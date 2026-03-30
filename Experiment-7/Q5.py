try:
    
    file = open("data.txt", "r")
    data = file.read().splitlines()
    numbers = [int(x) for x in data]
    result = numbers[0] // numbers[1]
    print("Result:", result)
    file.close()

except FileNotFoundError:
    print("Error: File not found")

except ValueError:
    print("Error: Invalid data in file")

except ZeroDivisionError:
    print("Error: Division by zero")

except Exception as e:
    print("Error:", e)