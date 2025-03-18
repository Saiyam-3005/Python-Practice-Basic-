"""	USER-DEFINED FUNCTION TO ACCEPT A STRING AS AN INPUT AND TO COUNT
AND DISPLAY THE TOTAL NUMBER OF VOWELS PRESENT IN IT"""
def count(str):
    c=0
    for r in str:
        if r in 'aeiouAEIOU':
           c+=1
    return c
i=input("enter any string:")
c=count(i)
print("total numbers of vowels present are:",c)
