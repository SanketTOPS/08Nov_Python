import re

mystr="This is Python!"

x=re.search('Python',mystr)
print(x)

if x: #true
    print("Match success!")
else:
    print("Error!, Not Match")
