
import pickle, os,math
from tkinter import N


class Gun:
    def __init__(self,name,dsus,dps,dmag,d):
        self.name = name
        self.dsus = dsus
        self.dps = dps
        self.dmag = dmag
        self.d = d

    def toString(self):
        return f"""{self.name}:  dsus: {self.dsus} | dps: {self.dps} | dmag: {self.dmag}"""
tp = {
    "1":1*4,
    "2":6*4,
    "3":12*4,
    "4":16*4
}
eleCo = {
    "f":[1.2,.5,.8],
    "s":[.9,1.5,.9],
    "e":[1,1,1],
    "c":[.8,.8,2]
}
eleMul = {"f" : .6, "s":1,"e":1.5,"c":.4 }
gFX = {
    "1": {
        "1":{
            "f":[0,0,1],
            "s":[0,0,1],
            "e":[100,0,1],
            "c":[0,0,1]
        },
        "2":{
            "f":[100,32,1],
            "s":[100,32,1],
            "e":[100,32,1],
            "c":[100,32,1]
        },
        "3":{
            "f":[100,44,1.5],
            "s":[100,44,1.5],
            "e":[100,44,1.5],
            "c":[100,44,1.5]
        },
        "4":{
            "f":[100,56,2],
            "s":[100,56,2],
            "e":[100,56,2],
            "c":[100,56,2]
        }
    },
    "2": {
        "1":{
            "f":[100,0,1],
            "s":[100,0,1],
            "e":[100,0,1],
            "c":[100,0,1]
        },
        "2":{
            "f":[40,20,1],
            "s":[40,20,1],
            "e":[40,20,1],
            "c":[40,20,1]
        },
        "3":{
            "f":[20,20,1.5],
            "s":[20,20,1.5],
            "e":[20,20,1.5],
            "c":[20,20,1.5]
            },
        "4":{
            "f":[15,20,2],
            "s":[15,20,2],
            "e":[15,20,2],
            "c":[15,20,2]
        },
    },
    "3": {
        "1":{
            "f":[25,20,1],
            "s":[25,20,1],
            "e":[25,20,1],
            "c":[25,20,1]
        },
        "2":{
            "f":[10,20,1],
            "s":[10,20,1],
            "e":[10,20,1],
            "c":[10,20,1]
        },
        "3":{
            "f":[10,20,1],
            "s":[10,20,1],
            "e":[10,20,1],
            "c":[10,20,1]
        },
        "4":{
            "f":[15,20,1],
            "s":[15,20,1],
            "e":[15,20,1],
            "c":[15,20,1]
        }
    },
    "4": {
        "1":{
            "f":[25,12,1],
            "s":[25,12,1],
            "e":[25,12,1],
            "c":[25,12,1]
        },
        "2":{
            "f":[10,14,1],
            "s":[10,14,1],
            "e":[10,14,1],
            "c":[10,14,1]
        },
        "3":{
            "f":[10,16,1],
            "s":[10,16,1],
            "e":[10,16,1],
            "c":[10,16,1]
        },
        "4":{
            "f":[20,24,1],
            "s":[20,24,1],
            "e":[20,24,1],
            "c":[20,24,1],
        },
    },
    "5": {
        "1":{
            "f":[30,4,1],
            "s":[30,4,1],
            "e":[30,4,1],
            "c":[30,4,1]
        },
        "2":{
            "f":[15,4,1],
            "s":[15,4,1],
            "e":[15,4,1],
            "c":[15,4,1]
        },
        "3":{
            "f":[15,5,1],
            "s":[15,5,1],
            "e":[15,5,1],
            "c":[15,5,1]
        },
        "4":{
            "f":[10,5,1],
            "s":[5,5,1],
            "e":[10,5,1],
            "c":[10,5,1]
        }
    },
    "6": {
        "1":{
            "f":[70,20,1],
            "s":[70,20,1],
            "e":[70,20,1],
            "c":[70,20,1]
        },
        "2":{
            "f":[20,16,1],
            "s":[20,16,1],
            "e":[20,16,1],
            "c":[20,16,1]
        },
        "3": {
            "f":[20,12,1.5],
            "s":[20,12,1.5],
            "e":[20,12,1.5],
            "c":[20,12,1.5,1.5]
            }
            ,
        "4":{
            "f":[40,30,1.5],
            "s":[40,30,1.5],
            "e":[40,30,1.5],
            "c":[40,30,1.5]
        },
    },
    "7": {
        "1":{
            "f":[100,0,1],
            "s":[100,0,1],
            "e":[100,0,1],
            "c":[100,0,1],
        },
        "2":{
            "f":[100,0,1],
            "s":[100,0,1],
            "e":[100,0,1],
            "c":[100,0,1],
        },
        "3":{
            "f":[100,0,1],
            "s":[100,0,1],
            "e":[100,0,1],
            "c":[100,0,1],
        },
        "4":{
            "f":[100,0,1],
            "s":[100,0,1],
            "e":[100,0,1],
            "c":[100,0,1],
        },
    }
}
#start of body
os.system('cls')
os.system('mode con: cols=151 lines=50')
guns = [None]*4
eleguns = [None]*4
print(
"______               _           _                 _       _                     _             _     _____       _            _       _             \n"
"| ___ \             | |         | |               | |     | |                   | |           | |   /  __ \     | |          | |     | |            \n"
"| |_/ / ___  _ __ __| | ___ _ __| | __ _ _ __   __| |___  | |     ___   __ _  __| | ___  _   _| |_  | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n"
"| ___ \/ _ \| '__/ _` |/ _ \ '__| |/ _` | '_ \ / _` / __| | |    / _ \ / _` |/ _` |/ _ \| | | | __| | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|\n"
"| |_/ / (_) | | | (_| |  __/ |  | | (_| | | | | (_| \__ \ | |___| (_) | (_| | (_| | (_) | |_| | |_  | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   \n"
"\____/ \___/|_|  \__,_|\___|_|  |_|\__,_|_| |_|\__,_|___/ \_____/\___/ \__,_|\__,_|\___/ \__,_|\__|  \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   \n"
)

try:
    if os.stat('GunData.bgc').st_size != 0:

        with open('GunData.bgc', 'rb') as f:
            print(

                "===================================================="
                "\nLoading from directory: ",os.getcwd(),
                "\n===================================================="
                )
            temp = pickle.load(f)
            guns = temp[0]
            eleguns = temp[1]
            
            
            
        
        print("\ncurrent weapons: ")
        for g in guns:
            if g == None:
                print("\t","no other equipped gun data")
                break
            else:
                print("\t",g.toString())
        print("\nelemental guns:")
        for g in eleguns:
            if g == None:
                print("\t","no other elemental gun data")
                break
            else:
                print("\t",g.toString())
except:
    print("no previous save data found")
    if input("would you like to continue y or n  ") == "n":
        quit()
    else:
        print("creating new data file")

eleguns.append(None)

i = "a"
while True:
    i = input(
        "\nMenu"
        "\n=================================================="
        "\nnew gun (any)"
        "\nelemental gun tables (t)"
        "\nchange a gun (int of slot of gun)"
        "\nchange elemental gun (first letter of the element)"
        "\nend (-)"
        "\n=================================================="
        "\nchoice: "
        )
    if i == "-": break

    if i == "t":
        print ("\n{:<30} {:<20} {:<20} {:<20} {:<20}".format('Gun','Flesh','Shield','Armor','AVG'))
        j = 0
        for g in eleguns:
            if g != None:
                type = ["f","s","e","c"]
                flesh = g.dsus*eleCo[type[j]][0]
                shield = g.dsus*eleCo[type[j]][1]
                armor = g.dsus*eleCo[type[j]][2]
                avg = (flesh+shield+armor)/3
                print ("{:<30} {:<20} {:<20} {:<20} {:<20}".format(g.name,flesh,shield,armor,avg))
                j+=1
        continue




    valid = False
    print("\nNEW GUN:\n==============")

    while not valid:
        try:
            d = float(eval(input("input damage: ")))
            if d == "" : 
                valid = False
                print("not valid")
            else:
                valid = True
            
        except:
            valid = False
            print("not valid")

    valid = False
    while not valid:
        try:
            rof = float(input("input rate of fire: "))
            if d == "": 
                valid = False
                print("not valid")
            else:
                valid = True
        except:
            valid = False
            print("not valid")
    valid = False
    while not valid:
        try:
            m = float(eval(input("input mag size: ")))
            if d == "": 
                valid = False
                print("not valid")
            else:
                valid = True
        except:
            valid = False
            print("not valid")

    valid = False
    while not valid:
        try:
            brl = float(input("input base reload speed: "))
            if d == "": 
                valid = False
                print("not valid")
            else:
                valid = True
        except:
            valid = False
            print("not valid")
    valid = False
    while not valid:
        try:
            mrl = float(input("input reload speed modifier: "))
            if d == "": 
                valid = False
                print("not valid")
            else:
                valid = True
        except:
            valid = False
            print("not valid")

    valid = False
    while not valid:
        try:  
            ele = input("Elemental type (enter for nothing): ")
            if ele not in ["f","s","e","c",""]: 
                valid = False
                print("not valid")
            else:
                valid = True
        except:
            valid = False
            print("not valid")
    
    dps = d *rof
    dmag = d*m
    if m <2 : m =2
    tun= (m-1)/rof
    if tun == 0 : tun = .000000000001
    trl = brl/(1+(mrl/100))
    rsus = rof * tun / (tun+trl)
    dsus = d *rsus
    gtype = ""

    if ele == "f" or  ele == "s"  or ele == "c" or  ele == "e":
        gtype = input("what is the gun type {sniper(1), revolver(2), shotgun(3), smg(4), repeater(5), combat rifle(6), rocket(7): ")
        mul = input("what is the multiplier: ")
        charge = tun*4
        pt = math.floor(m*(gFX[gtype][mul][ele][0]/100))
        if pt<1:
            pt=1
        sted = d + (d*(eleMul[ele]*gFX[gtype][mul][ele][2]))
        
        if(gFX[gtype][mul][ele][1] == 0):
            bbp = m
        else:
            bbp = math.floor(charge/gFX[gtype][mul][ele][1])+1
       
       
        t = tun/bbp
        pps = t/rof
        pdmg = sted*pps
        
        dmag = d*(m-bbp)+sted*bbp
        if m <2 : m =2
        tun= (m-1)/rof
       
        dps=dmag/tun
        trl = brl/(1+(mrl/100))
        rsus = rof * tun / (tun+trl)
        dsus = dmag/m * rsus
        

        


    
    print("dps: ",dps)
    print("mag damage: ",dmag)
    print("time to unload mag: ",tun)
    print("time to reload: ",trl)
    print("rate of fire with reload: ",rsus)
    print("dps with reload: ",dsus)
    named =False
    if ele == "f" or  ele == "s"  or ele == "c" or  ele == "e":
        if i == "f" or i == "s" or i == "e" or i == "c":
            element={"f":0,"s":1,"e":2,"c":3}
            eleguns[element[i]] =None
        if ele == "f": 
            if eleguns[0]== None:
                eleguns[0]=Gun(input("input name of the gun "),dsus,dps,dmag,d)
            elif(eleguns[0].dsus <= dsus):
                eleguns[0]=Gun(input("input name of the gun "),dsus,dps,dmag,d)

        elif  ele == "s":  
            if eleguns[1]== None:
                eleguns[1]=Gun(input("input name of the gun "),dsus,dps,dmag,d)
            elif(eleguns[1].dsus <= dsus):
                eleguns[1]=Gun(input("input name of the gun "),dsus,dps,dmag,d)

        elif ele == "c":
            if eleguns[3]== None:
                eleguns[3]=Gun(input("input name of the gun "),dsus,dps,dmag,d)
            elif(eleguns[3].dsus <= dsus):
                eleguns[3]=Gun(input("input name of the gun "),dsus,dps,dmag,d)

        elif  ele == "e":
            gtemp = None
            named = False
            if eleguns[2]== None:
                gtemp = Gun(input("input name of the gun "),dsus,dps,dmag,d)
                eleguns[2]=gtemp
                named = True
            elif(eleguns[2].dsus <= dsus):
                eleguns[2]=Gun(input("input name of the gun "),dsus,dps,dmag,d)
                named = True
                
            if i == "1" or i == "2" or i == "3" or i == "4":
                guns[int(i)-1] =None
            
            
            if guns[0] != None:
                if dsus >guns[0].dsus:
                    if gtemp != None:
                        guns[0] = gtemp
                        
                    else:
                        gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                        guns[0]=gtemp
                        named = True
            else:
                if gtemp != None:
                    guns[0] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[0]=gtemp
                    named = True
                
            if guns[1] != None:
                if dps >guns[1].dps:
                    if gtemp != None:
                        guns[1] = gtemp
                        
                    else:
                        gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                        guns[1]=gtemp
                        named = True
            else:
                if gtemp != None:
                    guns[1] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[1]=gtemp
                    named = True

                
            if guns[2] != None:
                if dmag >guns[2].dmag:
                    if gtemp != None:
                        guns[2] = gtemp
                    else:
                        gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                        guns[2]=gtemp
                        named = True
            else:
                if gtemp != None:
                    guns[2] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[2]=gtemp
                    named = True

            if guns[3] != None:
                if d >guns[3].d:
                    if gtemp != None:
                        guns[3] = gtemp
                    else:
                        gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                        guns[3]=gtemp
                        named = True
            else:
                if gtemp != None:
                    guns[3] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[3]=gtemp
                    named = True

            



           
                
    
    
    else: 
        print("else")
        if i == "1" or i == "2" or i == "3" or i == "4":
                guns[int(i)-1] =None

        
        

        
        if named != True:
            gtemp = None
        



        if guns[0] != None:
            print("not None")
            if dsus > guns[0].dsus:
                print("gt")
                if gtemp != None:
                    print("ne")
                    guns[0] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[0]=gtemp
        else:
            if gtemp != None:
                guns[0] = gtemp
            else:
                gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                guns[0]=gtemp
        

        if guns[1] != None:
            if dps >guns[1].dps:
                if gtemp != None:
                    guns[1] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[1]=gtemp
        else:
            if gtemp != None:
                guns[1] = gtemp
            else:
                gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                guns[1]=gtemp

            
        if guns[2] != None:
            if dmag >guns[2].dmag:
                if gtemp != None:
                    guns[2] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[2]=gtemp
        else:
            if gtemp != None:
                guns[2] = gtemp
            else:
                gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                guns[2]=gtemp

        if guns[3] != None:
           
            if d >guns[3].d:
                if gtemp != None:
                    guns[3] = gtemp
                else:
                    gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                    guns[3]=gtemp
        else:
            if gtemp != None:
                guns[3] = gtemp
            else:
                gtemp =Gun(input("input name of the gun "),dsus,dps,dmag,d)
                guns[3]=gtemp
        
        
            
            
            
                

                
                
            

  

    cats = ["Dmg Sustained: ","DPS: ","Mag Dmg: ","One-Shot: "]
    print("\nnew loadout")
    for g,c in zip(guns,cats):
        if g != None:
            print(f'''{c}: {g.name} | dsus: {g.dsus} | dps: {g.dps} | dmag: {g.dmag} | One-shot: {g.d}''')

    print("\nelemental guns:")
    cats = ["Fire: ","Shock: ","Explosive: ","Caustic: "]
    for g,c in zip(eleguns,cats):
        if g != None:
            print(f'''{c}: {g.name} | dsus: {g.dsus} | dps: {g.dps} | dmag: {g.dmag} | One-shot: {g.d}''')

    
    with open('GunData.bgc', 'wb') as f:
        temp = [guns,eleguns]
        pickle.dump(temp,f,pickle.HIGHEST_PROTOCOL)
        
        print(
            "\n===================================================="
            "\nUpdating data "
            "\n===================================================="
            )


with open('GunData.bgc', 'wb') as f:
    temp = [guns,eleguns]
    pickle.dump(temp,f,pickle.HIGHEST_PROTOCOL)
    
    print(
        "\n===================================================="
        "\nsaved in directory: ",os.getcwd(),
        "\n===================================================="
        )
   

