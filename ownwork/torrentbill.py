from collections import OrderedDict

def maincal(cal,unit,phase):
    amt=0
    for i in cal:
        if i<=unit: amt+=i*cal[i] 
        elif unit>=0: amt+=unit*cal[i]
        else: break
        unit-=i
    
    amt=amt/100
    amt+=phase
    print("Bill is:",amt,"Rs.")

def func1(unit):
    subcat=(("[1] Single Phase",25),("[2] Three Phase",65),("[0] Exit",0)) 
    print(*map(lambda p:p[0],subcat),sep="\n")
    print("==============================================="*3)
    choice=int(input("Enter Phase:"))
    if choice>=len(subcat) or choice<0:print("Wrong Input");return
    cal=OrderedDict({50:320,150:390})
    if unit>200:cal[unit-150]=490
    maincal(cal,unit,subcat[choice-1][1])


def func2(unit):
    print("==============================================="*3)
    cal=OrderedDict({30:150,20:320,150:390})
    if unit>200:cal[unit-150]=490   
    print("Bill is:",amt,"Rs.")
    maincal(cal,unit,5)

def func3(unit):
    subcat=(("[1] Single Phase",30),("[2] Three Phase",70),("[0] Exit",0)) 
    print(*map(lambda p:p[0],subcat),sep="\n")
    print("==============================================="*3)
    choice=int(input("Enter Phase:"))
    if choice>=len(subcat) or choice<0:print("Wrong Input");return
    cal=OrderedDict({200:410})
    if unit>200:cal[unit-200]=480
    maincal(cal,unit,subcat[choice-1][1])

def func4(unit):
    print("======================================="*3)
    amt=(unit*450)/100
    if unit<=5:
        amt+=70
    elif unit>5 and unit<=15:
        amt+=90
    print("Bill is:",amt,"Rs.")
    
def func5(unit):
    print("======================================="*3)
    amt=(unit*330)/100
    amt+=(unit*1.341)*10
    print("Bill is:",amt,"Rs.")

def func6(unit):print("Bill is:",(unit*420)/100,"Rs.")

def func7(unit):print("Bill is:",((unit*410)/100)+25,"Rs.")

def func8(unit):print("Bill is:",((unit*500)/100)+(25),"Rs.")



if __name__=="__main__":
    maincat={1:("[1] RGP : Residential General Purpose",func1),
            2:("[2] BPL : Below Poverty Line",func2),
            3:("[3] GLP : General Lighting Purpose",func3),
            4:("[4] Non-RGP : Low Tension Service for Commercial and Industrial Purpose",func4),
            5:("[5] LTP (AG) : Agriculture Service",func5),
            6:("[6] SL : Low Tension Tension Street Light Service",func6),
            7:("[7] LEV : LT- Electric Vehicle Charging Stations",func7),
            8:("[8] TMP : Low Tension Temporary Supply",func8),
            0:("[0] Exit","")}

    choice=1
    while choice!=0:
        print("==============================================="*3,)
        print(*map(lambda p:p[0],maincat.values()),sep="\n")
        print("==============================================="*3,)
        choice=int(input("Enter Bill Type Index Number:"))
        choice=choice if choice!=0 else exit()
        unit=int(input("Enter unit:"))
        if unit<=0:
            print("Wrong unit please enter one among the option")
            continue
        maincat[choice][1](unit) if choice in maincat else print("Wrong Input")
        input("End.............")
