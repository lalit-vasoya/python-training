
from functools import wraps
def shout(func):
    @wraps(func)
    def wrap(*args,**kargs):
        """ Hello we are in wrapper function"""
        print("Welcome",func.__name__)
        print(*args)
        func(*args,**kargs)
        print("Exit")
    return wrap

@shout
def abc(no1,no2):
    """ we are in abc function"""
    print("Sum Of Number is:",(no1+no2))

@shout
def xyz():
    """ we are in xyz function"""
    print("Just no pass any argument")

#abc(10,no2=20)
#xyz()
#print(help(xyz))
print(abc.__doc__)
print(xyz.__doc__)