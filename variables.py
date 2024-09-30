# # assign values to multiple variables in one line
a , b , c = "apple" , "banana" , "orange"
print(a)
print(b)
print(c)

# same value to multiple variables in one line
a = b = c = "apple"
print(a)
print(b)
print(c)

# In the print() function, you output multiple variables, separated by a comma
x = "bindu "
y= "madhavi "
z= "nalluri"
print(x,y,z)
#  OR using concatenate operator " + "
print( x + y + z)

x = 2
y = 3
print( x + y)

x = 2
y = "bindu"
print( x + y) #Error

# global variable
x="awesome"
def myfunc():
    print("python is " + x)
myfunc()

# global keyword
x="awesome"
def myfunc():
    global x
    x="fentastic"
myfunc()
print("python is " + x)

# local and global variable
x="awesome" #global variable
def myfunc():
    x="fentastic" #local variable
    print("python is " + x)
myfunc()
print("python is " + x)

