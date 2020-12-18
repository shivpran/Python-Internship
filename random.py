import random
import numpy as np
import matplotlib.pyplot as plt

rolls = []
for k in range(100):
    rolls.append(random.choiice([1,2,3,4,5,6]))
plt.hist(rolls, bins=np.linespce(0.5,6.5,7))
