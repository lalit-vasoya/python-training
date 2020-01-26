import time,sys
#a=[s for s in input().split()]
s=time.time()
#print(a)
for i in sys.argv:
    print(i)

print(time.time()-s)

# def abc(no1):
#     def xyz(no2):
#         return no1+no2
#     return xyz

# print(abc(10)(20))