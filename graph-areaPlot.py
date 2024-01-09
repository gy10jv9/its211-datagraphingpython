import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create data
x = range(1, 6)
y = [1, 4, 6, 8, 4]

# Create an area plot
plt.fill_between(x, y)

# Display the plot
plt.show()