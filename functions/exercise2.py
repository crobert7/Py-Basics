def fun(x):
    x += 1
    return x

x = 2
x = fun(x + 1)
print(x)

# dic = { }
# ls = ['a', 'b', 'c','d']

# for i in range(len(ls) - 1):
#     dic[ls[i]] = (ls[i], )
# for i in sorted(dic.keys()):
#     k = dic[i]
#     print(k[0])

# def fun(a):
#     if a % 2 == 0:
#         return 1
#     else:
#         return

# print(fun(fun(2) + 1))

# def any():
#     print(var + 1, end = '')

# var = 1
# any()
# print(var)

# def f(x, y, z):
#     return  x + 2 * y + 3 * z

# print(f(0, z = 1, y = 3 ))

# tup = (1, 2, 3, 4)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

ls = [1, 2]

for v in range(2):
    ls.insert(-1, ls[v])

print(ls)

z = 10
y = 0
x = y < z and z > y or y > z and z < y

# ls = [x * x for x in range(5)]
# print(ls)
# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(ls))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else: 
#         return 2

# print(fun(fun(2)))

nums = [1,2,3]
vals = nums
del vals[:]
print(vals)

# x = 3
# y = 2

# x = x % y
# x = x % y
# y = y % x
# print(y)

# x = 1 // 5 + 1/ 5
# print(x)

# x = 2
# y = 4

# print( y ** (1/x))

# dic = {'1':'3', '3':'1', '2':'3'}
# v = dic['3']

# for k in range(len(dic)):
#     v = dic[v]

# print(v)

# lis = [i for i in range(-1, -2) ]
# print(len(lis))

# i = 0

# while i < +2:
#     i+=1
#     print('*')
# else:
#     print('*') 

tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

# d = {'1':'0', '0':'1'}
# for i in d.vals():
#     print(x, end='')

# d = { }

# d['1'] = (1,2)
# d['2'] = (2,1)

# for i in d.keys():
#     print(d[i][1], end='')

# ls = [[x for x in range(3)] for y in range(3)]

# for i in range(3):
#     for j in range(3):
#         if ls[i][j] % 2 != 0:
#             print('*')

# def fun(x,y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)

# print(fun(0,3))
