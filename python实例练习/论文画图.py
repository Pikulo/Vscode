# coding=gbk
# ѧϰ������ ����
# д ϰ �ߣ�������
# ѧϰʱ�䣺2021/2/10  17:32
# encoding=utf-8
import matplotlib.pyplot as plt
import numpy as np

""" 2Dͼ����ͼ����������Ϊ"Parameters"������Ϊ"Accuracy,test set"��ͼ�������½ǣ����ַ������õ����������ͬ��ɫ��ʾ���Ӹ�� 1. APOZ (Hu et at., 2016) 2. Minimum weight 3. Random 4. Activation(mean) 5. ours """

plt.rcParams['font.sans-serif']=['Arial']  #���Ҫ��ʾ�������壬���ڴ˴���Ϊ��SimHei
plt.rcParams['axes.unicode_minus']=False  #��ʾ����

x = np.array([1.0,0.8,0.6,0.4,0.2,0.0])
y = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

APOZ = np.array([[1.0,0.801],[0.88,0.792],[0.78,0.77],[0.69,0.74],[0.57,0.71],[0.39,0.48],[0.21,0.31],[0.15,0.035]])
MinWeight = np.array([[1.0,0.801],[0.90,0.775],[0.75,0.76],[0.60,0.71],[0.37,0.57],[0.26,0.39],[0.14,0.01]])
Random = np.array([[1.0,0.801],[0.925,0.775],[0.82,0.755],[0.70,0.715],[0.585,0.68],[0.475,0.57],[0.27,0.435],[0.11,0.145]])
ActMean = np.array([[1.0,0.801],[0.89,0.8],[0.78,0.785],[0.68,0.77],[0.57,0.735],[0.42,0.69],[0.215,0.52],[0.04,0.03]])
ours = np.array([[1.0,0.801],[0.8,0.795],[0.694,0.78],[0.639,0.768],[0.612,0.763],[0.606,0.762],[0.4,0.71],[0.25,0.55],[0.1,0.20]])

#
#label��ͼʾ(legend)����ʾ����Ϊ��ѧ��ʽ����������ַ���ǰ�����"$"����
#color��b:blue��g:green��r:red��c:cyan��m:magenta��y:yellow��k:black��w:white������
#���ͣ�- -- -. : ��
#marker��. �� o v < * + 1
plt.figure(figsize=(5,5))
plt.grid(linestyle = "--")      #���ñ���������Ϊ����
ax = plt.gca()
#ax.spines['top'].set_visible(False) #ȥ���ϱ߿�
#ax.spines['right'].set_visible(False) #ȥ���ұ߿�

xgroup_labels=['100%','80%','60%','40%','20%','0%'] #x��̶ȵı�ʶ
ygroup_labels=['0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0'] #y��̶ȵı�ʶ

plt.xticks(x,xgroup_labels[::-1],fontsize=18,fontweight='bold') #Ĭ�������СΪ10
plt.yticks(y,ygroup_labels,fontsize=18,fontweight='bold')

# �Ȼ�����ͼ
# [::-1]
plt.plot(1-APOZ[:,0],APOZ[:,1],color="cyan",label="APOZ (Hu et at., 2016)",linewidth=2.5)
plt.plot(1-MinWeight[:,0],MinWeight[:,1],"red",label="Minimum weight",linewidth=2.5)
plt.plot(1-Random[:,0],Random[:,1],color="magenta",label="Random",linewidth=2.5)
plt.plot(1-ActMean[:,0],ActMean[:,1],"green",label="Activation(mean)",linewidth=2.5)
plt.plot(1-ours[:,0],ours[:,1],"blue",label="ours",linewidth=2.5)

# �ٻ�ɢ��ͼ
plt.scatter(1-APOZ[:,0],APOZ[:,1],c = 'cyan',s=150,marker = '.')
plt.scatter(1-MinWeight[:,0],MinWeight[:,1],c = 'red',s=150,marker = '.')
plt.scatter(1-Random[:,0],Random[:,1],c = 'magenta',s=150,marker = '.')
plt.scatter(1-ActMean[:,0],ActMean[:,1],c = 'green',s=150,marker = '.')
plt.scatter(1-ours[:,0],ours[:,1],c = 'blue',s=150,marker = '.')

plt.title("Parameters Vs Accuracy",fontsize=20,fontweight='bold')    #Ĭ�������СΪ12
plt.xlabel("Parameters",fontsize=20,fontweight='bold')
plt.ylabel("Accuracy,test set",fontsize=20,fontweight='bold')
plt.xlim(0.0,1.0)         #����x��ķ�Χ
plt.ylim(0.0,1.0)

plt.legend()          #��ʾ�����ߵ�ͼ��
plt.legend(loc=3,numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext,fontsize=20,fontweight='bold') #����ͼ������Ĵ�С�ʹ�ϸ

plt.show()
