from .base import Base 

class Non_Rgp(Base):
    """ Non-RGP : Low Tension Service for Commercial and Industrial Purpose """
    def __init__(self):
        """ Constructor of  Non-RGP : Low Tension Service for Commercial and Industrial Purpose """
        super(Non_Rgp,self).__init__()
        self.cal_non_rgp()

    def cal_non_rgp(self):
        """ Calulation of Non-RGP in This Method """
        print("======================================="*3)
        self.calof4to8(450,0)
        if self.unit<=5:
            self.amt+=70
        elif self.unit>5 and self.unit<=15:
            self.amt+=90
        print("Bill is:",self.amt,"Rs.")


    def calof4to8(self,paisa,add):
        """ Calling a Base Class Calculation Method """
        return super(Non_Rgp,self).calof4to8(paisa,add)