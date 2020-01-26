from .base import Base

class LevLt(Base):
    """ LEV : LT- Electric Vehicle Charging Stations """
    def __init__(self):
        """ Constructor of SL : Low Tension Tension Street Light Service """
        super(LevLt,self).__init__()
        self.cal_levlt()

    def cal_levlt(self):
        print("======================================="*3)
        super(LevLt,self).calof4to8(410,25)
        print("Bill is:",self.amt,"Rs.")

