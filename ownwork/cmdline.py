import time,sys
#a=[s for s in input().split()]
s=time.time()
#print(a)
for i in sys.argv:
    print(i)

print(time.time()-s)