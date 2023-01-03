import re

mystr="This is Python!656596"

#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
#x=re.findall('.$',mystr)
x=re.findall('96$',mystr)
print(x)