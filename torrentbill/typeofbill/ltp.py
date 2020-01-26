from .base import Base


class LTP_AG(Base):
    """ LTP (AG) : Agriculture Service """
    def __init__(self):
        """ Constructor of LTP (AG) : Agriculture Service """
        super(LTP_AG,self).__init__()
        self.cal_ltp()

    def cal_ltp(self):
        print("======================================="*3)
        super(LTP_AG,self).calof4to8(330,0)
        self.amt+=(self.unit*1.341)*10
        print("Bill is:",self.amt,"Rs.")