num=int(input("enter the number of customers whose data is to be entered: "))
count=1
shop=dict()
for count in range(num):
    name=str(input("enter the name of the customer: "))
    i=str(input("enter the name of the product bought: "))
    c=int(input("enter the cost of the product: "))
    p=int(input("enter the phone number of the customer: "))
    b=i,c,p
    shop[name]=b
print(shop)
print("\n")
print("CUSTOMER_NAME\tPRODUCT_NAME\tCOST\tPHONE_NUMBER")
for k in shop:
    print(k,end="\t\t")
    z=shop[k]
    for j in z :
        print(j,end="\t\t")
    print(end="\n")    
