'''24.	TO INPUT ELEMENTS IN A TUPLE AND PASS IT TO A FUNCTION TO DETERMINE
THE TOTAL NUMBER OF EVEN AND ODD NUMBERS IN IT'''
def count(tup):
    even=0
    odd=0
    for i in tup:
        if i%2==0:
            even +=1
        else:
            odd +=1
    return even,odd
tup1=()
n=int(input("enter the total no. of elements in a tuple:"))
for i in range(0,n):
    num=int(input("enter the number:"))
    tup1=tup1+(num,)
c=count(tup1)
print("even numbers are:",c[0])
print("odd numbers are:",c[1])
