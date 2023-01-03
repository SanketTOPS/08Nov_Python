import re

unm=input("Enter Username:")

unm_ptrn="[A-Z]+[a-z]+[0-9]+[.@!$]" #pattern

x=re.findall(unm_ptrn,unm)
#print(x)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username")