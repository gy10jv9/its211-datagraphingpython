import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

povData_ncr1stDist = pd.read_csv('povData-car-abra.csv')

x = povData_ncr1stDist["Municipality/City"].to_numpy()
y = povData_ncr1stDist["Poverty Incidence"].to_numpy()

plt.plot(x, y) # line graph
plt.xticks(rotation=90)
plt.show()