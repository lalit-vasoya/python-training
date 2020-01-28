from .base import Base

class LevLt(Base):
    """ LEV : LT- Electric Vehicle Charging Stations """
    def __init__(self):
        """ Constructor of SL : Low Tension Tension Street Light Service """
        super(LevLt,self).__init__() # calling a __init__ method of base class
        self.cal_levlt() # calling a  method of sub class or same class

    def cal_levlt(self):
        print("======================================="*3)
        self.calof4to8(410,25) # calling a inherit method of base class
        print("Bill is:",self.amt,"Rs.")
        return

