import re

mystr="This is Python!"

x=re.match('This',mystr)
print(x)

if x: #true
    print("Match success!")
else:
    print("Error!, Not Match")
