# coding=gbk
# 学习场所： 家里
# 写 习 者：刘明阳
# 学习时间：2021/2/10  17:32
# encoding=utf-8
import matplotlib.pyplot as plt
import numpy as np

""" 2D图，有图例，横坐标为"Parameters"，纵轴为"Accuracy,test set"，图例在左下角，五种方法，用点段描述，不同颜色表示，加格点 1. APOZ (Hu et at., 2016) 2. Minimum weight 3. Random 4. Activation(mean) 5. ours """

plt.rcParams['font.sans-serif']=['Arial']  #如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False  #显示负号

x = np.array([1.0,0.8,0.6,0.4,0.2,0.0])
y = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

APOZ = np.array([[1.0,0.801],[0.88,0.792],[0.78,0.77],[0.69,0.74],[0.57,0.71],[0.39,0.48],[0.21,0.31],[0.15,0.035]])
MinWeight = np.array([[1.0,0.801],[0.90,0.775],[0.75,0.76],[0.60,0.71],[0.37,0.57],[0.26,0.39],[0.14,0.01]])
Random = np.array([[1.0,0.801],[0.925,0.775],[0.82,0.755],[0.70,0.715],[0.585,0.68],[0.475,0.57],[0.27,0.435],[0.11,0.145]])
ActMean = np.array([[1.0,0.801],[0.89,0.8],[0.78,0.785],[0.68,0.77],[0.57,0.735],[0.42,0.69],[0.215,0.52],[0.04,0.03]])
ours = np.array([[1.0,0.801],[0.8,0.795],[0.694,0.78],[0.639,0.768],[0.612,0.763],[0.606,0.762],[0.4,0.71],[0.25,0.55],[0.1,0.20]])

#
#label在图示(legend)中显示。若为数学公式，则最好在字符串前后添加"$"符号
#color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
#线型：- -- -. : ，
#marker：. ， o v < * + 1
plt.figure(figsize=(5,5))
plt.grid(linestyle = "--")      #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False) #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框

xgroup_labels=['100%','80%','60%','40%','20%','0%'] #x轴刻度的标识
ygroup_labels=['0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0'] #y轴刻度的标识

plt.xticks(x,xgroup_labels[::-1],fontsize=18,fontweight='bold') #默认字体大小为10
plt.yticks(y,ygroup_labels,fontsize=18,fontweight='bold')

# 先画折现图
# [::-1]
plt.plot(1-APOZ[:,0],APOZ[:,1],color="cyan",label="APOZ (Hu et at., 2016)",linewidth=2.5)
plt.plot(1-MinWeight[:,0],MinWeight[:,1],"red",label="Minimum weight",linewidth=2.5)
plt.plot(1-Random[:,0],Random[:,1],color="magenta",label="Random",linewidth=2.5)
plt.plot(1-ActMean[:,0],ActMean[:,1],"green",label="Activation(mean)",linewidth=2.5)
plt.plot(1-ours[:,0],ours[:,1],"blue",label="ours",linewidth=2.5)

# 再画散点图
plt.scatter(1-APOZ[:,0],APOZ[:,1],c = 'cyan',s=150,marker = '.')
plt.scatter(1-MinWeight[:,0],MinWeight[:,1],c = 'red',s=150,marker = '.')
plt.scatter(1-Random[:,0],Random[:,1],c = 'magenta',s=150,marker = '.')
plt.scatter(1-ActMean[:,0],ActMean[:,1],c = 'green',s=150,marker = '.')
plt.scatter(1-ours[:,0],ours[:,1],c = 'blue',s=150,marker = '.')

plt.title("Parameters Vs Accuracy",fontsize=20,fontweight='bold')    #默认字体大小为12
plt.xlabel("Parameters",fontsize=20,fontweight='bold')
plt.ylabel("Accuracy,test set",fontsize=20,fontweight='bold')
plt.xlim(0.0,1.0)         #设置x轴的范围
plt.ylim(0.0,1.0)

plt.legend()          #显示各曲线的图例
plt.legend(loc=3,numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext,fontsize=20,fontweight='bold') #设置图例字体的大小和粗细

plt.show()
