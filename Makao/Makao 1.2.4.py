import random
#-------------Klasy--------------

class Karta():
    def __init__(self,kolor,numer):
        self.kolor = kolor
        self.numer = numer
    def print(self):
        print(self.kolor, self.numer)

#--------------Obiekty------------

dwaPik = Karta('pik', '2')
dwaKaro = Karta('karo', '2')
dwaKier = Karta('kier', '2')
dwaTrefl = Karta('trefl', '2')
trzyKier = Karta('kier', '3')
trzyTrefl = Karta('trefl', '3')
trzyKaro = Karta('karo', '3')
trzyPik = Karta('pik', '3')
czteryTrefl = Karta('trefl', '4')
czteryKier = Karta('kier', '4')
czteryKaro = Karta('karo', '4')
czteryPik = Karta('pik', '4')
piecTrefl = Karta('trefl', '5')
piecKier =  Karta('kier', '5')
piecKaro = Karta('karo', '5')
piecPik =Karta('pik', '5')
szescPik = Karta('pik', '6')
szescTrefl = Karta('trefl', '6')
szescKaro = Karta('karo', '6')
szescKier = Karta('kier', '6')
siedemPik = Karta('pik', '7')
siedemTrefl = Karta('trefl', '7')
siedemKaro = Karta('karo', '7')
siedemKier = Karta('kier', '7')
osiemKier = Karta('kier', '8')
osiemTrefl = Karta('trefl', '8')
osiemKaro = Karta('karo', '8')
osiemPik = Karta('pik', '8')
dziewiecPik = Karta('pik', '9')
dziewiecKier = Karta('kier', '9')
dziewiecKaro = Karta('karo', '9')
dziewiecTrefl = Karta('trefl', '9')
dziesiecKier = Karta('kier', '10')
dziesiecTrefl = Karta('trefl', '10')
dziesiecKaro = Karta('karo', '10')
dziesiecPik = Karta('pik', '10')
waletKier = Karta('kier', 'W')
waletKaro = Karta('karo', 'W')
waletPik = Karta('pik', 'W')
waletTrefl = Karta('trefl', 'W')
damaPik = Karta('pik', 'D')
damaKier = Karta('kier', 'D')
damaKaro = Karta('karo', 'D')
damaTrefl = Karta('trefl', 'D')
krolTrefl = Karta('trefl', 'K')
krolKaro = Karta('karo', 'K')
krolKier = Karta('kier', 'K')
krolPik = Karta('pik', 'K')
asTrefl = Karta('trefl', 'A')
asPik = Karta('pik', 'A')
asKaro = Karta('karo', 'A')
asKier = Karta('kier', 'A')

#--------------Zmienne------------

Gracz1 = []
GraczCPU = []
Talia1 = [damaKaro, damaKier, damaPik,damaTrefl,trzyKaro,trzyKier,trzyPik,trzyTrefl,czteryKaro,czteryKier,czteryTrefl,czteryPik,
          piecKaro,piecKier,piecPik,piecTrefl,szescKaro,szescKier,szescPik,szescTrefl,siedemKaro,siedemKier,siedemPik,siedemTrefl,
          osiemKaro,osiemKier,osiemPik,osiemTrefl,dziewiecKaro,dziewiecKier,dziewiecPik,dziewiecTrefl,dziesiecKaro,dziesiecKier,dziesiecPik,dziesiecTrefl,
          waletKaro,waletKier,waletPik,waletTrefl,damaTrefl,damaPik,damaKier,damaKaro,krolKaro,krolKier,krolPik,krolTrefl,asKaro,asKier,asPik,asTrefl]
Cmentarz = []
q = random.randint(13,37)
KartaStol = Talia1[q]
#--------------------Defy------------------

def PodajKartyGracza():
    for i in range(5):
        x = random.randint(0,len(Talia1))
        y = Talia1[x]
        Gracz1.append(y)
        Talia1.remove(y)
        print(i+1, ') ', y.numer, y.kolor)
def PodajKartyCPU():
    for i in range(5):
        x = random.randint(0,len(Talia1))
        y = Talia1[x]
        GraczCPU.append(y)
        Talia1.remove(y)
        print(i+1, ') ', y.numer, y.kolor)
def Check_if_swap():
    if len(Talia1) == 0:
        Talia1 == Cmentarz
PodajKartyGracza()

PodajKartyCPU()


#----------------Gra-----------------------------

while len(Gracz1) > 0 or len(GraczCPU) > 0:
    print(KartaStol.numer, KartaStol.kolor)
#---------------Tura gracza-----------------------

    while True:
        z = int(input("Wpisz numer karty: "))
        if z - 1 <= len(Gracz1):
            x = Gracz1[z-1]
        else:
            print("Za duzy numer!")
            continue
        if z == 0:
            x = random.randint(0, len(Talia1))
            y = Talia1[x]
            Gracz1.append(y)
            Talia1.remove(y)
            break
        if x.kolor == KartaStol.kolor or x.numer == KartaStol.numer:
            Gracz1.remove(x)
            Cmentarz.append(x)
            KartaStol = x
            print(x.numer, x.kolor)
            break
        else:
            print("Zla karta!")


#----------------------TuraCPU-------------------

    if True:
        for i in range(len(GraczCPU)):
            x = GraczCPU[i]
            if x.numer == KartaStol.numer or x.kolor == KartaStol.kolor:
                KartaStol = x
                GraczCPU.remove(x)
                Cmentarz.append(x)
                print(x.numer, x.kolor)
                break
        else:
            x = random.randint(0, len(Talia1))
            y = Talia1[x]
            GraczCPU.append(y)
            Talia1.remove(y)








#------------------Koniec tury---------------------
    for i in range(len(Gracz1)):
        x = Gracz1[i]
        print(i+1, ") ", x.numer, x.kolor)
    for i in range(len(GraczCPU)):
        x = GraczCPU[i]
        print(i+1, ") ", x.numer, x.kolor)
    Check_if_swap()
    if len(Gracz1) > 50:
        print("Za duzo kart w rece, przegrales!")
        break
    if len(Gracz1) == 0:
        print("Wygrales")
        break
    if len(GraczCPU) == 0:
        print("Komputer wygral! Niech zyje sztuczna inteligencja! Gin nedzny czlowiecze!")
        break
