tasks = []
for i in range(10):   
    print("\n1.Add Task  2.View Tasks  3.Remove Task")
    ch = input("Enter choice: ")
    if ch == "1":
        t = input("Enter task: ")
        tasks.append(t)
    elif ch == "2":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for j in range(len(tasks)):
                print(j+1, ".", tasks[j])
    elif ch == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
        else:
            print("Invalid number")