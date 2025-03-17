num=int(input("enter the number of friends : "))
count=1
phone=dict()
for count in range(num):
    name=input("enter the name of the friend : ")
    number=int(input("enter the phone number of your friend: "))
    phone[name]=number
print(phone)
print("\nNAME OF FRIEND\tPHONE NUMBER")
for k in phone:
    print(k,"\t\t",phone[k])
j=int(input("enter the number of friends whose data is to be added: "))
for i in range(0,j):
    s=str(input("enter the name of the friend whose number is to be added :"))
    w=int(input("enter hi phone number :"))
    phone[s]=w
print(phone)
print("\nNAME OF FRIEND\tPHONE NUMBER")
for k in phone:
    print(k,"\t\t",phone[k])
