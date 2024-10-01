#converting one type value into another type value
#1. int() - varname=int(float/bool/str-int--possible and complex/str(float,bool,str,complex)-not possible)
a = 1.2
print(a,type(a))
b = int(a)
print(b,type(b))

a = True
print(a,type(a))
b = int(a)
print(b,type(b))

# a = 12 + 3j
# print(a,type(a))
# b = int(a)
# print(b,type(b))

a = '12'
print(a,type(a))
b = int(a)
print(b,type(b))

# a = '1.2'
# print(a,type(a))
# b = int(a)
# print(b,type(b))

# a = '1 + 2j'
# print(a,type(a))
# b = int(a)
# print(b,type(b))

# a = 'True'
# print(a,type(a))
# b = int(a)
# print(b,type(b))

# a = 'python'
# print(a,type(a))
# b = int(a)
# print(b,type(b))

#2. float() - varname=float(int/bool/str-int,float--possible and complex/str(bool,complex,str)-not possible)
a = 12
print(a,type(a))
b = float(a)
print(b,type(b))

a = True
print(a,type(a))
b = float(a)
print(b,type(b))

a = '12'
print(a,type(a))
b = float(a)
print(b,type(b))


a = '1.2'
print(a,type(a))
b = float(a)
print(b,type(b))

# 3. bool() - varname=bool(int/float/complex/str(int,float,complex,str)--possible
a = 12
print(a,type(a))
b = bool(a)
print(b,type(b))

a = 1.2
print(a,type(a))
b = bool(a)
print(b,type(b))

a = 1 + 2j
print(a,type(a))
b = bool(a)
print(b,type(b))

a = '12'
print(a,type(a))
b = bool(a)
print(b,type(b))

a = '1.2'
print(a,type(a))
b = bool(a)
print(b,type(b))

a = '1 + 2j'
print(a,type(a))
b = bool(a)
print(b,type(b))

a = 'python'
print(a,type(a))
b = bool(a)
print(b,type(b))

# 4. complex() - varname=complex(int/float/bool/str(int,float)--possible and str(bool,str)--not possible
a = 12
print(a,type(a))
b = complex(a)
print(b,type(b))

a = 1.2
print(a,type(a))
b = complex(a)
print(b,type(b))

a = True
print(a,type(a))
b = complex(a)
print(b,type(b))

a = '12'
print(a,type(a))
b = complex(a)
print(b,type(b))


a = '1.2'
print(a,type(a))
b = complex(a)
print(b,type(b))

# 5. str() - varname=str(int/float/bool/complex)--possible
a = 12
print(a,type(a))
b = str(a)
print(b,type(b))

a = 1.2
print(a,type(a))
b = str(a)
print(b,type(b))

a = True
print(a,type(a))
b = str(a)
print(b,type(b))

a = 1 + 2j
print(a,type(a))
b = str(a)
print(b,type(b))