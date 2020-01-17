from time import time
from functools import wraps

def test_speed(func):
    @wraps(func)
    def wrap(*args,**kargs):

        start_time=time()
        r=func(*args,**kargs)
        end_time=time()
        print("Time Elapse:",(end_time-start_time))
        return r    
    return wrap

@test_speed
def use_gen():
    print(sum(i for i in range(100000000)))

@test_speed
def use_list():
    print(sum(i for i in range(100000000)))

use_gen()

use_list()