import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

carAbra = pd.read_csv('povData-car-abra.csv')
ncr1stDist = pd.read_csv('povData-ncr-1stDist.csv')
reg1IlocNorte = pd.read_csv('povData-reg1-ilocNorte.csv')
reg2Batanes = pd.read_csv('povData-reg2-batanes.csv')
reg3Bataan = pd.read_csv('povData-reg3-bataan.csv')
povData = pd.read_csv('povertyestimatesph-copy.csv')

def average(num):
    return sum(num) / len(num)

x = povData["Region"].to_numpy()
y = povData["Poverty Incidence"].to_numpy()
sizes = povData["Poverty Incidence"].to_numpy()

plt.scatter(x, y, s=sizes)

plt.xlabel('Region in the Philippines')
plt.ylabel('Poverty Incidence')

plt.xticks(rotation=90)
plt.show()