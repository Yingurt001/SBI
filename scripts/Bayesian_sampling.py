import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


y = 80
N = 100
alpha = beta_ = 1


a_post = y + alpha
b_post = N - y + beta_

# sampling process
samples = beta.rvs(a_post, b_post, size=5000)

# Plot histgrams
plt.hist(samples, bins=50, density=True, alpha=0.6, label="Posterior Samples")
plt.xlabel(r"$\theta$")
plt.ylabel("Density")
plt.title("Samples from Posterior Distribution")
plt.grid()
plt.legend()
plt.show()
