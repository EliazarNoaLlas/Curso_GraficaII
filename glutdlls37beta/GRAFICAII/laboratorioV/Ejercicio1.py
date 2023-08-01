import matplotlib.pyplot as plt
import numpy as np

def draw_simpson_head(x, y):
    plt.plot(x, y, linewidth=2)
    plt.fill(x, y, 'yellow')

    # Draw the eyes
    plt.plot([0.2, 0.4], [0.8, 0.8], 'black', linewidth=1)
    plt.plot([0.7, 0.9], [0.8, 0.8], 'black', linewidth=1)

    # Draw the mouth
    plt.plot([0.4, 0.7], [0.8, 0.6], 'black', linewidth=1)
    plt.plot([0.5, 0.6], [0.7, 0.5], 'black', linewidth=1)
    plt.plot([0.6, 0.7], [0.6, 0.4], 'black', linewidth=1)

    plt.show()

x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x) * 0.8 + 0.5

draw_simpson_head(x, y)