# Normal Distribution Utiizing Scipy

from scipy.stats import norm
import math

# What are the parameters?

mu = -10 # the mean
sigma = math.sqrt(25) #sqrt of varience

# define bounds
lower_bound = -25
upper_bound = 5

# calculate the cumulative properties
p_upper = norm.cdf(upper_bound, loc=mu, scale=sigma)
p_lower = norm.cdf(lower_bound, loc=mu, scale=sigma)

# Final probability
probability = p_upper - p_lower

# What's the probability
print(f"P({lower_bound} <= Y <= {upper_bound}) = {probability:.3f}")

