fl=open("test.txt","r+")

print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[5])

fl.write("\nHello Students!")

fl.close()


"""n=1
for i in fl:
    #print(i)
    print(f"Line:{n} = {i}")
    n+=1"""