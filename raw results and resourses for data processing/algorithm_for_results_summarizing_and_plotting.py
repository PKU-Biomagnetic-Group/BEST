import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
from matplotlib import rcParams

config = {
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 16,
    "mathtext.fontset": "custom",
    "mathtext.rm": "serif",
    "mathtext.bf": "serif:bold",
    "mathtext.it": "serif:italic",
    "mathtext.cal": "serif",
    "mathtext.tt": "monospace",
    "mathtext.sf": "sans",
    "mathtext.fallback_to_cm": False,
}
rcParams.update(config)

# 原始数据点
x = np.array([0.5, 1, 1.5, 2, 2.5, 3, 4])
y = np.array([0.5, 1, 1.5, 2, 2.5, 3, 4])
# y = np.array([2, 2.5, 3, 4, 5])

z = np.array([[0.8545, 0.84075, 0.83325, 0.82875, 0.82, 0.8145, 0.79525],
              [0.84975, 0.837, 0.835, 0.8265, 0.81775, 0.7975, 0.7715],
              [0.846, 0.8415, 0.82825, 0.82675, 0.824, 0.81075, 0.7985],
              [0.8395, 0.84275, 0.83, 0.82775, 0.8205, 0.81425, 0.80325],
              [0.8235, 0.837, 0.82325, 0.82575, 0.816, 0.8085, 0.7945],
              [0.8435, 0.83075, 0.845, 0.83275, 0.8195, 0.81375, 0.8025],
              [0.83675, 0.85775, 0.822, 0.82525, 0.8165, 0.80925, 0.79275]])
# z = np.array([[0.92125, 0.915, 0.901, 0.8965, 0.89, 0.875, 0.8635],
#               [0.89925, 0.891, 0.89175, 0.88075, 0.86575, 0.8505, 0.833],
#               [0.891, 0.86725, 0.8615, 0.85525, 0.8465, 0.841, 0.82725],
#               [0.8545, 0.837, 0.82825, 0.82775, 0.8205, 0.81375, 0.79275],
#               [0.81275, 0.815, 0.803, 0.828, 0.79, 0.78475, 0.7895]])
# z = np.array([[0.92125, 0.9225, 0.917, 0.90125, 0.91575, 0.915, 0.916],
#               [0.89925, 0.9205, 0.911, 0.916, 0.8845, 0.87975, 0.90525],
#               [0.891, 0.87525, 0.877, 0.88075, 0.877, 0.901, 0.85975],
#               [0.8545, 0.84975, 0.846, 0.8395, 0.8235, 0.8435, 0.83675],
#               [0.81275, 0.82125, 0.8125, 0.8125, 0.81575, 0.833, 0.80825]])


interp_func = interp2d(x, y, z, kind='linear')

# 定义插值的目标点
x_interp = np.linspace(0, 4, 400)
y_interp = np.linspace(0, 4, 400)
# y_interp = np.linspace(2, 5, 300)

# 进行插值
z_interp = interp_func(x_interp, y_interp)

fig1 = plt.figure(1)

# 绘制热图
plt.imshow(z_interp, cmap='rainbow', origin='lower', extent=[x_interp.min(), x_interp.max(), y_interp.min(), y_interp.max()])
plt.colorbar()
plt.clim(0.77, 0.86)

# 添加标题和坐标轴标签
# plt.title('plot')
plt.xlabel('$\mathit{h}$/cm')
plt.ylabel('$\mathit{a}$/cm')

fig2 = plt.figure(2)

# Set up a color map for differentiating each row
colors = plt.cm.rainbow(np.linspace(0, 1, len(z)))

# Plot each row of z against x with a different color'
# ylist = [2, 2.5, 3, 4, 5]
ylist = [0.5, 1, 1.5, 2, 2.5, 3, 4]
for i, row in enumerate(z):
    plt.plot(x, row, color=colors[i], linestyle='dashed', marker='o', markersize=8, label=r'$\mathit{a}$ = %.1f cm'%ylist[i])

plt.xlabel('$\mathit{h}$/cm')
plt.ylabel('Accuracy')
# plt.title('Plot of z rows against x')
plt.legend()
plt.grid(True)

fig3 = plt.figure(3)

# Set up a color map for differentiating each row
colors = plt.cm.rainbow(np.linspace(0, 1, len(z.T)))

# Plot each row of z against x with a different color
xlist = [0.5, 1, 1.5, 2, 2.5, 3, 4]
for i, row in enumerate(z.T):
#     print(i)
    plt.plot(y, row, color=colors[i], linestyle='dashed', marker='o', markersize=8, label=r'$\mathit{h}$ = %.1f cm'%xlist[i])

plt.xlabel('$\mathit{a}$/cm')
plt.ylabel('Accuracy')
# plt.title('Plot of z rows against y')
plt.legend()
plt.grid(True)

# 显示图形
plt.show()