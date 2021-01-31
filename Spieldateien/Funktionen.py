from random import randint
import pygame
import klassen
import random
pygame.font.init()


def Blockgroesse(Breite,Hoehe):
    for i in range (20,50):
        if Breite % i == 0:
            if Hoehe % i == 0:
                int(i)
                return i

def LaengeInBloecken(Breite,Hoehe):
    Groesse = Blockgroesse(Breite,Hoehe)
    return int(Breite/Groesse)

def HoeheInBloecken(Breite,Hoehe):
    Groesse = Blockgroesse(Breite,Hoehe)
    return int(Hoehe/Groesse)




def BilderLaden(Blockgroesse):
    Erde = pygame.image.load("Data\Grafiken\Erde\dirt.png")
    Erde = pygame.transform.scale(Erde,(Blockgroesse,Blockgroesse))
    Gras = pygame.image.load('Data\Grafiken\Erde\gras.png')
    Gras = pygame.transform.scale(Gras,(Blockgroesse,Blockgroesse))
    Eisen = pygame.image.load("Data\Grafiken\Erze\iron_ore.png")
    Eisen = pygame.transform.scale(Eisen,(Blockgroesse,Blockgroesse))
    Gold = pygame.image.load('Data\Grafiken\Erze\gold_ore.png')
    Gold = pygame.transform.scale(Gold,(Blockgroesse,Blockgroesse))
    Diamant = pygame.image.load('Data\Grafiken\Erze\diamond_ore.png')
    Diamant = pygame.transform.scale(Diamant,(Blockgroesse,Blockgroesse))
    Eiche = pygame.image.load('Data\Grafiken\Holz\oak_log.png')
    Eiche = pygame.transform.scale(Eiche,(Blockgroesse,Blockgroesse))
    Birke = pygame.image.load("Data\Grafiken\Holz\Birch_log.png")
    Birke = pygame.transform.scale(Birke,(Blockgroesse,Blockgroesse))
    Bruchstein = pygame.image.load('Data\Grafiken\Stein\cobblestone.png')
    Bruchstein = pygame.transform.scale(Bruchstein,(Blockgroesse,Blockgroesse))
    ReinerStein = pygame.image.load("Data\Grafiken\Stein\stone.png")
    ReinerStein = pygame.transform.scale(ReinerStein,(Blockgroesse,Blockgroesse))
    Blaetter = pygame.image.load('Data\Grafiken\Blätter\oak.png')
    Blaetter = pygame.transform.scale(Blaetter,(Blockgroesse,Blockgroesse))
    return[Erde,Gras,Eisen,Gold,Diamant,Eiche,Birke,Bruchstein,ReinerStein,Blaetter]

def GegenstaendeLaden(Blockgroesse):
    Spitzhacke = pygame.image.load("Data\Grafiken\Gui\Gegenstände\pickaxe.png")
    Spitzhacke = pygame.transform.scale(Spitzhacke,(Blockgroesse,Blockgroesse))
    Schwert = pygame.image.load("Data\Grafiken\Gui\Gegenstände\sword.png")
    Schwert = pygame.transform.scale(Schwert,(Blockgroesse,Blockgroesse))
    return [Spitzhacke,Schwert]


# TESTFUNKTION um Blöcke zu gegenstände im Inventar zu bekommen
def Block_zu_Gegenstand (Blockart,Item_Liste):    
    z = 0
    x = randint(1,3)
    Added = False
    Item_Laenge = 0
    # Gras zu Erde und ReinerStein zu Bruchstein
    if Blockart == "Gras":
        Blockart = "Erde"
    elif Blockart == "ReinerStein":
        Blockart = "Bruchstein"
    # Item_Liste länge, wenn 6 (also maximallänge geht es nicht weiter)
    for i in Item_Liste:
        Item_Laenge += 1
       
    # Item Hinzufügen wenn es noch keins gibt
    if not Item_Liste==[]:
        for i in Item_Liste:
            if i.Gegenstandsart == Blockart:
                print("Bestehendes Item:", Blockart)
                # Wenn das Item schon im Inventar ist einen hinzufügen
                Item_Liste[z].AnzahlCheck()
                if not Item_Liste[z].Anzahl == Item_Liste[z].StackgroesseMax:
                    Item_Liste[z].Anzahl +=1
                    Added=True
                    Blockart = "Fertig"
            z+=1
    # Wenn ein Stack voll ist wird ein neuer erstellt
    if not Item_Liste==[] and Item_Laenge<6 and Added==True:
        a = 0
        for i in Item_Liste:
            if Item_Liste[a].StackgroesseMax == Item_Liste[a].Anzahl:
                Added = False
            a+=1
    # Neues Item erstellen und ins Inventar hinzufügen
    if Added == False and Item_Laenge<6:        
        if Blockart == "Bruchstein":
            Item = klassen.Bruchstein_GS(1,False,100)
        elif Blockart == "Erde" or Blockart == "Gras":
            Item = klassen.Erde_GS(1,True,2)
        elif Blockart == "Eiche":
            Item = klassen.Eiche_GS(1,False,2)
        elif Blockart == "Birke":
            Item = klassen.Birke_GS(1,False,2)
        elif Blockart == "Diamant":
            Item = klassen.Diamant_GS(x,False,3)
        elif Blockart == "Eisen":
            Item = klassen.Eisen_GS(1,False,2)
        elif Blockart == "Gold":
            Item = klassen.Gold_GS(1,False,2)
        print("Neues Item:", Blockart)
        try:
            Item.Verbrauchdauer()
            Item.AnzahlCheck()
            Item_Liste.append(Item)
            Added = True
            #break
        except:
            print("Fehler: Block zu Gegenstand", Blockart)
        Blockart = "Fertig"
    
    # Ausgabe des Aktuellen Inventars mit Anzahl der Blöcke
    for help in Item_Liste:
        print(help.Gegenstandsart,help.Anzahl)
    print("######################")

    return Item_Liste

def Item_Anzahl_Schrift(Inventar,Position,Blockgroesse,xPosition_Mulitplikator,FensterBreite):
    Anzahl=Inventar[Position].Anzahl
    x,y = 0,Blockgroesse+20
    if Inventar[Position].Gegenstandsart in ["Spitzhacke","Schwert"]:
        x = -100
        y = -100
    elif Anzahl<10:
        x = FensterBreite-(Blockgroesse*xPosition_Mulitplikator)+30
    else:
        x = FensterBreite-(Blockgroesse*xPosition_Mulitplikator)+20

    font = pygame.font.SysFont('Arial', 18) 
    render = font.render(str(Anzahl),True,(255,255,255))
    return render,x,y

def Item_Am_Koerper(Bild,Rechts,Blockgroesse,X_Pos_Block,Y_Pos_Block,Beruehren,Draw_Hintergrund):
    x,y = -100,-100
    # Bild Verkleinern
    Bild = pygame.transform.scale(Bild,(int(Blockgroesse/1.2),int(Blockgroesse/1.2)))
    # Wenn Links Bild Spiegeln
    
    if Rechts == False:
        Im_Block = pygame.draw.rect(Draw_Hintergrund,(0,0,0),(X_Pos_Block-int(Blockgroesse/1.3),Y_Pos_Block-int(Blockgroesse/2),int(Blockgroesse/2),int(Blockgroesse/2)))
        if Im_Block.collidelist(Beruehren)==-1:
            Bild = pygame.transform.flip(Bild,True,False)
            x = X_Pos_Block-int(Blockgroesse/1.3)
            y = Y_Pos_Block-int(Blockgroesse/2)
    else:
        Im_Block = pygame.draw.rect(Draw_Hintergrund,(0,0,0),(X_Pos_Block+int(Blockgroesse/1.3),Y_Pos_Block-int(Blockgroesse/2),int(Blockgroesse/2),int(Blockgroesse/2)))
        if Im_Block.collidelist(Beruehren)==-1:
            x = X_Pos_Block+int(Blockgroesse/1.3)
            y = Y_Pos_Block-int(Blockgroesse/2)


    return Bild,x,y