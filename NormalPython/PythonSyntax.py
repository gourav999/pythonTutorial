#koi bhi python class exeucte karne ke liye terminal par folder tak navigare karo and write the comand python file name.py

#Indentation refers to the spaces at the beginning of a code line.

#Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

#Python uses indentation to indicate a block of code.

#for print something
print("GOurav jain is greate")
########################################################
#if loops
if (5>2):
    print("5 is greate than 2")
else:
    print("5 is less than 2")

if (1>2):
    print("1 is greate than 2")
else:
    print("1 is less than 2")
####################################################################################
 #python variables
x = 5
y = "Hello, World!"
z= "Gourav"
print (x,",",y,z)
   #if we declard like this z='gourav' or z="gourav" both are same.

#casting
castofX=str(3)
print (f"THis is x value {castofX}" )
castofy=int(3)
print (f"THis is y value {castofy}" )
castofz=float(3)
print (f"THis is z value {castofz}" )

print (type(castofz))

z1='gourav'
z11="gourav"
print(z1)
print(z11)
    #variable are case sensitive
a=4
A="anubha"
print(a)
print(A)

myvar="Gourav"
my_var="Gourav"
_my_var="Gourav"
myVar="Gourav"
MYVRA="gOURAV"
myvar2="gourav"

#camelcase
myVariableName="gourav"
MyVariableName="Gouravs"
my_variable_name="Gourav"

x,y,z="organe","banana", "apple"
print(x,y,z)

#one value to multiple variables.
Sourabh=Gourav=Anita="gourav"
print("sourabh's value==>"+Sourabh);print("Gourav's value==>"+Gourav); print("Anita's value==>"+Anita)

#unpacking the values
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x);print(y); print(z)

#python output variable
x="Gourav jain is greate"
print("Python is "+x) 
print(x)  #python is awesome

#copilot please write sum of two number in python   
x=5
y=6
print(x+y)

# #please write code for reading the excel file in python
# import pandas as pd

# df=pd.read_excel("C:/Users/gourav.b.jain/Downloads/Priority.xlsx")
# print(df)

#multiple variables seperated by comma
x,y,z="orange","banana","apple"
print(x,y,z)

#multiple variables seperated by comma
x,y,z="orange","banana     ","apple"
print(x+y+z)

x="awesome"
y=5
#print(y+x)/why this is not working /TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(y)+x)


#Global variable
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.k
x1="awesome"
def myfunc():
    print("Python is ==============>"+x1)
myfunc()

#create a variable inside a function, with the same name as the global variable
#in this case the function will print the local x, and then the code will print the global x
#if you use the same variable name inside and outside of a function, Python will treat them as two separate variables.
x2="gourav" 
def myfunc():
    x2="fantastic"
    print("Python is ==============>"+x2)
myfunc()

#global keyword
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.
#if you use the global keyword, the variable belongs to the global scope
x1="dummy value"
def myfunc():
    global x1
    x1="The future "
myfunc()
print("Python is ==============>"+x1)

#very good example. my func call hone ke bad print lagaya hai. awesome print hoga
x = 'awesone'  

def myfunc():  
    x = 'fantastic'  
    myfunc()  

print('python is ' + x)  
