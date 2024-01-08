import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

povData_ncr = pd.read_csv('povData-ncr.csv')

x = povData_ncr["Municipality/City"].to_numpy()
y = povData_ncr["Poverty Incidence"].to_numpy()

'''
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 24, 36, 40, 50]
'''

plt.bar(x, y)
plt.xticks(rotation=90)
plt.show()
