import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = [1, 3, 5, 7]
b = [11, 2, 4, 19]
plt.bar(a, b)

c = [1, 3, 2, 1]
plt.errorbar(a, b, yerr=c, fmt='o', color='r')

plt.show()
