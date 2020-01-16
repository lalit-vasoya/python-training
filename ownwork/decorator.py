def main(func,a):
     def wrap(a):
             print("Hello Welcome")
             func(a)
             print("bye")
     return wrap
 
@main
def abc(no=10):
     print("Lalit",no)
