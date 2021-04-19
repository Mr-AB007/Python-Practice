class Student: # we can use the keyword class to create class in the python,␣

#name student
    def printDetails(self,name=None,age = None):# init function is used to assign␣

        if name != None and age !=None:
            print("your name is "+name)
            print("your age is %d"%(age))
        else:
            print("what is your name?")
obj1 = Student()

obj1.printDetails() # this is going to call the method without any␣ argument

obj1.printDetails("Anubhav",23) #same method called with argument
