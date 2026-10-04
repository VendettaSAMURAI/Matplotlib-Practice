import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = np.array([5, 10, 15, 20, 25])

plt.grid(
    axis='y',
    linewidth=2,
    color="lightgray",
    linestyle="dashed"
)

plt.plot(x, y1)
plt.show()