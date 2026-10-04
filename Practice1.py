import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y = np.array([15,25,30,20])
y2 = np.array([25,35,45,50])

plt.plot(x,y, marker='*',
            markersize='30',
            markerfacecolor='cyan',
            linestyle='none',
            linewidth=2)
plt.plot(x,y2)
plt.show()