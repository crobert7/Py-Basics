# class A:
#     def __init__(self, v):
#         self.__a = v + 1

# a = A(0)
# print(a.__a)

# class A:
#     def __init__(self , v = 1):
#         self.v = v

#     def set(self, v):
#         self.v = v
#         return v

# a = A()
# print(a.set(a.v + 1))

# class A:
#     X = 0

#     def __init__(self, v = 0):
#         self.Y = v
#         A.X += v

# a = A()
# print(a.X)
# b = A(1)
# print(b.X)
# c = A(2)
# print(c.X)

# class A:
#     A = 1

# print(hasattr(A, 'A'))

# class A:
#     def __init__(self):
#         pass

# a = A(1)
# print(hasattr(a, 'A'))

# class A:
#     def __str__(self):
#         return 'a'

# class B(A):
#     def __str__(self):
#         return 'b'

# class C(B):
#     pass

# o = C()
# print(o)

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

# print(issubclass(C, A))


# class A:
#     def a(self):
#         print('a')

# class B:
#     def a(self):
#         print('b')

# class C(B, A):
#     def c(self):
#         self.a()

# o = C()
# o.c()

# class A:
#     def __str__(self):
#         return 'a'

# class B(A):
#     def __str__(self):
#         return 'b'

# class C(B):
#     pass

# o = C()
# print(o)


# class A:
#     v = 2

# class B(A):
#     v = 1

# class C(B):
#     pass

# o = C()
# print(o.v)


# def f(x):
#     try:
#         x = x / x
#     except:
#         print('a', end = '')
#     else:
#         print('b', end = '')
#     finally:
#         print('c', end = '')

# f(1)
# f(0)

# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))

# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self, msg + msg)
#         self.args = msg

# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v

# for i in I():
#     print(i, end='')


# def I():
#     s = 'abcdef'
#     for c in s[::2]:
#         yield c

# for i in I():
#     print(i, end='')


# def I(n):
#     s = '+'
#     for c in range(n):
#         s += s
#         yield s

# for i in I(2):
#     print(i, end='')

# def p(o):
#     def q():
#         return '*' * o
#     return q

# r = p(1)
# s = p(2)

# print(r() + s())

# import math
# print(dir(math))
# print(__name__)

# try:
#     raise Exception
# except:
#     print('c')
# except BaseException:
#     print('a')
# except Exception:
#     print('b')

# x = '\'
# print(len(x))
# x = """
# """
# print(len(x))

# class A:
#     A = 1
#     def __init__(self):
#         self.a = 0

# print(hasattr())

# class A:
#     pass

# class B:
#     pass

# class C(A,B):
#     pass

# print(issubclass(C,A) and issubclass(C,B))

def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s

for x in I(3):
    print(x, end='')