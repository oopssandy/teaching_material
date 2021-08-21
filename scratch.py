from urllib.parse import parse_qs
from copy import copy
# my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
# print(my_values)
# print(my_values['a'] if 'a' in my_values else 'Empty')
# my_str="0123456789"
# my_str=[0,1,2,3,4,5,6,7,8,9]
# if ((my_str := my_values.get('red',[chr(33)])[0])>'4'):
#     print('yes')
# else:
#     print('no')
# for i in my_str[::-1]:
#     print(i)
# class my_obj():
#     def __getitem__(self, index):
#         print(index)
#         print(index.indices(10))
# m = my_obj()
# m[1:2:3]
# a=[chr(a+33) for a in range(10)]
# for idx, value in enumerate(a):
#     print("index:", idx,"value:", value)
# b = [[b] for b in range(10)]
# c = [copy(B) for B in b]
# print("b",b)
# print("c",c)
# c[0][0]=100
# print("b",b)
# print("c",c)
# dst = "B"
# srcEdges = {"C":2,"B":3,"D":10}
# print(srcEdges)
# print(len(srcEdges))
# del srcEdges[dst]
# print(srcEdges)
# print(len(srcEdges))
a=[1,2,3,4]
while(a):
    print(a.pop(0))