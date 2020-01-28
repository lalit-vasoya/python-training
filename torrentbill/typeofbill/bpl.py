from collections import OrderedDict
from .base import Base 

class Bpl(Base):
    """ BPL : Below Poverty Line """
    def __init__(self):
        """ Constructor of  BPL : Below Poverty Line """
        super(Bpl,self).__init__() # calling a __init__ method of base class
        self.cal_bpl() # calling a  method of sub class or same class

    def cal_bpl(self):
        print("==============================================="*3)
        cal=OrderedDict({30:150,20:320,150:390})
        if self.unit>200: 
            cal[self.unit-150]=490   

        self.calof1to3(cal,5) # calling a inherit method of base class
        return
