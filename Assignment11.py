# # # ass1 remove the duplicate ele in the list without using set and by using set
x=[1,2,3,4,1,2,5,6]
# # x=set(x)  ==>using set
# # print(list(x)) ==> o/p [1, 2, 3, 4, 5, 6]
# y=list(dict.fromkeys(x))  ==>using form keys
# # print(y)
y=[]
for i in x:
    if i not in y:    ====> using membership
        y.append(i)
print(y)

#  Ass 3 : sort the list without sort function  # use any sorting logic
x=[1,20,4,3,5]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)

# print only even numbers using list comphreension
x=[1,3,2,4,5,7,6,8] # output -> [2,4,6,8]  -
evenno = [num for num in x if num % 2 == 0]
print("Even numbers : ", evenno)





# ass2 -> count the each ele how many times it is exits ->
x=[1,2,3,4,1,2,5,6]
counts = {}
for i in x:
    counts[i] =counts.get(i, 1) + 1
print(list(counts))
