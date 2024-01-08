import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

poverty_data = pd.read_csv('povertyestimatesph-copy.csv')
regions_array = poverty_data["Region"].to_numpy()

print(regions_array)

unique_regions, counts = np.unique(regions_array, return_counts=True) # to remove duplicates

print(unique_regions)

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange', 'test']
counts = [40, 100, 30, 55, 20]
bar_labels = ['red', 'blue', '_red', 'orange', "test"]
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', "tab:orange"]

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

#plt.show()
