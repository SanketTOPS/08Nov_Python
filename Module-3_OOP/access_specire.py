class student:
    __stid=12
    __stnm='Ashok'

    def __getdata(self):
        print("STudent ID:",self.__stid)
        print("Student Name:",self.__stnm)
    
    def printdata(self):
        self.__getdata()


st=student()
#print(st.stid)
#print(st.stnm)
#st.getdata()
st.printdata()