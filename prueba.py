
import numpy as np; import matplotlib.pyplot as plt; X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ]); N=len(X)
fig, ax = plt.subplots(figsize=(2.5, 2.5)); plt.grid(True); plt.axis([-1.5, 3.5, -1.5, 3.5])
plt.xticks(range(-1,4)); plt.yticks(range(-1,4)); plt.scatter(*X.T, facecolor='C0', edgecolor='k', s=64)