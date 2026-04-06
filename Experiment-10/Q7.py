import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.plot(x, y)
plt.title("Line Graph")
plt.show()
plt.bar(x, y)
plt.title("Bar Graph")
plt.show()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
labels = ["A", "B", "C", "D"]
plt.pie(y, labels=labels)
plt.title("Pie Chart")
plt.show()