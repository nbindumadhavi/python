# str - collection of characters enclosed with double or single and triple single or triple double quotes
s = "python"
print(s, type(s))

str = '123@$&nbm'
print(str, type(str))

c = """ bindu
    madhavi"""
print(c,type(c))

a = ''' bindu
    nalluri'''
print(a,type(a))

#operations on string
#1 indexing - str[index]
s = "python"
print(s)
print(s[0])
print(s[-6])
print(s[len(s) - 1])
print(s[True])
print(s[False])

#2 slicing - 1. strobj[BEGIN : END]
s = "python"
print(s)
print(s[0:3])
print(s[6:1]) # not give op cause "begin index < end index"
print(s[-6:-1])
#2 slicing - 2. strobj[BEGIN : ] if not specifying end index then pvm takes end index as len(strobj)
s = "python"
print(s)
print(s[1:])
print(s[-6:])
print(s[5:])
#2 slicing - 3. strobj[ : END] if not specifying begin index then pvm takes begin index as 0 (or) -len(strobj)
s = "python"
print(s)
print(s[:-1])
print(s[:5])
print(s[:1])
#2 slicing - 4. strobj[ : ] if not specify the begin and end indexes then pvm takes entire strobj data
s = "python"
print(s[ : ])
#2 slicing - 5. strobj[BEGIN : END : STEP]
# 1. begin, end and step either +ve or -ve
s = "python"
print(s[-6 : -2 : 1])
# 2. if step is +ve then it takes begin to end-1 and should begin < end otherwise get '  '
print(s[-6 : 5 : 3])
print(s[0 : -2 : 2])
print(s[ : :1])
# 3. if step is -ve then it takes begin to end+1 and should begin > end otherwise get '  '
s="python"
print(s[4 : 2 :-1])
print(s[ : :-1])
# 4. if end index as 0, step is +ve then we get '  '
s="python"
print(s[5: 0 :1])
print(s[1 : 0 :1])
# 5. if end index as -ve, step is also -ve then we get '  '
s="python"
print(s[5: -1 :-1])
print(s[ : -5 :-1])

# predefined functions in string
# 1.capitalize - strobj.capitalize()
s = "python"
print(s)
print(s.capitalize())
a = "bindu"
print(a)
b = a.capitalize()
print(b)

# 2. title() - strobj.title()
s = "python language"
print(s)
print(s.title())
a = "bindu nalluri"
print(a)
b = a.title()
print(b)

# 3. index() - strobj.index(value)
s = "python"
print(s.index('n'))
a = s.index('y')
print(a)

# 4. upper() - strobj.upper()
s = "python"
print(s.upper())
a = s.upper()
print(a)

# 5. lower() - strobj.lower()
s = "PythOn"
print(s.lower())
a = s.lower()
print(a)

# 6. isupper() - strobj.isupper()
s = "PYTHON"
print(s.isupper())
a = s.isupper()
print(a)

# 7. islower() - strobj.islower()
s = "python"
print(s.islower())
a = s.islower()
print(a)

# 8. isalpha() - strobj.isalpha()
s = "python"
print(s.isalpha())
a = s.isalpha()
print(a)

# 9. isdigit() - strobj.isdigit()
s = '234'
print(s.isdigit())
a = s.isdigit()
print(a)

# 10. isalphanum() - strobj.isalphanum()
s = 'python3' # python 3 OR python3.12 -error
print(s.isalnum())
a = s.isalnum()
print(a)

# 11. isspace() - strobj.isspace()
s = ' '
print(s.isspace())
a = s.isspace()
print(a)

# 12. split() - strobj.split()
s = 'python is a language'
print(s,type(s))
print(s.split(),type(s))
a = s.split()
print(a,type(a))

s = 'python3.12'
b = s.split('.')
print(b,type(b))

# 13. join() - strobj.join(iterable obj)
lst = ['python','is','a','language']
print(lst,type(lst))
a = '-'
print(a.join(lst))

lst = ['python','is','a','language']
print(lst,type(lst))
a = ' '
print(a.join(lst))

# 14. startswith() - strobj.startswith(value)
s = 'python is a language'
print(s.startswith('python'))
print(s.startswith('Python')) #false

# 15. endswith() - strobj.endswith(value)
s = 'python is a language'
print(s.endswith('language'))
print(s.endswith('Language')) #false

# 16. swapcase() - strobj.swapcase()
s = 'PytHoN'
print(s.swapcase())
a=s.swapcase()
print(a)