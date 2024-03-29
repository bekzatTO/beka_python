import os
import sys

f='file.txt'
sys.path.append(      os.path.join( os.path.dirname(os.path.abspath(sys.argv[0])), "utils"  )             )


my_loc = os.getcwd()

my_file= my_loc + "/utils/" + f

o=open(my_file, "r")


for i in o.read().splitlines():
        if not i.startswith("#"):
                with open(my_loc + "/utils/file2","a+") as f2:
                        f2.write(i)

o.close()


times={
    "Japan": -16, 
    "Kyrgyzstan": -12,
    "Russia": -10
}

def time_zone(x):
    USA=time.localtime().tm_hour
    a=USA- times[x]
    return "For {}, it is {}".format(x,a)


print(time_zone("Russia"))

#!/root/.venv/bin/python
def get_tukum():
    return "Took tuudu"

def get_took():
    return "took, satyp aldym"


def get_rooster(tukum, took):
    # tooktun {tukum} tap
    # tukumdu {took}tu aldyna koi 30 kun
    # chojolordun ichinen korzun tap
    # any chonoit
    # urushkanga uirot
    return "Koroz"




Rooster = ( get_rooster(get_tukum(), get_took())   )
rooster = "Koroz"


print(Rooster)
print(rooster)




# --------------------------------------------------------
import os

def install_packages(x):
    os.system(r"echo 'yum install {x}' ")



def get_hostname():
    return os.system("hostname")



def is_hostname_set():
    if get_hostname() is not None:
        return True
    else:
        return False




def greeting(n):
    print ("E {}, kandaisyn?".format(n))


greeting("Venera")
b=greeting("Beka")

print(  get_hostname()   )

if get_hostname() == "DESKTOP-3U2JPUV":
    print("OK")

# if greeting("Venera") == ?:
#     print("OK")

# if install_packages("nmap") == ?

print(is_hostname_set())


# ----------------------------------------------------------

n = [12,23,34,41, 65, 50, 14]

m = [76,12,34,56,41]

box=[]

def five_maker(x):
    for i in x:
        b=str(i)
        if int(b[0]) + int(b[1]) == 5:
            box.append(i)
    return box


# print(five_maker(m))


import os, sys

os.chdir('/root')




def is_same(x, y):

    diff = os.system(' diff {} {}'.format(x,y))
    if diff != 0:
        return False
    else:
        return True



f1 = "file_3"
f2 = "file_2"


if is_same(f1,f2):
    print(f"{f1}  menen  {f2} Bul eki file chyndap okshosh eken")
else:
    print(f"{f1} menen  {f2}  Bul eki file  okshosh EMES eken")


#-------------------------------------------------------------------------

def money_converter(amount, currency_from, currency_to):

    ratio = {"USD": 1, "KGS": 85, "TL": 10}

    dol = amount / ratio[currency_from]

    if currency_from == "KGS":
        if currency_to == "USD":
            return dol
        elif currency_to == "TL":
            return dol * ratio["TL"]


    if currency_from == "TL":
        if currency_to == "USD":
            return dol
        elif currency_to == "KGS":
            return dol * ratio["KGS"]



print(money_converter(10, "TL", "KGS") )




#--------------------------------------------------------------



class Family:

    middle_name = 'Adykovich'

    def __init__(self, taga_jurt, ata_jurt, kainy_jurt):
        self.ata_jurt = ata_jurt
        self.taga_jurt = taga_jurt
        self.kainy_jurt = kainy_jurt
        


    def is_beka (self):

        if self.ata_jurt == "savai" and self.taga_jurt == "kytai":
            return True
     

    def is_emil (self):

        if self.ata_jurt == "savai" and self.taga_jurt == "latysh":
            return True


    def is_sayan (self):

        if self.ata_jurt == "monok" and self.taga_jurt == "savai":
            return True
    

    def member1(self):
        if self.is_beka():
            return "Menin atym Beka, men 16ga chyktym. Atam Mirlan"

        if self.is_emil():
            return "Menin atym Emil, men 10ga chyktym. Atam Nurik"

        if self.is_sayan():
            return "Menin atym Sayan, men 11ga chyktym. Atam Ilim"
        else:
            return "You are not in our family"



p1  =  Family("kytaii", "savai", None)

p2  =  Family("kytai", "savai", None)

p3  =  Family("latysh", "savai", None)

p4  =  Family("savai", "monok", None)


print (   p1.member1()   )

print (   p2.member1()   )

print (   p3.member1()   )

print (   p4.member1()   )




# ################################################ multiple Inheritances #####################################

# vi start.py:

balance=500
class Clothing:
    def __init__(self, shoes,pants,shirt,person):
        self.shoes=shoes
        self.pants=pants
        self.shirt=shirt
        self.person=person
        

    def shoe_fit(self):
        if self.person >= 16:
            if self.shoes<10.5:
                return "Shoes too small"
            elif self.shoes>=10.5:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10"
    def pants_fit(self):
        if self.person >= 16:
            if self.pants<33:
                return "Shoes too small"
            elif self.pants>=33:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10"

    def shirt_fit(self):
        if self.person >= 16:
            if self.shirt<18:
                return "Shirt too small"
            elif self.shirt>=18:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10" 
class Buy(Clothing):
    def __init__(self,year=None, shoes=None ,pants=None,shirt=None,person=None):
        self.year = year        
        Clothing.__init__(self,shoes,pants,shirt,person)

    def purchase(self):
        if self.shirt_fit() or self.pants_fit or self.shoe_fit == False:
            return "I have enough money to buy almost everything I want :D"
        else:
            return "I can't buy everything!"

# vi test.py:


import start

class Test(start.Buy):

    def __init__(self, age=None, year=None, shoes=None ,pants=None,shirt=None,person=None ):
        self.age = age
        start.Buy.__init__(self, year,shoes,pants,shirt,person)

    def test1(self):
        return "ishtedi"

    



# o = Test(16, 2022, 43, 33, 18, 16)
o = Test(person=13, shoes=43)


print(  o.shoe_fit()   )








def vote(party,state):
    if party == "Democrat": 
        if state == "Texas":
            return "This State is mainly for republicans so you should move out"
        elif state == "California" or "Oregon":
            return f"{state} is mainly democratic. Welcome!!!"

    elif party == "Republican":
        if state == "Idaho" or "Utah" or "South Carolina":
            return f"{state} is a mainly republican state so you can stay"
        elif state == "California" or "Oregon" or "Washington":
            return "This state is mainly democratic and you might need to move"


print(vote("Democrat","California"))
    




########################################################################


# argparse module




import math, os, sys, argparse

parser=argparse.ArgumentParser(description="Volume of all 3D objects in Geometry")
parser.add_argument("-r","--radius", type=int,help="radius")
parser.add_argument("-ht","--height", type=int,help="height")
parser.add_argument("-w","--width", type=int,help="width")
parser.add_argument("-l","--length", type=int,help="length")

args=parser.parse_args()


class Volume:
    def __init__(self, width, length,radius,height=5):
        self.r=radius
        self.h=height
        self.w=width
        self.l=length
    
    def cylinder(self):
        return self.r**2 * math.pi * self.h
    

    def sphere(self):
        return self.r**3 * math.pi *4/3
    
    def rect_prism(self):
        return self.h * self.w * self.l

height=2
width=4
length=4
radius=7

if args.height:
    height=args.height

if args.width:
    width=args.width

if args.length:
    length=args.length


p1=Volume( width, length, radius, height)   
print(p1.cylinder())



##################################################


class Foo:

    def meth1(self,x):
        return x.meth3()
    
    def meth2(self,meth1=False):
        p2=Foo()
        return p2.meth1(p2)
    
    def meth3(self):
        return f"I am from meth3"


p1=Foo()

print(p1.meth1(p1))







