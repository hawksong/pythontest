'''
Created on 2017年12月15日
0
@author: user
'''
'''
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
 
# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24
 
np.random.seed(42)
 
# x轴的采样点
x = np.linspace(0, 5, 100)
 
# 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
y = 2*np.sin(x) + 0.3*x**2
y_data = y + np.random.normal(scale=0.3, size=100)
 
# figure()指定图表名称
plt.figure('data')
 
# '.'标明画散点图，每个散点的形状是个圆
plt.plot(x, y_data, '.')
 
# 画模型的图，plot函数默认画连线图
plt.figure('model')
plt.plot(x, y)
 
# 两个图画一起
plt.figure('data & model')
 
# 通过'k'指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
# 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
plt.plot(x, y, 'k', lw=3)
 
# scatter可以更容易地生成散点图
plt.scatter(x, y_data)
 
# 将当前figure的图保存到文件result.png
plt.savefig('result.png')
 
# 一定要加上这句才能让画好的图显示在屏幕上
plt.show()

'''


import matplotlib.pyplot as plt
import numpy as np
# 3D图标必须的模块，project='3d'的定义
from mpl_toolkits.mplot3d.axes3d import *   
 
np.random.seed(42)
 
n_grids = 51            # x-y平面的格点数 
c = n_grids / 2         # 中心位置
nf = 2                  # 低频成分的个数
 
# 生成格点
x = np.linspace(0, 1, n_grids)
y = np.linspace(0, 1, n_grids)
 
# x和y是长度为n_grids的array
# meshgrid会把x和y组合成n_grids*n_grids的array，X和Y对应位置就是所有格点的坐标
X, Y = np.meshgrid(x, y)
 
# 生成一个0值的傅里叶谱
spectrum = np.zeros((n_grids, n_grids), dtype=np.complex)
 
# 生成一段噪音，长度是(2*nf+1)**2/2
noise = [np.complex(x, y) for x, y in np.random.uniform(-1,1,((2*nf+1)**2//2, 2))]
 
# 傅里叶频谱的每一项和其共轭关于中心对称
noisy_block = np.concatenate((noise, [0j], np.conjugate(noise[::-1])))
 
# 将生成的频谱作为低频成分
spectrum[c-nf:c+nf+1, c-nf:c+nf+1] = noisy_block.reshape((2*nf+1, 2*nf+1))
 
# 进行反傅里叶变换
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))
 
# 创建图表
fig = plt.figure('3D surface & wire')
 
# 第一个子图，surface图
ax = fig.add_subplot(1, 2, 1, projection='3d')
 
# alpha定义透明度，cmap是color map
# rstride和cstride是两个方向上的采样，越小越精细，lw是线宽
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='jet', rstride=1, cstride=1, lw=0)
 
# 第二个子图，网线图
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, lw=0.5)
 
plt.show()