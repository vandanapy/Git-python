#1) wa function to check wheather num is prime or not
def checkPrime(x):
    for i in range(2, x):
        if n%i==0:
            return 1
n = int(input("enter a num  "))
p = checkPrime(n)
if p==1:
    print( n," is not a Prime Number")
else:
    print(n ," is a Prime Number")


#2) types of all functions with example
a.function without argument and without return value
def add():
    a=10
    b=20
    print (a+b)
add()

b.function with argument and without return value
def add(a,b):
    print(a+b)
add(30, 20)

c.function without argument and with return value
def add():
    a=10
    b=20
    return a+b
c=add()
print(c)

d.function with argument and with return value
def add(a,b):
  return a+b
c=add(10,20)
print(c)

#3) x={'A:100,'B':200}    # op {100:'A',200:'B'}
x={'A':100,'B':200}
a=list(x.keys())
b=list(x.values())
z=list(zip(b,a))
print(dict(z))



#5) x=[1,2,3,5] -> add 10 to each element in list use lambda fun
X=[1,2,3,5]
Y=lambda i:i+10
z=[]
for i in X:
  z.append(Y(i))
print(z)

#6) what is filter ,reduce map with syntax and example
MAP:-applies a function to all the items in an input_list.and it will modify the elememt and returns new element
  syntax:- variable_name=map(fun,sequence)

Filter:-it wil take 2 args one is fun nnd list  it wil fiter the perticuler elements
        synatx : var_name=list(filter(fun,iterable_obj))

Reduce:- This fun will reduce the sequnce of elements into a single eleMENT by applying specified fun
         # syntax : reduce(fun name ,sequnce)
# if we want to use reduce we have to import the module called functools


#7) wa function x=[[1,2,3],[4,5,6],[1,2,3]] remove duplicate list from list
x=[[1,2,3],[4,5,6],[1,2,3]]
# z=[]
# for i in x:
#     if i not in z:
#         z.append(i)
# print(z)

y = list(set(map(lambda i: tuple(sorted(i)),x)))
print(y)
























