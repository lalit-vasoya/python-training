from .base import Base


class LTP_AG(Base):
    """ LTP (AG) : Agriculture Service """
    def __init__(self):
        """ Constructor of LTP (AG) : Agriculture Service """
        super(LTP_AG,self).__init__() # calling a __init__ method of base class
        self.cal_ltp() # calling a  method of sub class or same class

    def cal_ltp(self):
        print("======================================="*3)
        self.calof4to8(330,0) # calling a inherit method of base class
        self.amt+=(self.unit*1.341)*10 
        print("Bill is:",self.amt,"Rs.")
        return