from random import randint

# Blöcke
class Block():
    DurchgehbareBloecke = ['Wasser','Lava']
    def __init__(self, xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__()

    def ErmittleDurchgehbarkeit(self):
        if self.Blockart in self.DurchgehbareBloecke:
            self.Durchgehbarkeit = True
        else:
            self.Durchgehbarkeit = False
    def ErmittleDropanzahl(self):
        if self.Blockart == 'Diamant':
            self.Dropanzahl = randint(1,5)
        elif self.Blockart == 'Blätter' or self.Blockart == 'Lava':
            self.Dropanzahl = 0
        else:
            self.Dropanzahl = 1

class Materialien(Block):
    def __init__(self, xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Erde(Materialien):
    def __init__(self, xPosition, yPosition, Blockart='Gras', Farbe=(127,255,0), Abbaukraft=25, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)
    # Funktion für dirt wenn an Luft Blockart dann Gras
    def Checkgras(self,AktuelleReihe,ReihenOverall):
        if AktuelleReihe<ReihenOverall:
            self.Blockart = 'Erde'
        else:
            self.Blockart = 'Gras'



class Erze(Materialien):
    def __init__(self, xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Eisen(Erze):
    def __init__(self, xPosition, yPosition,  Blockart='Eisen', Farbe=(138,149,151), Abbaukraft=100, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden=KannGedroptWerden, Brennbarkeit=Brennbarkeit, Transparenz=Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Gold(Erze):
    def __init__(self, xPosition, yPosition,  Blockart='Gold', Farbe=(255,215,0), Abbaukraft=125, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden=KannGedroptWerden, Brennbarkeit=Brennbarkeit, Transparenz=Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Diamant(Erze):
    def __init__(self, xPosition, yPosition, Blockart='Diamant', Farbe=(112,209,244), Abbaukraft=175, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition,  Blockart, Farbe, Abbaukraft, KannGedroptWerden=KannGedroptWerden, Brennbarkeit=Brennbarkeit, Transparenz=Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Holz(Block):
    def __init__(self, xPosition, yPosition,  Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Eiche(Holz):
    def __init__(self, xPosition, yPosition, Blockart='Eiche', Farbe=(139,69,19), Abbaukraft=50, KannGedroptWerden=True, Brennbarkeit=True, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Birke(Holz):
    def __init__(self, xPosition, yPosition, Blockart='Birke', Farbe=(238,180,180), Abbaukraft=50, KannGedroptWerden=True, Brennbarkeit=True, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition,  Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Stein(Materialien):
    def __init__(self, xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Bruchstein(Stein):
    def __init__(self, xPosition, yPosition, Blockart='Bruchstein', Farbe=(122,122,122), Abbaukraft=75, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition,  Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class ReinerStein(Stein):
    def __init__(self, xPosition, yPosition, Blockart='ReinerStein', Farbe=(181,181,181), Abbaukraft=75, KannGedroptWerden=True, Brennbarkeit=False, Transparenz=0, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition, Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)



class Lava(Block):
    def __init__(self, xPosition, yPosition, Blockart='Lava', Farbe=(171,37,36), Abbaukraft=-30, KannGedroptWerden=False, Brennbarkeit=True, Transparenz=50, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition,  Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)

class Blaetter(Block):
    def __init__(self, xPosition, yPosition, Blockart='Blaetter', Farbe=(99,219,86), Abbaukraft=25, KannGedroptWerden=False, Brennbarkeit=True, Transparenz=30, Durchgehbarkeit=False, Dropanzahl=0):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.Blockart = Blockart
        self.Farbe = Farbe
        self.Abbaukraft = Abbaukraft
        self.KannGedroptWerden = KannGedroptWerden
        self.Brennbarkeit = Brennbarkeit
        self.Transparenz = Transparenz
        self.Durchgehbarkeit = Durchgehbarkeit
        self.Dropanzahl = Dropanzahl
        super().__init__(xPosition, yPosition,  Blockart, Farbe, Abbaukraft, KannGedroptWerden, Brennbarkeit, Transparenz, Durchgehbarkeit=Durchgehbarkeit, Dropanzahl=Dropanzahl)


# Spieler und Gegner
class Wesen():
    def __init__(self,Level,Name,Schadenspunkte,Lebenspunkte,x,y,Breite,Hoehe):
        self.Level = Level
        self.Name = Name
        self.Schaden = Schadenspunkte
        self.Lebenspunkte = Lebenspunkte
        self.x = x
        self.y = y
        self.Breite = Breite
        self.Hoehe = Hoehe
    
class Spieler(Wesen):
    def __init__(self, Level, Name, Schadenspunkte, Lebenspunkte, x, y, Breite, Hoehe,Slot1,Slot1Anzahl,Slot2,Slot2Anzahl,Slot3,Slot3Anzahl,Slot4,Slot4Anzahl,Slot5,Slot5Anzahl,Slot6,Slot6Anzahl, Pointer):
        self.Level = Level
        self.Name = Name
        self.Schaden = Schadenspunkte
        self.Lebenspunkte = Lebenspunkte
        self.x = x
        self.y = y
        self.Breite = Breite
        self.Hoehe = Hoehe
        self.Slot1 = Slot1
        self.Slot1Anzahl = Slot1Anzahl
        self.Slot2 = Slot2
        self.Slot2Anzahl = Slot2Anzahl
        self.Slot3 = Slot3
        self.Slot3Anzahl = Slot3Anzahl
        self.Slot4 = Slot4
        self.Slot4Anzahl = Slot4Anzahl
        self.Slot5 = Slot5
        self.Slot5Anzahl = Slot5Anzahl
        self.Slot6 = Slot6
        self.Slot6Anzahl = Slot6Anzahl
        self.Pointer = Pointer
        super().__init__(Level, Name, Schadenspunkte, Lebenspunkte, x, y, Breite, Hoehe)


class Gegenstände():
    Werkzeuge = ['Schwert','Spitzhacke']
    def __init__(self,Abbaukraft,Schadenswert,Gegenstandsart,Anzahl,StackgroesseMax,KannKapputtGehen,VerbrauchDauer):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
    def Verbrauchdauer(self):
        if self.Gegenstandsart in self.Werkzeuge:
            self.VerbrauchDauer = 100
            self.KannKapputtGehen = True
        else:
            self.VerbrauchDauer = -1
            self.KannKapputtGehen = False
    def AnzahlCheck(self):
        if self.Anzahl > self.StackgroesseMax:
            self.Anzahl = self.StackgroesseMax

class Platzierbare(Gegenstände):
    def __init__(self, Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Abbaukraft, Schadenswert, Gegenstandsart, Anzahl, StackgroesseMax, KannKapputtGehen, VerbrauchDauer)

class Werkzeuge(Gegenstände):
    def __init__(self, Abbaukraft, Schadenswert, Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, StackgroesseMax=1):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Abbaukraft, Schadenswert, Gegenstandsart, Anzahl, StackgroesseMax, KannKapputtGehen, VerbrauchDauer)

class Bruchstein_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Bruchstein'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Erde_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Erde'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Eiche_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Eiche'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Birke_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Birke'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Diamant_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Diamant'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Eisen_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Eisen'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Gold_GS(Platzierbare):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=1, StackgroesseMax=32, Gegenstandsart='Gold'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=Abbaukraft, Schadenswert=Schadenswert, StackgroesseMax=StackgroesseMax)

class Schwert(Werkzeuge):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=1, Schadenswert=25, StackgroesseMax=1, Gegenstandsart='Schwert'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Abbaukraft, Schadenswert, Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, StackgroesseMax=StackgroesseMax)

class Spitzhacke(Werkzeuge):
    def __init__(self, Anzahl, KannKapputtGehen, VerbrauchDauer, Abbaukraft=25, Schadenswert=1, StackgroesseMax=1, Gegenstandsart='Spitzhacke'):
        self.Abbaukraft = Abbaukraft
        self.Schadenswert = Schadenswert
        self.Gegenstandsart = Gegenstandsart
        self.Anzahl = Anzahl
        self.StackgroesseMax = StackgroesseMax
        self.KannKapputtGehen = KannKapputtGehen
        self.VerbrauchDauer = VerbrauchDauer
        super().__init__(Abbaukraft, Schadenswert, Gegenstandsart, Anzahl, KannKapputtGehen, VerbrauchDauer, StackgroesseMax=StackgroesseMax)