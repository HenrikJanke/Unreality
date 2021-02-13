import klassen as K
from random import randint
import pygame

# Funktion eigentlich unnötig
def Blockanzahl(HoeheBlock,BreiteBlock,Blockinsg):
    # Erstellen der Variablen Namen mit den Die Objekte angesprochen werden können bsp.: 'R1Blcok10'  für den Zehnten Block in der Ersten Reihe
    Name = []
    for i in range (1,HoeheBlock+1):
        for e in range(1,BreiteBlock+1):
            s = 'R'+str(i)+'Block'+str(e)
            Name.append(s)
    return Name

# Baumart, um den BaumGenerator zu erleichtern
def Baueme(x,y,Baumart):
    if Baumart == 1:
        return K.Eiche(x,y)
    if Baumart == 2:
        return K.Birke(x,y)
    if Baumart == 3:
        return K.Blaetter(x,y)

# Aktuell nur ein Baum, (Zufallszahl immer kleiner als 4)
def BaumGenerator(Blockgroesse,HoeheBlock,BreiteBlock,Hoehe,Breite):
    Baumtyp = randint(1,6)
    Baumart = randint(1,2)
    Baum = []
    xVerschiebung = int(randint(3,BreiteBlock-4))
    z = []
    k = 0
    if Baumtyp < 5:
        for i in range (0,2):
            Baum.append(Baueme(Breite-Blockgroesse*xVerschiebung,Hoehe-(HoeheBlock+k)*Blockgroesse,Baumart))
            k+=1
        k=2
        for i in range(0,3):
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-1),Hoehe-(HoeheBlock+k)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung+1),Hoehe-(HoeheBlock+k)*Blockgroesse,3))          
            k+=1
        k=3
        for i in range(0,1):
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung+2),Hoehe-(HoeheBlock+k)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-2),Hoehe-(HoeheBlock+k)*Blockgroesse,3))
        k = 4
        for i in range(0,4):
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung),Hoehe-(HoeheBlock+k-2)*Blockgroesse,3))
            k+=1
    
    if Baumtyp == 5:
        hilfe = k
        for i in range(0,9):
            #                                       hier x Verschiebung         k+ ist Y Verschiebung
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+4),Hoehe-(HoeheBlock+k+3)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+4),Hoehe-(HoeheBlock+k+4)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+4),Hoehe-(HoeheBlock+k+5)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+4),Hoehe-(HoeheBlock+k+6)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+4),Hoehe-(HoeheBlock+k+7)*Blockgroesse,3))

        for i in range(0,7):
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+3),Hoehe-(HoeheBlock+k+2)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i+3),Hoehe-(HoeheBlock+k+8)*Blockgroesse,3))

        for i in range(0,3):
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung+5),Hoehe-(HoeheBlock+k+i+4)*Blockgroesse,3))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-5),Hoehe-(HoeheBlock+k+i+4)*Blockgroesse,3))

        #Stamm
        for i in range(0,5):
            Baum.append(Baueme(Breite-Blockgroesse*xVerschiebung,Hoehe-(HoeheBlock+hilfe)*Blockgroesse,Baumart))
            hilfe+=1
        #Mittelstamm
        for i in range(2,4):
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung+i),Hoehe-(HoeheBlock+k+5)*Blockgroesse,Baumart))
            Baum.append(Baueme(Breite-Blockgroesse*(xVerschiebung-i),Hoehe-(HoeheBlock+k+5)*Blockgroesse,Baumart))
    for i in Baum:
        z.append(i)
    return z
    
def Berg_Bloecke(X,Y,Bildschirm_Breite,Untere_Breite,Anzahl):
    Zufall = randint(0,100)
    # Wenn der Block über X hinweg geht
    # If Abfrage, das wenn es Größer als Breite ist (Fensterbreite) oder kleiner als 0, dann an der anderen Seite Weiter machen
    if X>=Bildschirm_Breite:
        X -= Bildschirm_Breite
    if Untere_Breite==Anzahl or Anzahl == 1:
        Finaler_Block = K.Erde(X,Y)
    elif Zufall <= 2:
        Finaler_Block = K.Diamant(X,Y)
    elif Zufall <= 5:
        Finaler_Block = K.Gold(X,Y)
    elif Zufall <= 15:
        Finaler_Block = K.Eisen(X,Y)
    elif Zufall <= 20:
        Finaler_Block = K.Erde(X,Y)
        Finaler_Block.Blockart = "Erde"
    else:
        Finaler_Block = K.ReinerStein(X,Y)

    return Finaler_Block
    # Wenn der Block nicht über X hinweg geht

def Recursiv_Berg(X,Y,Bildschirm_Breite,Blockgroesse, Untere_Breite,List):
    Anzahl = 0
    for i in range(1,Untere_Breite):
        Anzahl+=1
        List.append(Berg_Bloecke(X+((i+1)*Blockgroesse),Y-Blockgroesse,Bildschirm_Breite,Untere_Breite-1,Anzahl))
    if Untere_Breite>=6:
        Recursiv_Berg(X+Blockgroesse,Y-Blockgroesse,Bildschirm_Breite,Blockgroesse,Untere_Breite-2,List)    
    else:
        # Oberste Reihe komplett mit Gras bedeckt
        for i in range(1,Untere_Breite):
            List.append(Berg_Bloecke(X+((i+1)*Blockgroesse),Y-Blockgroesse,Bildschirm_Breite,Untere_Breite-1,1))
    return List


def Berge(Blockgroesse,Hoehe,Breite,HoeheBlock,BreiteBlock,Baum):
    Groeßter_X = 0
    Kleinster_X = 20000
    Groeßter_Y = 0
    Untere_Breite_Berg = randint(10,21)
    # Ist in der "Erde drinne"
    Kleinster_Y = (HoeheBlock+6)*Blockgroesse
    Liste = []

    # Größter und Kleinster X Wert
    for i in Baum:
        if i.xPosition > Groeßter_X:
            Groeßter_X = i.xPosition
        if i.xPosition < Kleinster_X:
            Kleinster_X = i.xPosition
        if i.yPosition > Groeßter_Y:
            Groeßter_Y = i.yPosition
    
    Groeßter_X+=Blockgroesse
    # Wenn kein Baum da ist, Random wo der Berg ist
    if Baum == []:
        Groeßter_X = (randint(0,32))*Blockgroesse
    return Recursiv_Berg(Groeßter_X,Kleinster_Y,Breite,Blockgroesse,Untere_Breite_Berg,[])

    




def Generator(Blockgroesse,Hoehe,Breite,HoeheBlock,BreiteBlock):
    # Da der unterste Block sonst im Nicht Darstellbaren Bereich gehen würde                x=0, y=1 ist der AusgangsPunkt unten Rechts
    # Anzahl der Blöcke wie Hoch der Generator geht (7 Hoch)
    HoeheBlock = int(HoeheBlock/2-2)
    # Namen der Objekte 
    ObjektNamen = Blockanzahl(HoeheBlock,BreiteBlock,(HoeheBlock*BreiteBlock))
    # Liste aller Objekte die Später Zurück gegeben wird
    AlleObjekte = []
    Blocknummer = 0
    BreiteGanzRechts = BreiteBlock-1
    HoeheGanzOben = HoeheBlock-1
    for y in range(HoeheBlock):
        for x in range(BreiteBlock):
            if y != HoeheGanzOben:
                Zufall = randint(0,50)
                if Zufall<2:
                    ObjektNamen[int(Blocknummer)] = K.Diamant(x*32,Hoehe-Blockgroesse*y)
                elif Zufall<10 and not Zufall<2:
                    ObjektNamen[int(Blocknummer)] = K.Eisen(x*32,Hoehe-Blockgroesse*y)
                elif Zufall<15 and not Zufall<10:
                    ObjektNamen[int(Blocknummer)] = K.Erde(x*32,Hoehe-Blockgroesse*y)
                    ObjektNamen[int(Blocknummer)].Checkgras(y,HoeheGanzOben)
                elif Zufall<18 and not Zufall<15:
                    ObjektNamen[int(Blocknummer)] = K.Gold(x*32,Hoehe-Blockgroesse*y)
                else:
                    ObjektNamen[int(Blocknummer)] = K.ReinerStein(x*32,Hoehe-Blockgroesse*y)
            else:
                ObjektNamen[int(Blocknummer)] = K.Erde(x*32,Hoehe-Blockgroesse*y)
                ObjektNamen[int(Blocknummer)].Checkgras(y,HoeheGanzOben)
            
            AlleObjekte.append(ObjektNamen[int(Blocknummer)])
            Blocknummer+=1
    Baum = BaumGenerator(Blockgroesse,HoeheBlock,BreiteBlock,Hoehe,Breite)
    for k in Baum:
        AlleObjekte.append(k)
    Berg = Berge(Blockgroesse,Hoehe,Breite,HoeheBlock,BreiteBlock,Baum)
    for i in Berg:
        AlleObjekte.append(i)
    return AlleObjekte

