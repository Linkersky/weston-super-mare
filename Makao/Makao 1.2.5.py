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
krolTrefl = Karta('trefl', 'Koff')
krolKaro = Karta('karo', 'Koff')
krolKier = Karta('kier', 'Kon')
krolPik = Karta('pik', 'Kon')
asTrefl = Karta('trefl', 'A')
asPik = Karta('pik', 'A')
asKaro = Karta('karo', 'A')
asKier = Karta('kier', 'A')
kartaZero = Karta ('zero', 'zero')
#--------------Zmienne------------

b = 0
a = 0
Gracz1 = []
GraczCPU = []
Talia1 = [dwaKaro, dwaKier, dwaPik,dwaTrefl,trzyKaro,trzyKier,trzyPik,trzyTrefl,czteryKaro,czteryKier,czteryTrefl,czteryPik,
          piecKaro,piecKier,piecPik,piecTrefl,szescKaro,szescKier,szescPik,szescTrefl,siedemKaro,siedemKier,siedemPik,siedemTrefl,
          osiemKaro,osiemKier,osiemPik,osiemTrefl,dziewiecKaro,dziewiecKier,dziewiecPik,dziewiecTrefl,dziesiecKaro,dziesiecKier,dziesiecPik,dziesiecTrefl,
          waletKaro,waletKier,waletPik,waletTrefl,damaTrefl,damaPik,damaKier,damaKaro,krolKaro,krolKier,krolPik,krolTrefl,asKaro,asKier,asPik,asTrefl]
q = random.randint(12,36)
KartaStol = Talia1[q]
KartaWalka = kartaZero
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
def KartaWalkaGracz2():
    global KartaWalka, KartaStol, a
    if KartaWalka.numer == '2' and a == 0:
        while True:
            z = int(input("Podaj karte bojawa: "))
            if z - 1 <= len(Gracz1):
                x = Gracz1[z - 1]
            else:
                print("Za duzy numer!")
                continue
            if z == 0:
                for i in range(2):
                    x = random.randint(0, len(Talia1))
                    y = Talia1[x]
                    Gracz1.append(y)
                    Talia1.remove(y)
                KartaWalka = kartaZero
                a = 1
                break

            if x.numer == KartaWalka.numer:
                Gracz1.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                a = 1
                break
            elif x.kolor == KartaWalka.kolor and x.numer == '3':
                Gracz1.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                a = 1
                break
            else:
                print("Zla karta!")
def KartaWalkaGracz3():
    global KartaWalka, KartaStol, a
    if KartaWalka.numer == '3' and a == 0:
        while True:
            z = int(input("Podaj karte bojawa: "))
            if z - 1 <= len(Gracz1):
                x = Gracz1[z - 1]
            else:
                print("Za duzy numer!")
                continue
            if z == 0:
                for i in range(3):
                    x = random.randint(0, len(Talia1))
                    y = Talia1[x]
                    Gracz1.append(y)
                    Talia1.remove(y)
                KartaWalka = kartaZero
                a = 1
                break

            if x.numer == KartaWalka.numer:
                Gracz1.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                a = 1
                break
            elif x.kolor == KartaWalka.kolor and x.numer == '2':
                Gracz1.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                a = 1
                break
            else:
                print("Zla karta!")
def KartaWalkaGraczKon():
    global KartaWalka, KartaStol, a
    if KartaWalka.numer == 'Kon' and a == 0:
        while True:
            z = int(input("Podaj karte bojawa: "))
            if z - 1 <= len(Gracz1):
                x = Gracz1[z - 1]
            else:
                print("Za duzy numer!")
                continue
            if z == 0:
                for i in range(5):
                    x = random.randint(0, len(Talia1))
                    y = Talia1[x]
                    Gracz1.append(y)
                    Talia1.remove(y)
                KartaWalka = kartaZero
                a = 1
                break

            if x.numer == KartaStol.numer:
                Gracz1.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                a = 1
                break
            else:
                print("Zla karta!")
def KartaStop4Gracz():
    global KartaStol, KartaWalka, a
    if KartaWalka.numer == '4':
        print("Czekasz ture!")
        a = 1
        KartaWalka = kartaZero
def KartaWalka2CPU():
    global KartaWalka, KartaStol, b
    if KartaWalka.numer == '2':
        for i in range(len(GraczCPU)):
            x = GraczCPU[i]
            if x.numer == KartaStol.numer:
                GraczCPU.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                b = 1
                print("Komuter wybral karte: ", x.numer, x.kolor)
                break
        else:
            for i in range(2):
                x = random.randint(0, len(Talia1))
                y = Talia1[x]
                GraczCPU.append(y)
                Talia1.remove(y)
                KartaWalka = kartaZero
            print("Komputer dobiera 2 karty!")
            b = 1
def KartaWalka3CPU():
    global KartaWalka, KartaStol, b
    if KartaWalka.numer == '3':
        for i in range(len(GraczCPU)):
            x = GraczCPU[i]
            if x.numer == KartaStol.numer:
                GraczCPU.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                b = 1
                print("Komuter wybral karte: ", x.numer, x.kolor)
                break
        else:
            for i in range(3):
                x = random.randint(0, len(Talia1))
                y = Talia1[x]
                GraczCPU.append(y)
                Talia1.remove(y)
                KartaWalka = kartaZero
            print("Komputer dobiera 3 karty!")
            b = 1
def KartaWalkaKonCPU():
    global KartaWalka, KartaStol, b
    if KartaWalka.numer == 'Kon':
        for i in range(len(GraczCPU)):
            x = GraczCPU[i]
            if x.numer == KartaStol.numer:
                GraczCPU.remove(x)
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                b = 1
                print("Komuter wybral karte: ", x.numer, x.kolor)
                break
        else:
            for i in range(5):
                x = random.randint(0, len(Talia1))
                y = Talia1[x]
                GraczCPU.append(y)
                Talia1.remove(y)
                KartaWalka = kartaZero
            print("Komputer dobiera 5 kart!")
            b = 1
def KartaStop4CPU():
    global KartaStol, KartaWalka, b
    if KartaWalka.numer == '4':
        print("Komputer czeka ture!")
        KartaWalka = kartaZero
        b = 1



#----------------Gra-----------------------------

PodajKartyGracza()
PodajKartyCPU()

while len(Gracz1) > 0 or len(GraczCPU) > 0:
    print('Karta na stole: ', KartaStol.numer, KartaStol.kolor)

#---------------Tura gracza-----------------------
    print("-----Tura gracza-----")
    a = 0
    KartaStop4Gracz()
    KartaWalkaGracz2()
    KartaWalkaGracz3()
    KartaWalkaGraczKon()
    if a == 0 and KartaWalka.numer != '2' and KartaWalka.numer != '3' and KartaWalka.numer != 'Kon' and KartaWalka.numer != '4':
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
                Talia1.append(x)
                KartaStol = x
                KartaWalka = x
                break
            else:
                print("Zla karta!")

    print("Karta na stole: ", KartaStol.numer, KartaStol.kolor)
#----------------------TuraCPU-------------------
    print("-----Tura komputera-----")
    if True:
        b = 0
        KartaStop4CPU()
        KartaWalka2CPU()
        KartaWalka3CPU()
        KartaWalkaKonCPU()
        if b == 0 and KartaWalka.numer != '2' and KartaWalka.numer != '3' and KartaWalka.numer != 'Kon' and KartaWalka.numer != '4':
            for i in range(len(GraczCPU)):
                x = GraczCPU[i]
                if x.numer == KartaStol.numer or x.kolor == KartaStol.kolor:
                    KartaStol = x
                    KartaWalka = x
                    GraczCPU.remove(x)
                    Talia1.append(x)
                    print("Komuter wybral karte: ",x.numer,x.kolor)
                    break
            else:
                x = random.randint(0, len(Talia1))
                y = Talia1[x]
                GraczCPU.append(y)
                Talia1.remove(y)
                print("Komputer dobiera karte!")

#------------------Koniec tury---------------------
    print("Karty gracza: ")
    for i in range(len(Gracz1)):
        x = Gracz1[i]
        print(i+1, ") ", x.numer, x.kolor)
    if len(Gracz1) > 50:
        print("!!!Za duzo kart w rece, przegrales!!!")
        break
    if len(Gracz1) == 0:
        print("!!!Po Makale, wygrales!!!")
        break
    if len(GraczCPU) == 0:
        print("!!!Po Makale, komputer wygral!!!")
        break
    if len(Gracz1) == 1:
        print("!!!Makao: Gracz!!!")
    if len(GraczCPU) == 1:
        print("!!!Makao: komputer!!!")