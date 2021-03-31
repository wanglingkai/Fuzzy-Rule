import numpy as np
from matplotlib import pyplot as plt

def determinLarge(input):
    if input<0:
        return 0
    if input>=0 and input<0.4:
        return input/0.4
    if input>=0.4:
        return  1
def determinSmall(input):
    if input<-0.4:
        return 1
    if input>=-0.4 and input<0:
        return -input/0.4
    if input>=0:
        return  0
def determinMiddle(input):
    if input<-0.4:
        return 0
    if input>=-0.4 and input<0:
        return (input+0.4)/0.4
    if input>=0 and input<0.4:
        return  (0.4-input)/0.4
    if input>=0.4:
        return 0

def GraCal(gl,gs,hl,hs,hm,gm):
    rule1 = min(gs, hl)#If GSR is low And HR is high Then 場所 is high
    rule2 = min(gs, hm)#If GSR is low And HR is middle Then 場所 is middle
    rule3 = min(gm, hl)#If GSR is middle And HR is high Then 場所 is middle
    rule4 = min(gs, hs)#If GSR is low And HR is low Then 場所 is low
    rule5 = min(gm, hm)#If GSR is middle And HR is middle Then 場所 is low
    rule6 = min(gm, hs)#If GSR is middle And HR is low Then 場所 is low
    rule7 = min(gl, hl)#If GSR is high And HR is high Then 場所 is low
    rule8 = min(gl, hs)#If GSR is high And HR is low Then 場所 is low
    rule9 = min(gl, hm)#If GSR is high And HR is middle Then 場所 is low
    high=rule1
    middle=max(rule2,rule3)
    low=max(rule4,rule5,rule6,rule7,rule8,rule9)
    sumD=0
    sumU=0
    fx=[]
    x=[]
    for i in range(-10,11,1):
        if i>=-10 and i<-6:
            fx.append(min(low,(i+10)*0.25))
        if i>=-6 and i<=-4:
            fx.append(min(low,-(i+2)*0.25))
        if i==-3:
            fx.append(max(min(0.25,low),min(0.25,middle)))
        if i>=-2 and i<0:
            fx.append(min(middle,(i+4)*0.25))
        if i>=0 and i<=2:
            fx.append(min(middle,-(i-4)*0.25))
        if i==3:
            fx.append(max(min(0.25,middle),min(0.25,high)))
        if i>=4 and i<=6:
            fx.append(min(high,(i-2)*0.25))
        if i>6 and i<=10:
            fx.append(min(high,-(i-10)*0.25))
        x.append(i)
    for i in range(21):
        sumU=sumU+x[i]*fx[i]
        sumD=sumD+fx[i]
    return sumU/sumD/10
GL=[]#GSR大きい
GS=[]#GSR小さい
GM=[]#GSRMiddle
HL=[]#HR大きい
HM=[]#HRMiddle
Gra=[]#重心
HS=[]#HR小さい
GSR=[]
with open("GSR.csv") as read_object:
    lines=read_object.readlines()
for line in lines:
    GSR.append(float(line.rstrip()))
HR=[]
with open("HR.csv") as read_object:
    lines=read_object.readlines()
for line in lines:
    HR.append(float(line.rstrip()))
#GSRdif=[]
#for i in range(len(GSR)-1):
#    #print(i)
#    GSRdif.append(GSR[i+1]-GSR[i])
#    GSRdif[i] = GSRdif[i] * 100
#    if GSRdif[i]<0:
#        GSRdif[i]=-GSRdif[i]
    #print(GSRdif[i])
#HRdif=[]
#for i in range(len(HR)-1):
#    #print(i)
#    HRdif.append(HR[i+1]-HR[i])
#    HRdif[i] = HRdif[i] * 100
#    if HRdif[i]<0:
#        HRdif[i]=-HRdif[i]
    #print(HRdif[i])
for i in range(len(HR)):
    GL.append(determinLarge(GSR[i]))
    GS.append(determinSmall(GSR[i]))
    HL.append(determinLarge(HR[i]))
    HS.append(determinSmall(HR[i]))
    HM.append(determinMiddle(HR[i]))
    GM.append(determinMiddle(GSR[i]))
    Gra.append(GraCal(GL[i],GS[i],HL[i],HS[i],HM[i],GM[i]))
    print(i)
    print(Gra[i])

x = range(len(Gra))
y = Gra
#z = HRdif
plt.plot(x,y)
plt.title("Excitement level")
plt.xlabel("Time(in seconds)")
plt.ylabel("Output variable")
plt.annotate(' ', xy=(372,-0.1), xytext=(372,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(126,-0.1), xytext=(126,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(587,-0.1), xytext=(587,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(798,-0.1), xytext=(798,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(902,-0.1), xytext=(902,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(977,-0.1), xytext=(977,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(1656,-0.1), xytext=(1656,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.annotate(' ', xy=(1811,-0.1), xytext=(1811,0.1),arrowprops=dict(width=0.5,headwidth=0.5,headlength=0.5,facecolor='black', shrink=0.05))
plt.show()

