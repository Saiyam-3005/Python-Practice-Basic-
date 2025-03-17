num=int(input("enter the number of student whose data is to be entered: "))
count=1
mark=dict()
for count in range(num):
    name=str(input("enter the name of the student: "))
    ut=int(input("enter the ut mark of student from 30: "))
    ut2=int(input("enter the ut2 mark of student from 30: "))
    half=int(input("enter the half yearly mark of student from 80: "))
    final=int(input("enter the final mark of student from 80: "))
    b=ut,ut2,half,final
    mark[name]=b
print(mark)
print("\n")
print("\n\STUDENT_NAME\tUT-1\t\tUT-2\t\tMID TERM\tANNUAL TERM")
for k in mark:
    print(k,end="\t\t")
    z=mark[k]
    for j in z :
        print(j,end="\t\t")
        
find=str(input("enter the name of the student whose name is to be fined: "))
for i in mark:
    if i==find:
        print("name of the student: ",i,"\nmarks of the students: ",mark[i])
        list1=list(mark[i])
        p=sum(list1)
        perc=p*100/220
        print("percentage of the student is: ",perc)
        if perc>=80:
            print('your grade is:A')
        elif 60<=perc<80 :
            print('your grade is:B')
        elif 50<=perc<60 :
            print('your grade is:C')
        elif 45<=perc<50 :
            print('your grade is:D')
        elif 25<=perc<45 :
            print('your grade is:E')
        else :
            print('your grade is:F')

            


        



        

