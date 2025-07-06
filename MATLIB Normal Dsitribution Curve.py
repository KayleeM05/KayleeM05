# Using matplotlib

import matplotlib.pyplot as plt
import numpy as np


mu = -10
sigma = np.sqrt(25)

# Generate X values from -25 to 5
x = np.linspace(mu - 25*sigma, mu + 25*sigma, 1000)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2)) # 2's don't change

# plot normal distribution
plt.plot(x, pdf, label='Normal Distribution', color='blue')

# Shade area between -25 and 5

x_shade = np.linspace(-25, 5, 1000)
pdf_shade = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x_shade - mu)**2 / (2 * sigma**2))
plt.fill_between(x_shade, pdf_shade, alpha=0.4, color='orange', label='P(-25 <= Y <= 5)')


# Labeling

plt.title("Normal Distribution Curve")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show(block=True)

