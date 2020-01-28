from .base import Base

class TMP(Base):
    """ TMP : Low Tension Temporary Supply """
    def __init__(self):
        """ Constructor of TMP : Low Tension Temporary Supply """
        super(TMP,self).__init__() # calling a __init__ method of base class
        self.cal_tmp() # calling a  method of sub class or same class

    def cal_tmp(self):
        print("======================================="*3)
        #super(TMP,self).calof4to8(410,25)
        self.calof4to8(410,25) # calling a inherit method of base class
        print("Bill is:",self.amt,"Rs.")
        return
