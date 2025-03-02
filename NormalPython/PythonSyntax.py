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
x=y=z="gourav"
print(x);print(y); print(z)

#unpacking the values
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x);print(y); print(z)