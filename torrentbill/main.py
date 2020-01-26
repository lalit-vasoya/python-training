import typeofbill as tariff

CHOICE=0
if __name__=='__main__':
    maincat={1:("[1] RGP : Residential General Purpose",tariff.Rgp),
        2:("[2] BPL : Below Poverty Line",tariff.Bpl),
        3:("[3] GLP : General Lighting Purpose",tariff.Glp),
        4:("[4] Non-RGP : Low Tension Service for Commercial and Industrial Purpose",tariff.Non_Rgp),
        5:("[5] LTP (AG) : Agriculture Service",tariff.LTP_AG),
        6:("[6] SL : Low Tension Tension Street Light Service",tariff.Sl),
        7:("[7] LEV : LT- Electric Vehicle Charging Stations",tariff.LevLt),
        8:("[8] TMP : Low Tension Temporary Supply",tariff.TMP),
        0:("[0] Exit","")}
    
    try:
        print("==============================================="*3,)
        print(*map(lambda p:p[0],maincat.values()),sep="\n")
        print("==============================================="*3,)
        CHOICE=int(input("Enter Bill Type Index Number:"))

        if CHOICE<0 or CHOICE>len(maincat):
            print(f"Input in between 0 to {len(maincat)}")
        else:
            if CHOICE==0:
                exit()
            maincat[CHOICE][1]()  # calling a class constructor in the line class is bpl(),glp(),rgp()

    except Exception as e:
        print("Enter Only The Integer Field")
        #print(e)