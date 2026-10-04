import matplotlib.pyplot as plt
import numpy as np

groceries = np.array([
    "Milk",
    "Bread",
    "Eggs",
    "Chicken",
    "Potatoes",
    "Rice",
    "Tomatoes",
    "Cheese"
])

values = np.array([4, 3, 2, 5, 3, 1, 4, 6])

plt.bar(groceries, values)
plt.title("Grocery")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()