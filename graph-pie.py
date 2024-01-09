import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels)
plt.show()