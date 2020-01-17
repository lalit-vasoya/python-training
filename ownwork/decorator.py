def main(func):
     def wrap():
             print("Hello Welcome")
             func()
             print("bye")
     return wrap
 

@main
def abc():
     print("Lalit")
b=main(abc)
b()