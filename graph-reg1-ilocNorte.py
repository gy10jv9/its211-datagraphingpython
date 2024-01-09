import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

povData_ncr1stDist = pd.read_csv('povData-reg1-ilocNorte.csv')

x = povData_ncr1stDist["Municipality/City"].to_numpy()
y = povData_ncr1stDist["Poverty Incidence"].to_numpy()

plt.scatter(x, y) # scatter plot
plt.xticks(rotation=90)
plt.show()