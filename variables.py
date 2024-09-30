## global variable
# x="awesome"
# def myfunc():
#     print("python is " + x)
# myfunc()

#global key word
def myfunc():
    global x
    x="fentastic"
    print("python is " + x)
myfunc()

# local and global variable
x="awesome" #global variable
def myfunc():
    x="fentastic" #local variable
    print("python is " + x)
myfunc()
print("python is " + x)

