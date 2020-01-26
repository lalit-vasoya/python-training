from collections import OrderedDict
from .base import Base 

class Glp(Base):
    """ GLP : General Lighting Purpose """
    def __init__(self):
        """ Constructor of  GLP : General Lighting Purpose """
        super(Glp,self).__init__()
        self.cal_Glp()

    def cal_Glp(self):
        """ Calulation of GLP in This Method """
        subcat=(
            ("[1] Single Phase",30),
            ("[2] Three Phase",70),
            ("[0] Exit",0)
            )

        print(*map(lambda p:p[0],subcat),sep="\n")
        print("==============================================="*3)
        
        choice=int(input("Enter Phase:"))

        if choice>=len(subcat) or choice<=0:
            print("Wrong Input")
            return
        
        cal=OrderedDict({200:410})
        if self.unit>200:cal[self.unit-200]=480   
        self.calof1to3(cal,subcat[choice-1][1])


    def calof1to3(self, cal, phase):
        """ Calling a Base Class Calculation Method """
        return super().calof1to3(cal, phase)
