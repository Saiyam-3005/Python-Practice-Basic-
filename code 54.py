#16
import statistics
n=int(input("enter the total number of people who donated :"))
donations=list()
for i in range(0,n):
    p=int(input("enter the amount donated :"))
    donations.append(p)
print(donations)
d=statistics.mean(donations)
e=statistics.median(donations)
print("the average amount of the total donation is :",d)
print("the median of the total donation is :",e)
