from random import randint
import pygame
import klassen
import random


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
    Added = False
    for i in Item_Liste:
        if i.Gegenstandsart == Blockart and Added==False:
            # Wenn das Item schon im Inventar ist einen hinzufügen
            print(Item_Liste[z].AnzahlCheck())
            if not Item_Liste[z].Anzahl == Item_Liste[z].StackgroesseMax:
                Item_Liste[z].Anzahl +=1
                Added=True
        # Neues Item erstellen und ins Inventar hinzufügen
        elif  Added == False:
            if Blockart == "Bruchstein":
                Item = klassen.Bruchstein_GS(1,False,100)
            elif Blockart == "Erde" or Blockart == "Gras":
                Item = klassen.Erde_GS(1,True,2)
            elif Blockart == "Eiche":
                Item = klassen.Eiche_GS(1,False,2)
            elif Blockart == "Birke":
                Item = klassen.Birke_GS(1,False,2)
            elif Blockart == "Diamant":
                Item = klassen.Diamant_GS(1,False,3)
            elif Blockart == "Eisen":
                Item = klassen.Eisen_GS(1,False,2)
            elif Blockart == "Gold":
                Item = klassen.Gold_GS(1,False,2)
            try:
                Item.Verbrauchdauer()
                Item.AnzahlCheck()
                Item_Liste.append(Item)
                Added = True
            except:
                print("Fehler: Block zu Gegenstand")
        z+=1


    return Item_Liste

"""eins = klassen.Gold(2,2)
Inv1 = klassen.Eisen_GS(1,False,20)
Inv2 = klassen.Eisen_GS(1,False,3)

Inv1.AnzahlCheck()
Inv1.Verbrauchdauer()

ki = [Inv1,Inv2]
print(Block_zu_Gegenstand(eins.Blockart,ki)[2])"""
