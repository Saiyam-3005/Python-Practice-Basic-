str1=input("enter the string :")
str2=""
for i in range(len(str1)):
    if str1[i] not in "aeiouAEIOU":
        str2+=str1[i]
print("original string is :",str1)
print("edited string is :",str2) 
    
            
              
    
            
    
