
class Base:
    unit=0
    amt=0
    def __init__(self):
        itre_if_unit_not_valid=1
        while itre_if_unit_not_valid:
            self.unit=int(input("Enter unit:"))
            itre_if_unit_not_valid=1 if self.unit<=0 else 0

    def calof1to3(self,cal,phase):
        """ calculate the amount of specified unit per paisa """
        for i in cal:
            if i<=self.unit:
                self.amt+=i*cal[i] 
            elif self.unit>=0: 
                self.amt+=self.unit*cal[i]
            else: break
            self.unit-=i
        self.amt=self.amt/100 # convert paisa to Rs.
        self.amt+=phase # add the fix rate of Phase
        print("Bill is:",self.amt,"Rs.")
        return

    def calof4to8(self,paisa,add):
        self.amt=((self.unit*paisa)/100)+add
        return

        