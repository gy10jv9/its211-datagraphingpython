import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create data
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])
sizes = np.array([20, 40, 60, 80, 100])

# Create a bubble chart
plt.scatter(x, y, s=sizes)

# Label the axes and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Basic Bubble Chart')

# Display the plot
plt.show()