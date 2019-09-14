from CardFun import *
import random

################################## KARTY W TALII #####################################
dwaPik = DwaP()
dwaKaro = DwaKa()
dwaKier = DwaKi()
dwaTrefl = DwaT()
trzyKier = TrzyKi()
trzyTrefl = TrzyT()
trzyKaro = TrzyKa()
trzyPik = TrzyP()
czteryTrefl = CzteryT()
czteryKier = CzteryKi()
czteryKaro = CzteryKa()
czteryPik = CzteryP()
piecTrefl = PiecT()
piecKier =  PiecKi()
piecKaro = PiecKa()
piecPik =PiecP()
szescPik = SzescP()
szescTrefl = SzescT()
szescKaro = SzescKa()
szescKier = SzescKi()
siedemPik = SiedemP()
siedemTrefl = SiedemT()
siedemKaro = SiedemKa()
siedemKier = SiedemKi()
osiemKier = OsiemKi()
osiemTrefl = OsiemT()
osiemKaro = OsiemKa()
osiemPik = OsiemP()
dziewiecPik = DziewiecP()
dziewiecKier = DziewiecKi()
dziewiecKaro = DziewiecKa()
dziewiecTrefl = DziewiecT()
dziesiecKier = DziesiecKi()
dziesiecTrefl = DziesiecT()
dziesiecKaro = DziesiecKa()
dziesiecPik = DziesiecP()
waletKier = WaletKi()
waletKaro = WaletKa()
waletPik = WaletP()
waletTrefl = WaletT()
damaPik = DamaP()
damaKier = DamaKi()
damaKaro = DamaKa()
damaTrefl = DamaT()
krolTrefl = KrolOFFt()
krolKaro = KrolOFFk()
krolKier = KrolONk()
krolPik = KrolONp()
asTrefl = AsT()
asPik = AsP()
asKaro = AsKa()
asKier = AsKi()
#################################################################################
Talia = [dwaKaro, dwaKier,dwaPik,dwaTrefl,trzyKaro,trzyKier,trzyPik,trzyTrefl,czteryKaro,czteryKier,czteryPik,czteryTrefl,piecKaro,piecKier,piecPik,piecTrefl,szescKaro,szescKier,szescPik,szescTrefl,siedemKaro,siedemKier,siedemPik,siedemTrefl,osiemKaro,osiemKier,osiemPik,osiemTrefl,dziewiecKaro,dziewiecKier,dziewiecPik,dziewiecTrefl,dziesiecKaro,dziesiecKier,dziesiecPik,dziesiecTrefl,waletKaro,waletKier,waletPik,waletTrefl,damaTrefl,damaPik,damaKier,damaKaro,krolKaro,krolKier,krolPik,krolTrefl,asKaro,asKier,asPik,asTrefl]
Gracz1 = []
GraczCPU = []
Talia2 = []
def KartyGracza():
    print("Twoja reka: ")
    for i in range(5):
        x = random.randint (0, len(Talia))
        y = Talia[x]
        Gracz1.append(y)
        Talia2.append(y)
        Talia.remove(y)
        y.print()
def KartyKomputera():
    print("Reka komputera")
    for i in range(5):
        x = random.randint(0, len(Talia))
        z = Talia[x]
        GraczCPU.append(z)
        Talia2.append(z)
        Talia.remove(z)
        z.print()

def PierwszaKarta():
    x = random.randint(13,37)
    y = Talia[x]
    Talia.remove(y)
    Talia2.append(y)
    print("Pierwsza karta to: ")
    y.print()

PierwszaKarta()
KartyGracza()
print(Gracz1)
KartyKomputera()
print(GraczCPU)
print(Talia2)






