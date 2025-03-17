print("-------------CALCULATOR----------------")
print("1.SUM")
print("2.DIFFERENCE")
print("3.PRODUCT")
print("4.DIVISION")
print("5.INTEGER DIVISION")
print("6.SQUARE ROOT")
print("7.SQUARE")
print("0.EXIT")
while(True):
        n=int(input("ENTER THE index of number to perform: "))
        if n in  range(1,6):
                a=float(input('enter the first number:'))
                b=float(input('enter the second number:'))
        elif n in range(6,8):
                a=float(input('enter the number:'))
        match n:
                case 1 :
                        print("result = ",a+b)
                case 2 :
                        print("result = ",a-b)
                case 3 :
                        print("result = ",a*b)
                case 4 :
                        print("result = ",a/b)
                case 5 :
                        print("result = ",a//b)
                case 6 :
                        print("result = ",a**0.5)
                case 7 :
                        print("result = ",a**2)
                case 0 :
                        print("THANK YOU")
                        break
               