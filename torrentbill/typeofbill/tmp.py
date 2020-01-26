from .base import Base

class TMP(Base):
    """ TMP : Low Tension Temporary Supply """
    def __init__(self):
        """ Constructor of TMP : Low Tension Temporary Supply """
        super(TMP,self).__init__()
        self.cal_tmp()

    def cal_tmp(self):
        print("======================================="*3)
        super(TMP,self).calof4to8(410,25)
        print("Bill is:",self.amt,"Rs.")

