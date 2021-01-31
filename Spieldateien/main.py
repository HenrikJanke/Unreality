import pygame
import sys
from random import randint
import klassen

import Funktionen
import time
import WorldGenerator

# Rahmendaten
FensterBreite,FensterHoehe = 1024,576
Blockgroesse = Funktionen.Blockgroesse(FensterBreite,FensterHoehe)
BreiteinBloecken = Funktionen.LaengeInBloecken(FensterBreite,FensterHoehe)
HoeheInBloecken = Funktionen.HoeheInBloecken(FensterBreite,FensterHoehe)
dict = WorldGenerator.Generator(Blockgroesse,FensterHoehe,FensterBreite,HoeheInBloecken,BreiteinBloecken)

x,y = (randint(1,31))*Blockgroesse,Blockgroesse*4
Frames = 60

# Speilmechanik Variablen
Geschwindigkeit= 3
Sprungintensitaet, Sprung,Sprungverbot, zaehler = -16,False,False,0
Linkserlaubnis,Rechtserlaubnis,Obenerlaubnis = False,False,False
Links_klick, Inv_Pointer = False,1
HoverX, HUD_Aktiv = 0, True
Schwert = klassen.Schwert(1,True)
Spitzhacke = klassen.Spitzhacke(1,True)
Inventar, InventarBilder = [Schwert,Spitzhacke],[]
RechtsBewegung = True




# Grafisch/Audische Variablen
pygame.init()
pygame.font.init()

# alle Bilder laden
Grafiken = Funktionen.BilderLaden(Blockgroesse)
Erde = Grafiken[0]
Gras = Grafiken[1]
Eisen = Grafiken[2]
Gold = Grafiken[3]
Diamant = Grafiken[4]
Eiche = Grafiken[5]
Birke = Grafiken[6]
Bruchstein = Grafiken[7]
ReinerStein = Grafiken[8]
Blaetter = Grafiken[9]

# Alle Gegenstände Laden
GS_Laden = Funktionen.GegenstaendeLaden(Blockgroesse)
GS_Erde = Erde
GS_Eisen = Eisen
GS_Gold = Gold
GS_Diamant = Diamant
GS_Eiche = Eiche
GS_Birke = Birke
GS_Bruchstein = Bruchstein
GS_Spitzhacke = GS_Laden[0]
GS_Schwert = GS_Laden[1]



Fenster = pygame.display.set_mode((FensterBreite,FensterHoehe))
FigurIMG = pygame.image.load('Data\Spieler\Figur.png')
pygame.display.set_caption("Unreality")
Startbild = pygame.image.load("Data\Grafiken\Icon\Icon.png")
pygame.display.set_icon(Startbild)
fps = pygame.time.Clock()
Hintergrund = pygame.image.load("Data\Grafiken\Hintergrund\Hintergrund.png")
GuiOverlay = pygame.image.load("Data\Grafiken\Gui\Overlay\Overlay.png")
GuiOverlay = pygame.transform.scale(GuiOverlay,(Blockgroesse*12,Blockgroesse*2))
Hover = pygame.image.load("Data\Grafiken\Gui\Overlay\Hover.png")
Hover = pygame.transform.scale(Hover,(Blockgroesse*2,Blockgroesse*2))
Sprunghilfe = pygame.Surface((FensterBreite,FensterHoehe)) 
Sprunghilfe.set_alpha(0)
pygame.mouse.set_visible(False)
coursor_Farbe_Default = (0,0,0)
coursor_Farbe = coursor_Farbe_Default


# Hintergrund Musik
pygame.mixer.init()
pygame.mixer.music.load("Data\Musik\Sound of Rain.mp3")
pygame.mixer.music.play()
Lautstaerke = pygame.mixer.music.get_volume()
if Lautstaerke >= 0.95:
    pygame.mixer.music.set_volume(Lautstaerke-0.96)

while True:
    # Formen und Inventarr auf der Karte zurücksetzen
    Formen =[]
    InventarBilder = []
    
    # Inventar mit den Mausrad durchgehen
    if Inv_Pointer < 1:
        Inv_Pointer = 6
    elif Inv_Pointer > 6:
        Inv_Pointer = 1

    # Spieler Objekt erzeugen  
    Spieler = klassen.Spieler(1,'Ben',2,100,int(x),int(y-(Blockgroesse*2)),Blockgroesse-4,Blockgroesse*3,'Nichts',0,'Nichts',0,'Nichts',0,'Nichts',0,'Nichts',0,'Nichts',0,Inv_Pointer)

    #Schwarzer Hintergrund und das Hintergrundbild sowie die Hilfsstruktur
    Fenster.fill((0,0,0))
    Fenster.blit(Hintergrund,(0,0))

    for event in pygame.event.get():
        # Schließen initialisieren  
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Links_klick = True
            # Mit Mausrad durch das Inventar gehen
            elif event.button == 5:
                Inv_Pointer -= 1
            elif event.button == 4:
                Inv_Pointer += 1
        # Wenn Taste I gedrückt dann das Inventar öffnen
        if event.type == pygame.KEYDOWN:
            # Wegwerfen von Items Taste Q
            if event.key == pygame.K_q:
                try:
                    Inventar.pop(Inv_Pointer-1)
                except:
                    pass
                    

    # Objekte als Formen umgesetzt und danach der Liste Formen hinzugefügt
    for i in dict:
        k = pygame.draw.rect(Sprunghilfe,i.Farbe,(i.xPosition,i.yPosition,Blockgroesse,Blockgroesse))
        # Blöcke pro Durchgang hinzufügen
        Formen.append(k)   
        # Grafik der Blockart an den Punkt hinzufügen
        if i.Blockart == 'Erde':
            Fenster.blit(Erde,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Gras':
            Fenster.blit(Gras,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Eisen':
            Fenster.blit(Eisen,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Gold':
            Fenster.blit(Gold,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Diamant':
            Fenster.blit(Diamant,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Eiche':
            Fenster.blit(Eiche,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Birke':
            Fenster.blit(Birke,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Bruchstein':
            Fenster.blit(Bruchstein,(i.xPosition,i.yPosition))
        elif i.Blockart == 'ReinerStein':
            Fenster.blit(ReinerStein,(i.xPosition,i.yPosition))
        elif i.Blockart == 'Blaetter':
            Fenster.blit(Blaetter,(i.xPosition,i.yPosition))



    #Spielfigur zeichnen  rect(Fenster,Farbe,(x,y,Breite,Hoehe))
    Figur = pygame.draw.rect(Sprunghilfe,(200,55,55),(Spieler.x,Spieler.y,Spieler.Breite,Spieler.Hoehe))    
    Fenster.blit(FigurIMG,(Spieler.x,Spieler.y))
    # Erstellen eines viereckes über der Spielfigur was Transparent ist und für die Sprungbedingung benutzt wird. 
    SprungCheckFigur = pygame.draw.rect(Sprunghilfe,(0,0,0),(int(Spieler.x)+0.5,int(Spieler.y)-2,int(Spieler.Breite)-2,Blockgroesse/10))
    #LinkscheckFigur das es nicht in ein Block reinlaufen oder reinspringen kann
    LinksCheckFigur = pygame.draw.rect(Sprunghilfe,(0,0,0),((Spieler.x)-0.5,Spieler.y,Blockgroesse/10,int(Spieler.Hoehe)-5))
    #RechtsCheckFigur das es nicht in ein Block reinlaufen oder reinspringen kann
    RechtsCheckFigur = pygame.draw.rect(Sprunghilfe,(0,0,0),((Spieler.x)+int(Blockgroesse/1.16),Spieler.y,Blockgroesse/18,Blockgroesse*2.9))
    #UntencheckFigur das es nicht durch einen Block durchfällt
    UntenCheckFigur = pygame.draw.rect(Sprunghilfe,(0,0,0),(int(Spieler.x)+Blockgroesse/2,y+Blockgroesse-(Blockgroesse/10),1,Blockgroesse/10))

   # Mausposition
    MausX, MausY = pygame.mouse.get_pos()
    #AbbauHintergrundCheck ob es in der Möglichen umkreis ist wo es abgebaut werden kann
    AbbauHintergrundCheck = pygame.draw.rect(Sprunghilfe,(255,200,0),(Spieler.x-Blockgroesse*2,Spieler.y-Blockgroesse,Blockgroesse*5,Blockgroesse*4.85))
    # Individueller Mauszeiger
    Verrtikal = pygame.draw.rect(Fenster,(coursor_Farbe),(MausX-1,MausY-7,2,14))
    Horizontal = pygame.draw.rect(Fenster,(coursor_Farbe),(MausX-7,MausY-1,14,2))
    # Wird Benutzt, da ein Fehler auftritt wenn das Fadenkreuz genutzt wird
    Neuer_Cursor = pygame.draw.rect(Sprunghilfe,(coursor_Farbe),(MausX-1,MausY-1,2,2))
    #Farbe des coursors ändern wenn es in einen möglichen Block ist der abgebaut werden kann
    if AbbauHintergrundCheck.colliderect(Neuer_Cursor):
        coursor_Farbe = (255,0,0)
    else:
        coursor_Farbe = coursor_Farbe_Default



    # Abbauen des Blockes wenn Links gedrückt und wenn Neuer_Cursor in AbbauhintergrundCheck ist
    if Neuer_Cursor.collidelist(Formen)!=-1 and AbbauHintergrundCheck.colliderect(Neuer_Cursor)==True and Links_klick == True:
        # Herausfinden des Objektes um die Abbaukraft und die Stärke des Blockes herauszufinden sowie Später die item zugabe
        Block = dict[Neuer_Cursor.collidelist(Formen)]
        # Ausgabe der Blockart des Objektes, stellt da das ein Objekt gelöscht wird wodurch später items für das Inventar gemacht werden können sowie die Abbaudauer
        Inventar = Funktionen.Block_zu_Gegenstand(Block.Blockart,Inventar)
        # an der Stelle Block wird der Block aus der Liste entfernt, möglicher Stackunderflow
        dict.pop(Neuer_Cursor.collidelist(Formen))
    else:
        Links_klick = False
    # InventarBilder erstellen
    for i in Inventar:
        Zahl = i.Anzahl
        i = i.Gegenstandsart
        if i == "Bruchstein":
            InventarBilder.append(GS_Bruchstein)
        elif i == "Erde":
            InventarBilder.append(GS_Erde)
        elif i == "Eiche":
            InventarBilder.append(GS_Eiche)
        elif i == "Birke":
            InventarBilder.append(GS_Birke)
        elif i == "Diamant":
            InventarBilder.append(GS_Diamant)
        elif i == "Eisen":
            InventarBilder.append(GS_Eisen)
        elif i == "Gold":
            InventarBilder.append(GS_Gold)
        elif i == "Schwert":
            InventarBilder.append(GS_Schwert)
        elif i == "Spitzhacke":
            InventarBilder.append(GS_Spitzhacke)
    
    # Anzeige der Items am Körper
    if not Inventar == []:
        try:
            Bild_Koerper,X_Bild,Y_Bild = Funktionen.Item_Am_Koerper(InventarBilder[Inv_Pointer-1],RechtsBewegung,Blockgroesse,x,y,Formen,Sprunghilfe) 
            Fenster.blit(Bild_Koerper,(X_Bild,Y_Bild))
        except:
            pass

    # Wenn I gedrückt
    if HUD_Aktiv == True:
        Fenster.blit(GuiOverlay,((FensterBreite-(Blockgroesse*12.5)),Blockgroesse/2))
        # GUI Hover
        if Inv_Pointer == 1:
            HoverX = 0
        else:
            HoverX = (Inv_Pointer-1)*2
        # Anzeige in Welcher Position man ist
        Fenster.blit(Hover,((FensterBreite-(Blockgroesse*12.5))+HoverX*Blockgroesse,Blockgroesse/2))
        # Inventar Testwerte
        if not Inventar == []:
            # Erste Position
            Fenster.blit(InventarBilder[0],((FensterBreite-(Blockgroesse*12),Blockgroesse)))
            Render,X_Inv,Y_Inv = Funktionen.Item_Anzahl_Schrift(Inventar,0,Blockgroesse,12,FensterBreite)
            Fenster.blit(Render,(X_Inv,Y_Inv))
            # Zweite Position
            try:
                Fenster.blit(InventarBilder[1],((FensterBreite-(Blockgroesse*10),Blockgroesse)))
                Render,X_Inv,Y_Inv = Funktionen.Item_Anzahl_Schrift(Inventar,1,Blockgroesse,10,FensterBreite)
                Fenster.blit(Render,(X_Inv,Y_Inv))
            except:
                pass
            # Dritte Position
            try:
                Fenster.blit(InventarBilder[2],((FensterBreite-(Blockgroesse*8),Blockgroesse)))
                Render,X_Inv,Y_Inv = Funktionen.Item_Anzahl_Schrift(Inventar,2,Blockgroesse,8,FensterBreite)
                Fenster.blit(Render,(X_Inv,Y_Inv))
            except:
                pass
            # Vierte Position
            try:
                Fenster.blit(InventarBilder[3],((FensterBreite-(Blockgroesse*6),Blockgroesse)))
                Render,X_Inv,Y_Inv = Funktionen.Item_Anzahl_Schrift(Inventar,3,Blockgroesse,6,FensterBreite)
                Fenster.blit(Render,(X_Inv,Y_Inv))
            except:
                pass
            # Fünfte Position
            try:
                Fenster.blit(InventarBilder[4],((FensterBreite-(Blockgroesse*4),Blockgroesse)))
                Render,X_Inv,Y_Inv = Funktionen.Item_Anzahl_Schrift(Inventar,4,Blockgroesse,4,FensterBreite)
                Fenster.blit(Render,(X_Inv,Y_Inv))
            except:
                pass
            # Sechste Position
            try:
                Fenster.blit(InventarBilder[5],((FensterBreite-(Blockgroesse*2),Blockgroesse)))
                Render,X_Inv,Y_Inv = Funktionen.Item_Anzahl_Schrift(Inventar,5,Blockgroesse,2,FensterBreite)
                Fenster.blit(Render,(X_Inv,Y_Inv))
            except:
                pass




    # Tastenanschläge bekommen Variable defenieren
    TastenAbfangen = pygame.key.get_pressed()    
    # Rechtsbewegung
    if RechtsCheckFigur.collidelist(Formen)!=-1:
        #Check ob es in einen Blcok steht damit es nach links noch gehen kann
        Rechtserlaubnis = False
        if UntenCheckFigur.collidelist(Formen)==-1 and not y+Blockgroesse>FensterHoehe:
            y+=Geschwindigkeit
    if TastenAbfangen[pygame.K_d]:
        if not x>FensterBreite-Blockgroesse and Figur.collidelist(Formen)==-1 or Rechtserlaubnis==True :
            if not x>FensterBreite-Blockgroesse:
                RechtsBewegung = True
                x+=Geschwindigkeit

            Sprungverbot = False
            Rechtserlaubnis = False
            Linkserlaubnis = True
   
    # Linksbewegung
    if LinksCheckFigur.collidelist(Formen)!=-1:
        Linkserlaubnis= False
        if UntenCheckFigur.collidelist(Formen)==-1 and not y+Blockgroesse>FensterHoehe:
            y+=Geschwindigkeit
    if TastenAbfangen[pygame.K_a]:
        if not x<0 and Figur.collidelist(Formen)==-1 or Linkserlaubnis==True:
            if not x<0:
                RechtsBewegung = False
                x-=Geschwindigkeit
            Sprungverbot=False
            Rechtserlaubnis = True
            Linkserlaubnis=False

    # Konstantes Fallen
    if Figur.collidelist(Formen)==-1 and not y+(Blockgroesse)>FensterHoehe:
        y+=Geschwindigkeit
        zaehler +=1
    
    # Bewegung auf dem Block 
    elif Figur.collidelist(Formen)>=0 and not y+(Blockgroesse)>FensterHoehe:
        Rechtserlaubnis = True
        Linkserlaubnis = True
    
    # zaehler rücksetzung wenn an Block, wichtig für Sprung
    if Figur.collidelist(Formen)>=0 or y+(Blockgroesse)>FensterHoehe:
        zaehler = 0

    # Springen / nur hoch animation, da das Fallen die runteranimation ist
    if TastenAbfangen[pygame.K_SPACE] and Sprungintensitaet == -16 and zaehler == 0 and  SprungCheckFigur.collidelist(Formen)==-1 and Sprungverbot == False:
        Sprungintensitaet = 11
    if Sprungintensitaet >= 0 :
        n = 1
        if  SprungCheckFigur.collidelist(Formen)==-1:
            y -= (Sprungintensitaet**2)*0.16*n
        else:
            y += Geschwindigkeit
        Sprungintensitaet -= 1
    if Sprungintensitaet == 0:
        Sprungintensitaet = -16            
    if Sprungverbot == True and Sprungintensitaet == -16:
        Sprungverbot = False
    #Updaten des Bildschirms, da vorher was verändert wurde
    pygame.display.update()
    #Regulierung auf 60 Bilder Pro sekunde
    fps.tick(Frames)