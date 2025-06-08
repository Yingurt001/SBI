import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
import os  

y = 10
N = 100
alpha = beta_ = 1


theta = np.linspace(0, 1, 100)
posterior = beta.pdf(theta, y + alpha, N - y + beta_)

plt.plot(theta, posterior, label="Posterior")
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\pi(\theta \mid y)$")
plt.title("Posterior Density π(θ|y)")
plt.grid()
plt.legend()
plt.show()
