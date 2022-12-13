fl=open('test.txt',"w")

id=input("Enter ID:")
name=input("Enter Name:")
city=input("Enter City:")

fl.write(f"ID:{id}\nName:{name}\nCity:{city}\n")