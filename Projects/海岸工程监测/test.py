
from cmath import pi, tan


i = 0
while i < 13:
    if i == 0:
        L = 9.81*100/2/pi
    else:
        L = (9.81*100/2/pi)*tan(10)*2*pi*10/L
    print(i,L)
    i+=1
kk = (9.81*100/2/pi)*tan(10)*2*pi*10/156.2
print(kk)