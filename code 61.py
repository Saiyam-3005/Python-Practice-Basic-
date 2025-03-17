num=int(input("enter the number of countries whose data is to be entered: "))
count=1
world=dict()
for count in range(0,num):
    name=str(input("enter the name of the country: "))
    i=str(input("enter the name of their capital: "))
    c=str(input("enter the currency of that country: "))
    b=i,c
    world[name]=b
print(world)
print("\n")
print("COUNTRY_NAME\tCAPITAL_NAME\tCURRENCY")
for k in world:
    print(k,end="\t\t")
    z=world[k]
    for j in z :
        print(j,end="\t\t")
    print(end="\n")   
print("\n")
find=str(input("enter the name of the country to be fined: "))
for i in world:
 if i==find:
      print("name of the country: ",name ,"\n name of Capital and currency is: ",world[i])


