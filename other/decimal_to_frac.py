#coding:utf-8
from decimal import *
getcontext().prec=100
x=Decimal(3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706)

N=10**6 
score = x**2
top=None
for i in range(1,N):
    for j in range(int(i*x)-2,int(i*x)+2):
        p=Decimal(j)/Decimal(i)
        e=(p-x)*(p-x) 
        if score >  e:
            top=(j,i)
            score = e
            print top
            
print "optimum num:",top,e


