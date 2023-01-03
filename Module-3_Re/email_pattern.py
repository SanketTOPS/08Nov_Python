import re


#sanket2020@gmail.com
email=input("Enter an email:")

email_ptrn="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"


x=re.findall(email_ptrn,email)

if x:
    print("Valid Email!")
else:
    print("Error!Invalid Email")