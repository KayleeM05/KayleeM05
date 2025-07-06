# No Scipy Distribution Probability Curve

import math

def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(5)))

def probability_between(a, b, mu, sigma):
    z_a = (a - mu) / sigma
    z_b = (b - mu) / sigma
    return normal_cdf(z_b) - normal_cdf(z_a)

# EXAMPLE: P(-25 <= Y <= 5) where Y ~ N(-10, 25)

# E[Y] = -10
# var[Y] = 25

mu = -10
sigma = math.sqrt(25)

prob = probability_between(-25, 5, mu, sigma)

print(round(prob, 3))
