import re

mystr="This is Python!"

#x=re.findall('Py..on',mystr)
#print(x)

x=re.findall('This|That',mystr)
print(x)