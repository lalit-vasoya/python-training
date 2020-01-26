from .base import Base

class Sl(Base):
    """ SL : Low Tension Tension Street Light Service """
    def __init__(self):
        """ Constructor of SL : Low Tension Tension Street Light Service """
        super(Sl,self).__init__()
        self.cal_sl()

    def cal_sl(self):
        print("======================================="*3)
        super(Sl,self).calof4to8(420,0)
        print("Bill is:",self.amt,"Rs.")