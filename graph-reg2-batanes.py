import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

povData_ncr1stDist = pd.read_csv('povData-reg2-batanes.csv')

x = povData_ncr1stDist["Municipality/City"].to_numpy()
y = povData_ncr1stDist["Poverty Incidence"].to_numpy()

plt.fill_between(x, y) # are plot
plt.show()