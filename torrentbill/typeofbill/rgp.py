from collections import OrderedDict
from .base import Base 

class Rgp(Base):
    """ RGP : Residential General Purpose """
    def __init__(self):
        """ Constructor of  RGP : Residential General Purpose """
        super(Rgp,self).__init__() # calling a __init__ method of base class
        self.cal_rgp() # calling a  method of sub class or same class

    def cal_rgp(self):# calling a  method of sub class or same class
        """ Calulation of RGP in This Method """
        subcat=(
            ("[1] Single Phase",25),
            ("[2] Three Phase",65),
            ("[0] Exit",0)
            )

        print(*map(lambda p:p[0],subcat),sep="\n") #Print on console option of the Phase
        print("==============================================="*3)
        
        choice=int(input("Enter Phase:"))

        if choice>=len(subcat) or choice<=0:
            print("Wrong Input")
            return
        
        cal=OrderedDict({50:320,150:390})
        if self.unit>200:
            cal[self.unit-150]=490
        self.calof1to3(cal,subcat[choice-1][1]) # calling a inherit method of base class
        return