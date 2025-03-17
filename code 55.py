#15
import statistics
n=int(input("enter the total number of temperature :"))
d=list()
for i in range(0,n):
    p=int(input("enter the temperature:"))
    d.append(p)
print(d)
e=statistics.mean(d)
f=statistics.median(d)
print("the average tempeature of north india is :",e,"\n the median temperature of north india is :",f)
o=int(input("enter the value by which the tempeature is dipped :"))
for i in range(len(d)):
    d[i]-=o
print(d)
g=statistics.mean(d)
h=statistics.median(d)
print("the new average tempeature of north india is :",g,"\n the median of new temperature of north india is :",h)
