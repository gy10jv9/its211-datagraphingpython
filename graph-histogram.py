import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Predefined data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a histogram plot
plt.hist(data, bins=range(min(data), max(data) + 2), align='left', color='skyblue', edgecolor='black')

# Label the axes and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

# Display the plot
plt.show()


