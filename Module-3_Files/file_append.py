fl=open('test.txt',"a")
#fl=open('hello.docx',"w")

id=input("Enter ID:")
name=input("Enter Name:")
city=input("Enter City:")

fl.write(f"ID:{id}\nName:{name}\nCity:{city}\n")