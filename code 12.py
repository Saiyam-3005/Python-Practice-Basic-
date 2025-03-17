a1=eval(input('enter the first age:'))
a2=eval(input('enter the second age:'))
a3=eval(input('enter the third age:'))
old=a1
young=a1
if a1==a2==a3:
    print(a1,a2,a3,'all are of same age')
elif old<a2 :
    old=a2
elif young>a2:
    young=a2
if old<a3:
    old=a3
elif young>a3:
    young=a3
print(old,'is the oldest and',young,'is the youngest')
input()
