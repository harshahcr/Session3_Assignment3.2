#3.1.a -list comprehensions
input = str('ACADGILD')
stringlist = list(input)
print('Implemented List comprehensions to produce the following lists. :')
print(stringlist)

#3.1.b - list comprehensions
val = list('xyz')
temp=''
lis1=[]
for j in val:
    for i in range(4):
        for k in range(0,i+1):
            temp=temp+j
        lis1.append(temp)
        temp=''
print(lis1)

#3.1.c - list comprehensions
var = list('xyz')
temp = ''
lis2 = []
for i in range(4):
    for j in var:
        for k in range(0,i+1):
            temp=temp+j
        lis2.append(temp)
        temp = ''
print(lis2)

#3.1.d - list comprehensions
lis4 = []
temp = 0
m=2
n=5
lis3=[]
for x in range(3):
    for i in range(m+x,n+x):
        temp=temp+i
        lis3.append(temp)
        lis4.append(lis3)
        lis3=[]
        temp=0
print(lis4)

#3.1.e - list comprehensions
temp=0
lis5=[]
lis6=[]
m=2;n=6  
for i in range(4):
    for j in range(m+i,n+i):
        temp=temp+j
        lis5.append(temp)
        temp=0
    lis6.append(lis5)
    lis5=[]
print(lis6)

#3.1.f - list comprehensions
x=[1,2,3]
tup = []
for i in x:
    for j in x:
        tup.append((j,i))
print(tup)




