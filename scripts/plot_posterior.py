import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
import os  # 新增模块

# 设置参数
y = 80
N = 100
alpha = beta_ = 1

# 生成 theta 和后验密度
theta = np.linspace(0, 1, 100)
posterior = beta.pdf(theta, y + alpha, N - y + beta_)

# 设置输出路径
output_dir = "/Users/zhangying/Documents/Research/figures"
output_path = os.path.join(output_dir, "posterior_plot.png")

# 自动创建输出文件夹（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 绘图并保存
plt.plot(theta, posterior, label="Posterior")
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\pi(\theta \mid y)$")
plt.title("Posterior Density π(θ|y)")
plt.grid()
plt.legend()
plt.savefig(output_path)
plt.show()
