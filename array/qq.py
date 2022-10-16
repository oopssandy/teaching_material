# def firstDuplicate(a):
#     c=[]
#     for i in a:
#         if a.count(i)==1:
#             c.append(i)
#         if a.count(i)>1:
#             y=a.index(i)
#             a.pop(y)
#             r=a.index(i)
#             return r+1
#             break
#     if len(c) == len(a):
#         return -1

# x=[1,1,1,2,2,3]
# c=[]
# for i in x:
#     a=x.count(i)
#     c.append(a)
# max_count = max(c)
# y=c.index(max_count)
# print(x[y]*max_count)

a = [11, 22, 33]
b = [2, 1, 0]
# -> [33,22,11];
c = []
for i in b:
    aa = a[i]
    c.append(aa)
print(c)

#     seat_c=i
#     for ver in a:
#         # print(c.insert[seat_c,ver])
#         print(seat_c,ver)
