import matplotlib.pyplot as plt
import numpy as np

x_data = np.random.random(5) * 2
y_data = np.random.random(5) * 2

plt.plot(x_data, y_data, c="red")
plt.title("Testing project with plot")
plt.show()
