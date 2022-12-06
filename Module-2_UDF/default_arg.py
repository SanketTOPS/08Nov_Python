def getdata(id,name,sub='Python',city="Rajkot"): #default argument
    print("Student ID:",id)
    print("Student Name:",name)
    print("Student Subject:",sub)
    print("City:",city)

#getdata(101,'Snaket')
#getdata(12,'Sanket','PHP')
#getdata(1,'Nirav','JAVA','Ahmedabad') #positional argumnet

#getdata(id=1,name='Nirav',sub='JAVA') #keyword argument

getdata(sub='PHP',id=12,name="Sanket")