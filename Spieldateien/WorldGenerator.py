import klassen as K
from random import randint

# Funktion eigentlich unnötig
def Blockanzahl(HoeheBlock,BreiteBlock,Blockinsg):
    # Erstellen der Variablen Namen mit den Die Objekte angesprochen werden können bsp.: 'R1Blcok10'  für den Zehnten Block in der Ersten Reihe
    Name = []
    for i in range (1,HoeheBlock+1):
        for e in range(1,BreiteBlock+1):
            s = 'R'+str(i)+'Block'+str(e)
            Name.append(s)
    return Name

# Aktuell nur ein Baum, (Zufallszahl immer kleiner als 4)
def BaumGenerator(Blockgroesse,HoeheBlock,BreiteBlock,Hoehe,Breite):
    Baumtyp = randint(1,3)
    Baumart = randint(1,2)
    xVerschiebung = int(randint(3,BreiteBlock-3))
    u = ['1','2','3','4']
    z = []
    k = 0
    # 1 Ganz Rechts, Breiteblock BreiteBlock ganz RLinks
    #xVerschiebung = 13
    if Baumtyp<=4:
        if Baumart==1: 
            for i in u:
                i = K.Eiche(Breite-Blockgroesse*xVerschiebung,Hoehe-(HoeheBlock+k)*Blockgroesse)
                k+=1
                z.append(i)
        else:
            for i in u:
                i = K.Birke(Breite-Blockgroesse*xVerschiebung,Hoehe-(HoeheBlock+k)*Blockgroesse)
                k+=1
                z.append(i)
        k=2
        u = u[:-1]
        for i in u:
            i = K.Blaetter(Breite-Blockgroesse*(xVerschiebung-1),Hoehe-(HoeheBlock+k)*Blockgroesse)
            z.append(i)
            i = K.Blaetter(Breite-Blockgroesse*(xVerschiebung+1),Hoehe-(HoeheBlock+k)*Blockgroesse)
            z.append(i)                
            k+=1
        k=3
        for i in u[:-2]:
            i = K.Blaetter(Breite-Blockgroesse*(xVerschiebung+2),Hoehe-(HoeheBlock+k)*Blockgroesse)
            z.append(i)
            i = K.Blaetter(Breite-Blockgroesse*(xVerschiebung-2),Hoehe-(HoeheBlock+k)*Blockgroesse)
            z.append(i)
        
        k = 4
        h = ['1','2','3','4'] 
        for i in h:
            i = K.Blaetter(Breite-Blockgroesse*(xVerschiebung),Hoehe-(HoeheBlock+k-2)*Blockgroesse)
            k+=1
            z.append(i)
    
    
    return z
    




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
    return AlleObjekte

