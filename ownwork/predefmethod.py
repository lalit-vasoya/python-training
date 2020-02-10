class Base:
    base_a='hiii'

    def __get__(self,instance,owner):
        print(self.__class__.__name__)
        print(instance.__class__.__name__)
        print(owner.__name__)
        return f'{self.base_a} lalit'

class Derive:
    o=Base()
    derive_a=10

    def __get__(self,instance,owner):
        return self
    # def __getattribute__(self,name):
    # #     print("Hiii",name)
    #     return "dasd"

obj=Derive()
print(obj.o)