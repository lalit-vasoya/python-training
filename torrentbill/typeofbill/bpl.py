from collections import OrderedDict
from .base import Base 

class Bpl(Base):
    """ BPL : Below Poverty Line """
    def __init__(self):
        """ Constructor of  BPL : Below Poverty Line """
        super(Bpl,self).__init__()
        self.cal_bpl()

    def cal_bpl(self):
        print("==============================================="*3)
        cal=OrderedDict({30:150,20:320,150:390})
        if self.unit>200:cal[self.unit-150]=490   
        self.calof1to3(cal,5)

    def calof1to3(self,cal,phase):
        """ Calling a Base Class Calculation Method """
        super(Bpl,self).calof1to3(cal,phase)