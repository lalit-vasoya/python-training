
# import threading
# import time
# a=time.time()
# def cube(no):
#     a=0
#     for i in range(1,no):
#         a+=i*i*i
#         print(i*i*i)

# def squre(no):
#     a=0
#     for j in range(1,no):
#         a+=j*j
#         print(j*j)

# t1=threading.Thread(target=cube,args=(10,))
# t2=threading.Thread(target=squre,args=(10,))

# t1.start()
# print(time.time()-a)
# t2.start()
# print(time.time()-a)
# cube(100)
# squre(100)
#print(time.time()-a)
def sum(no,func):
    tot=0
    for i in range(no):
        print(func(i))
    return tot

def squre(x):
    return x*x


#print(sum(3,squre))
from random import choice
def methonout(name):
    def method1():
        return name+choice(("lol","hahaha","hoore","yahoo","asas"))

    return method1()

a=methonout("method")
print(a)
print(a)
print(a)


