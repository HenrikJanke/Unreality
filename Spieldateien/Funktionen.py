from random import randint
import pygame
import klassen as k
import klassen
import random
import sys
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
        try:
            Item.Verbrauchdauer()
            Item.AnzahlCheck()
            Item_Liste.append(Item)
            Added = True
            #break
        except:
            pass
        Blockart = "Fertig"

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

def Startsequenz(Fenster,button_farbe_normal,schrift_farbe_normal,start_button_breite,start_button_hoehe,FensterBreite,FensterHoehe,Versteckter_monitor,maus_x,maus_y,Links_klick,Blockgroesse):
    # Wichtige Variablen und Einstellungen einstellen
    Formen_lokal = []
    dict_lokal = []
    Grafiken = BilderLaden(Blockgroesse)
    Gras = Grafiken[1]
    Eisen = Grafiken[2]
    Gold = Grafiken[3]
    Diamant = Grafiken[4]
    font_Start = pygame.font.SysFont('Arial', 40)
    font_unreality = pygame.font.SysFont('Arial', 120)
    Phantom_fenster = pygame.draw.rect(Versteckter_monitor,(button_farbe_normal),(FensterBreite/2-int(start_button_breite/2),FensterHoehe/2+start_button_hoehe,start_button_breite,start_button_hoehe))
    Mauszeiger = pygame.draw.rect(Versteckter_monitor,(0,0,0),(maus_x,maus_y,10,10))
    

    # Invertierte Farbe
    Font_farbe_kopie = schrift_farbe_normal
    button_farbe_kopie = button_farbe_normal
    if Mauszeiger.colliderect(Phantom_fenster):
        schrift_farbe_normal = button_farbe_normal
        button_farbe_normal = Font_farbe_kopie
    else:
        schrift_farbe_normal = Font_farbe_kopie
        button_farbe_normal = button_farbe_kopie
    # Darstellen der Gegenstände
    Start_rect = pygame.draw.rect(Fenster,(button_farbe_normal),(FensterBreite/2-int(start_button_breite/2),FensterHoehe/2+start_button_hoehe,start_button_breite,start_button_hoehe))
    start_schrift = font_Start.render("START",True,(schrift_farbe_normal))
    Unreality_schrift = font_unreality.render("UNREALITY",True,(button_farbe_kopie))
    Fenster.blit(start_schrift,(FensterBreite/2-int(start_button_breite/2)+35,FensterHoehe/2+start_button_hoehe))
    Fenster.blit(Unreality_schrift,(200,180))

    # Ausschmückungen an den Rändern erstellen
    # UntenLinks
    for i in range(1,5):
        r1_y= FensterHoehe
        if i == 1:
            r1_x = 0
            r2_x = Blockgroesse
            r3_x = r2_x+Blockgroesse
            r4_x = r2_x+Blockgroesse*2
        if i == 2:
            r1_x = FensterBreite-Blockgroesse
            r2_x = FensterBreite-Blockgroesse*2
            r3_x = FensterBreite-Blockgroesse*3
            r4_x = FensterBreite-Blockgroesse*4
        if i == 3:
            r1_y = 0
            r1_x = 0
            r2_x = Blockgroesse
            r3_x = r2_x+Blockgroesse
            r4_x = r2_x+Blockgroesse*2
        if i == 4:
            r1_y = 0
            r1_x = FensterBreite-Blockgroesse
            r2_x = FensterBreite-Blockgroesse*2
            r3_x = FensterBreite-Blockgroesse*3
            r4_x = FensterBreite-Blockgroesse*4
        if i in [1,2]:
            dict_lokal.append(k.Diamant(r1_x,r1_y-Blockgroesse))
            dict_lokal.append(k.Gold(r1_x,r1_y-Blockgroesse*2))
            dict_lokal.append(k.Eisen(r1_x,r1_y-Blockgroesse*3))
            dict_lokal.append(k.Erde(r1_x,r1_y-Blockgroesse*4))
            dict_lokal.append(k.Eisen(r2_x,r1_y-Blockgroesse))
            dict_lokal.append(k.Diamant(r2_x,r1_y-Blockgroesse*2))
            dict_lokal.append(k.Erde(r2_x,r1_y-Blockgroesse*3))
            dict_lokal.append(k.Gold(r3_x,r1_y-Blockgroesse))
            dict_lokal.append(k.Erde(r3_x,r1_y-Blockgroesse*2))
            dict_lokal.append(k.Erde(r4_x,r1_y-Blockgroesse))
        elif i in [3,4]:
            dict_lokal.append(k.Diamant(r1_x,r1_y))
            dict_lokal.append(k.Gold(r1_x,r1_y+Blockgroesse*1))
            dict_lokal.append(k.Eisen(r1_x,r1_y+Blockgroesse*2))
            dict_lokal.append(k.Erde(r1_x,r1_y+Blockgroesse*3))
            dict_lokal.append(k.Eisen(r2_x,r1_y))
            dict_lokal.append(k.Diamant(r2_x,r1_y+Blockgroesse*1))
            dict_lokal.append(k.Erde(r2_x,r1_y+Blockgroesse*2))
            dict_lokal.append(k.Gold(r3_x,r1_y))
            dict_lokal.append(k.Erde(r3_x,r1_y+Blockgroesse*1))
            dict_lokal.append(k.Erde(r4_x,r1_y))
    # Ausschmückungen an den Rändern in Bilder umformen
    for i in dict_lokal:
        # Blöcke pro Durchgang hinzufügen
        Formen_lokal.append(i)   
        # Grafik der Blockart an den Punkt hinzufügen
        if i.Blockart == 'Gras':
            Fenster.blit(Gras,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Eisen':
            Fenster.blit(Eisen,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Gold':
            Fenster.blit(Gold,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Diamant':
            Fenster.blit(Diamant,(i.xPosition,i.yPosition))
    
    # Abbruchkriterium um Ins Hauptspiel zu kommen
    if Mauszeiger.colliderect(Phantom_fenster) and Links_klick == True:
        return 1
    else:
        return 0

def Esape_menu(Fenster,maus_x,maus_y,Verstecktes_fenster,schrift_rot,schrift_weiß,Links_klick,Regen_an, Regen_Geschwindigkeit, Musik_an,FensterBreite,FensterHoehe,Blockgroesse,Auswahl):
    schrift_rot_kopie = schrift_rot
    schrift_weiß_kopie = schrift_weiß
    Formen_lokal = []
    dict_lokal = []
    Grafiken = BilderLaden(Blockgroesse)
    Gras = Grafiken[1]
    Eisen = Grafiken[2]
    Gold = Grafiken[3]
    Diamant = Grafiken[4]

    Spielsequenz = 2
    for event in pygame.event.get():
        # Schließen initialisieren  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Links_klick = True
            else:
                Links_klick = False


    Mauszeiger = pygame.draw.rect(Verstecktes_fenster,(0,0,0),(maus_x,maus_y,10,10))
    Font = pygame.font.SysFont('Arial', 32)

    # Escape Fenster
    Escape_Fenster = pygame.draw.rect(Fenster,schrift_weiß,(20,20,160,40))
    Escape_Schrift = Font.render("ZURÜCK",True,(schrift_rot))
    if Mauszeiger.colliderect(Escape_Fenster):
        Escape_Fenster = pygame.draw.rect(Fenster,schrift_rot,(20,20,160,40))
        Escape_Schrift = Font.render("ZURÜCK",True,(schrift_weiß))
    Fenster.blit(Escape_Schrift,(30,23))
    # Übergabe des Klickens
    if Mauszeiger.colliderect(Escape_Fenster) and Links_klick == True:
        Spielsequenz = 1

    # Regen Ausschalten
    Regen_aus = pygame.draw.rect(Fenster,schrift_weiß,(200,200,220,40))
    Regen_aus_Schrift = Font.render("Regen ist an",True,(schrift_rot))
    if Regen_an == False:
        Regen_aus = pygame.draw.rect(Fenster,schrift_rot,(200,200,220,40))
        Regen_aus_Schrift = Font.render("Regen ist aus",True,(schrift_weiß))
    Fenster.blit(Regen_aus_Schrift,(210,200))
    if Mauszeiger.colliderect(Regen_aus) and Links_klick == True:
        if Regen_an == True:
            Regen_an = False
        else:
            Regen_an = True
        
    # Musik Ausschalten
    Musik_aus = pygame.draw.rect(Fenster,schrift_weiß,(600,200,220,40))
    Musik_aus_Schrift = Font.render("Musik ist an",True,(schrift_rot))
    if Musik_an == False:
        Musik_aus = pygame.draw.rect(Fenster,schrift_rot,(600,200,220,40))
        Musik_aus_Schrift = Font.render("Musik ist aus",True,(schrift_weiß))
    Fenster.blit(Musik_aus_Schrift,(620,200))
    if Mauszeiger.colliderect(Musik_aus) and Links_klick == True:
        if Musik_an == True:
            Musik_an = False
        else:
            Musik_an = True

    # Exit
    Exit = pygame.draw.rect(Fenster,schrift_weiß,(450,400,100,40))
    Exit_Schrift = Font.render("EXIT",True,(schrift_rot))
    if Mauszeiger.colliderect(Exit):
        Exit = pygame.draw.rect(Fenster,schrift_rot,(450,400,100,40))
        Exit_Schrift = Font.render("EXIT",True,schrift_weiß)
    Fenster.blit(Exit_Schrift,(465,400))
    if Mauszeiger.colliderect(Exit) and Links_klick == True:
        sys.exit()
    
    # Blöcke an der Seite
    for i in range(1,5):
        r1_y= FensterHoehe
        if i == 1:
            r1_x = 0
            r2_x = Blockgroesse
            r3_x = r2_x+Blockgroesse
            r4_x = r2_x+Blockgroesse*2
        if i == 2:
            r1_x = FensterBreite-Blockgroesse
            r2_x = FensterBreite-Blockgroesse*2
            r3_x = FensterBreite-Blockgroesse*3
            r4_x = FensterBreite-Blockgroesse*4
        if i == 4:
            r1_y = 0
            r1_x = FensterBreite-Blockgroesse
            r2_x = FensterBreite-Blockgroesse*2
            r3_x = FensterBreite-Blockgroesse*3
            r4_x = FensterBreite-Blockgroesse*4
        if i in [1,2]:
            dict_lokal.append(k.Diamant(r1_x,r1_y-Blockgroesse))
            dict_lokal.append(k.Gold(r1_x,r1_y-Blockgroesse*2))
            dict_lokal.append(k.Eisen(r1_x,r1_y-Blockgroesse*3))
            dict_lokal.append(k.Erde(r1_x,r1_y-Blockgroesse*4))
            dict_lokal.append(k.Eisen(r2_x,r1_y-Blockgroesse))
            dict_lokal.append(k.Diamant(r2_x,r1_y-Blockgroesse*2))
            dict_lokal.append(k.Erde(r2_x,r1_y-Blockgroesse*3))
            dict_lokal.append(k.Gold(r3_x,r1_y-Blockgroesse))
            dict_lokal.append(k.Erde(r3_x,r1_y-Blockgroesse*2))
            dict_lokal.append(k.Erde(r4_x,r1_y-Blockgroesse))
        elif i == 4:
            dict_lokal.append(k.Diamant(r1_x,r1_y))
            dict_lokal.append(k.Gold(r1_x,r1_y+Blockgroesse*1))
            dict_lokal.append(k.Eisen(r1_x,r1_y+Blockgroesse*2))
            dict_lokal.append(k.Erde(r1_x,r1_y+Blockgroesse*3))
            dict_lokal.append(k.Eisen(r2_x,r1_y))
            dict_lokal.append(k.Diamant(r2_x,r1_y+Blockgroesse*1))
            dict_lokal.append(k.Erde(r2_x,r1_y+Blockgroesse*2))
            dict_lokal.append(k.Gold(r3_x,r1_y))
            dict_lokal.append(k.Erde(r3_x,r1_y+Blockgroesse*1))
            dict_lokal.append(k.Erde(r4_x,r1_y))
    # Ausschmückungen an den Rändern in Bilder umformen
    for i in dict_lokal:
        # Blöcke pro Durchgang hinzufügen
        Formen_lokal.append(i)   
        # Grafik der Blockart an den Punkt hinzufügen
        if i.Blockart == 'Gras':
            Fenster.blit(Gras,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Eisen':
            Fenster.blit(Eisen,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Gold':
            Fenster.blit(Gold,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Diamant':
            Fenster.blit(Diamant,(i.xPosition,i.yPosition))

    return Spielsequenz, Regen_an, Regen_Geschwindigkeit, Musik_an,Auswahl
  