import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot(x, y):
    x, y = np.meshgrid(x, y)
    z = x ** 2 + y ** 2

    gradient = [2 * x, 2 * y]

    axes = plt.axes(projection='3d')
    axes.plot_surface(x, y, z)
    # plt.show()
