# # #1)Reverse words in a given String in Python
# # #Input : str = “my name is laxmi”
# # #output : str= laxmi is name my
# s="my name is laxmi"
# # x=s.split()
# # print(x)
# # x=x[::-1]
# # l=[]
# # for i in x:
# #       l.append(i)
# #       a=" ".join(l)
# # print(a)
#
# # 2)Find Highest Frequency Character in a String
# #    ex:  x='Helloworld' #o/p l=3
#
# # 3)Print the Words Ending with Letter 'A'
# #     ex :x=Hello Rama NagA is Good RA   # o/p : NagA RA
# x='Hello Rama NagA is Good RA'

# x='Hello Rama NagA is Good RA'
# out=[]
# s=x.split()
# for i in s:
#     if i.endswith(('A')):
#         out.append(i)
# print(out)
# y=" ".join(out)
# print(y)
# #
# #
# # x="Amma is"
# # temp=x.reverse(x)
# # print(temp)
# str1 = 'w3resource'
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



x=[1,20,4,3,5]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)

