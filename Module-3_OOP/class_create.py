class student:
    stid=1
    stnm='Sanket'


    def getdata(self):
        print("This is student class.")


#Object of class
st=student()
print(st.stid)
print(st.stnm)
st.getdata()