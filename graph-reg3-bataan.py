import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

povData_reg3Bataan = pd.read_csv('povData-car-abra.csv')

a = povData_reg3Bataan["Municipality/City"].to_numpy()
b = povData_reg3Bataan["Poverty Incidence"].to_numpy()
plt.bar(a, b)

c = povData_reg3Bataan["Standard Error (SE)"].to_numpy()

plt.errorbar(a, b, yerr=c, fmt='o', color='r')
plt.xticks(rotation=90)
plt.show()
