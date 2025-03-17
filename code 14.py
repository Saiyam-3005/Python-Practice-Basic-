amt= eval(input('enter your amount:'))
SI=0
if 500<=amt<2000:
    print('your rate of interest is :12')
    r=12
    t=eval(input('time in years:'))
elif 2000<=amt<5000:
    print('your rate of interest is :15')
    r=15
    t=eval(input('time in years:'))
elif amt>=5000:
    print('your rate of interest is :16')
    r=16
    t=eval(input('time in years:'))
if amt<500:
    print('your rate of interest is :RS 50')
    t=eval(input('time in years:'))
    SI=(amt+50)*t
else:
    SI=(amt*r*t)/100
print('your simple interest is:',SI)
input()
