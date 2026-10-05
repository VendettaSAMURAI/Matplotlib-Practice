import matplotlib.pyplot as plt

# Example data
x = [10, 20, 30, 40, 50, 60]
y = [15, 25, 28, 45, 48, 65]

# Create scatterplot
plt.scatter(x, y, label="Data points")

# Labels and title
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.title("Scatterplot")

# Legend
plt.legend()

# Display
plt.show()