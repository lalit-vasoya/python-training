from .base import Base

class Sl(Base):
    """ SL : Low Tension Tension Street Light Service """
    def __init__(self):
        """ Constructor of SL : Low Tension Tension Street Light Service """
        super(Sl,self).__init__() # calling a __init__ method of base class
        self.cal_sl() # calling a  method of sub class or same class

    def cal_sl(self):
        print("======================================="*3)
        #super(Sl,self).calof4to8(420,0)
        self.calof4to8(420,0) # calling a inherit method of base class
        print("Bill is:",self.amt,"Rs.")
        return