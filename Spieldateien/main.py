import pygame
import sys
from random import randint
import klassen
import time
import math
import Funktionen
import time
import WorldGenerator

# Rahmendaten
FensterBreite,FensterHoehe = 1024,576
Blockgroesse = Funktionen.Blockgroesse(FensterBreite,FensterHoehe)
BreiteinBloecken = Funktionen.LaengeInBloecken(FensterBreite,FensterHoehe)
HoeheInBloecken = Funktionen.HoeheInBloecken(FensterBreite,FensterHoehe)
dict = WorldGenerator.Generator(Blockgroesse,FensterHoehe,FensterBreite,HoeheInBloecken,BreiteinBloecken)
x,y = (randint(1,31))*Blockgroesse,-50
Frames = 60
Geschwindigkeit= 3

# Speilmechanik Variablen
Sprungintensitaet, Sprung,Sprungverbot, zaehler = -16,False,False,0
Linkserlaubnis,Rechtserlaubnis,Obenerlaubnis = False,False,False
Links_klick, Inv_Pointer = False,1
Rechts_klick = False
HoverX, HUD_Aktiv = 0, True
Schwert = klassen.Schwert(1,True)
Spitzhacke = klassen.Spitzhacke(1,True)
Inventar, InventarBilder = [Schwert,Spitzhacke],[]
RechtsBewegung = True
Aus_Dem_Bildschirm = False
Rechts_Behinderung, Links_Behinderung = False,False
Erst_Kontakt = -10
Abbau, Abbaukraft_Bekommen, Abbau_Pos  = True, False, False
Klick_Rate = 0
Regen,tropfen_anzahl  = [], 0
Regen_an, Regen_Geschwindigkeit, Musik_an,Auswahl = True, 0.5, True,1

# Pygame initialisieren
pygame.init()
pygame.font.init()

# Pygame Einstellungen zum Personalisieren des Spiels
Fenster = pygame.display.set_mode((FensterBreite,FensterHoehe))
FigurIMG = pygame.image.load('Data\Spieler\Figur.png')
pygame.display.set_caption("Unreality")
Startbild = pygame.image.load("Data\Grafiken\Icon\Icon.png")
pygame.display.set_icon(Startbild)
fps = pygame.time.Clock()
Sprunghilfe = pygame.Surface((FensterBreite,FensterHoehe)) 
Sprunghilfe.set_alpha(0)
coursor_Farbe_Default = (0,0,0)
coursor_Farbe = coursor_Farbe_Default
Spielsequenz = 0

# Alle Grafiken und Verschönerungen (Regen, Bilder, Inventar)
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
# Alle Abbaustadien laden 
Abbau_Null = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_9.png")
Abbau_Null = pygame.transform.scale(Abbau_Null,(Blockgroesse,Blockgroesse))
Abbau_Eins = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_8.png")
Abbau_Eins = pygame.transform.scale(Abbau_Eins,(Blockgroesse,Blockgroesse))
Abbau_Zwei = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_7.png")
Abbau_Zwei = pygame.transform.scale(Abbau_Zwei,(Blockgroesse,Blockgroesse))
Abbau_Drei = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_6.png")
Abbau_Drei = pygame.transform.scale(Abbau_Drei,(Blockgroesse,Blockgroesse))
Abbau_Vier = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_5.png")
Abbau_Vier = pygame.transform.scale(Abbau_Vier,(Blockgroesse,Blockgroesse))
Abbau_Fuenf = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_4.png")
Abbau_Fuenf = pygame.transform.scale(Abbau_Fuenf,(Blockgroesse,Blockgroesse))
Abbau_Sechs = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_3.png")
Abbau_Sechs = pygame.transform.scale(Abbau_Sechs,(Blockgroesse,Blockgroesse))
Abbau_Sieben = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_2.png")
Abbau_Sieben = pygame.transform.scale(Abbau_Sieben,(Blockgroesse,Blockgroesse))
Abbau_Acht = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_1.png")
Abbau_Acht = pygame.transform.scale(Abbau_Acht,(Blockgroesse,Blockgroesse))
Abbau_Neun = pygame.image.load("Data\Grafiken\Zerstören\destroy_stage_0.png")
Abbau_Neun = pygame.transform.scale(Abbau_Neun,(Blockgroesse,Blockgroesse))
Abbau_Animation = [Abbau_Null,Abbau_Eins,Abbau_Zwei,Abbau_Drei,Abbau_Vier,Abbau_Fuenf,Abbau_Sechs,Abbau_Sieben,Abbau_Acht,Abbau_Neun]
# Hintergrund Bild und Overlay
Hintergrund = pygame.image.load("Data\Grafiken\Hintergrund\Hintergrund.png")
GuiOverlay = pygame.image.load("Data\Grafiken\Gui\Overlay\Overlay.png")
GuiOverlay = pygame.transform.scale(GuiOverlay,(Blockgroesse*12,Blockgroesse*2))
Hover = pygame.image.load("Data\Grafiken\Gui\Overlay\Hover.png")
Hover = pygame.transform.scale(Hover,(Blockgroesse*2,Blockgroesse*2))
# Hintergrund Musik
pygame.mixer.init()
pygame.mixer.music.load("Data\Musik\Sound of Rain.mp3")
Musik, Musik_pausiert = False, False






while True:
     # Formen und Inventar auf der Karte zurücksetzen
    Formen =[]
    InventarBilder = []
    # Mauspositionen bekommen, um später damit zu Arbeiten
    m_x, m_y =  pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Schließen initialisieren  
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Links_klick = True
                Klick_Rate += 1
            # Rechtsklick
            elif event.button == 3:
                Rechts_klick = True
            # Mit Mausrad durch das Inventar gehen
            elif event.button == 5:
                Inv_Pointer -= 1
            elif event.button == 4:
                Inv_Pointer += 1
        # Wenn Taste Gedrückt
        if event.type == pygame.KEYDOWN:
            # Wegwerfen von Items Taste Q
            if event.key == pygame.K_q:
                try:
                    Inventar.pop(Inv_Pointer-1)
                except:
                    pass
            if event.key == pygame.K_ESCAPE:
                # In den Einstellungs Modus kommen
                if Spielsequenz == 1:
                    Spielsequenz = 2
    # Start Bildschirm
    if Spielsequenz == 0:
        Fenster.fill((0,0,0))
        Fenster.blit(Hintergrund,(0,0))
        start_button_breite = 200 
        start_button_hoehe = 50
        button_farbe_normal = (255,255,255)
        schrift_farbe_normal = (144,55,73)
        Spielsequenz = Funktionen.Startsequenz(Fenster,button_farbe_normal,schrift_farbe_normal,start_button_breite,start_button_hoehe,FensterBreite,FensterHoehe,Sprunghilfe,m_x,m_y,Links_klick,Blockgroesse)
        Links_klick = False
    
    # Einstellungen Modus
    elif Spielsequenz == 2:
        # Musik Pausieren wenn es im Escape Modus ist
        pygame.mixer.music.pause()
        Musik_pausiert = True
        Escape_Hintergrund = pygame.Surface((FensterBreite,FensterHoehe))
        Escape_Hintergrund.blit(Hintergrund,(0,0))
        # Mauszeiger wieder darstellen
        pygame.mouse.set_visible(True)
        Spielsequenz, Regen_an, Regen_Geschwindigkeit, Musik_an,Auswahl = Funktionen.Esape_menu(Escape_Hintergrund,m_x,m_y,Sprunghilfe,(144,55,73),(255,255,255),Links_klick,Regen_an, Regen_Geschwindigkeit, Musik_an,FensterBreite,FensterHoehe,Blockgroesse,Auswahl)
        Links_klick = False
        # Fenster mit den Aktuellen Escape Hintergrund updaten
        Fenster.blit(Escape_Hintergrund,(0,0))


    elif Spielsequenz == 1:
        # Wenn Musik nicht an ist aber an sein soll wird es angestellt
        if Musik == False and not Musik_an == False:
            pygame.mixer.music.play()
            Lautstaerke = pygame.mixer.music.get_volume()
            if Lautstaerke >= 0.95:
                pygame.mixer.music.set_volume(Lautstaerke-0.96)
            Musik = True
        # Musiker wird wieder angemacht, wenn es an sein soll
        if Musik_pausiert == True and not Musik_an == False:
            pygame.mixer.music.unpause()
            Musik_pausiert = False
        
        # Mauszeiger ausschalten, da Später ein eigener erstellt wird
        pygame.mouse.set_visible(False)

        # Inventar mit den Mausrad durchgehen
        if Inv_Pointer < 1:
            Inv_Pointer = 6
        elif Inv_Pointer > 6:
            Inv_Pointer = 1

        # Spieler Objekt erzeugen  
        Spieler = klassen.Spieler(1,'Ben',2,100,int(x),int(y-(Blockgroesse*2)),Blockgroesse-4,Blockgroesse*3,Inv_Pointer)

        #Schwarzer Hintergrund und das Hintergrundbild sowie die Hilfsstruktur
        Fenster.fill((0,0,0))
        Fenster.blit(Hintergrund,(0,0))

        # Regen erstellen und Regen entfernen, wenn es Aus dem Bildschirm ist
        if Regen_an == True:
            # Regen Im Hintergrund
            Verlangsamer = round(time.time())
            #Verlangsamer.round(1)
            for i in range (0,randint(1,2)):
                if Verlangsamer % randint(1,3) == 0:
                    Regen.append(klassen.Regen(FensterBreite,FensterHoehe))
            tropfen_anzahl = 0
            pop_zaehler = 0
            for i in Regen:
                if i.yPosition >= FensterHoehe:
                    Regen.pop(pop_zaehler)
                pop_zaehler +=1
                i.yPosition += Regen_Geschwindigkeit
            for i in Regen:
                pygame.draw.rect(Fenster,(255,255,255),(i.xPosition,i.yPosition,int(Blockgroesse/16),int(Blockgroesse/16)))
                tropfen_anzahl +=1
                        
        
        # Objekte als Formen umsetzen und danach der Liste Formen hinzugefügt
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
        Verrtikal = pygame.draw.rect(Fenster,(coursor_Farbe),(m_x-1,m_y-7,2,14))
        Horizontal = pygame.draw.rect(Fenster,(coursor_Farbe),(m_x-7,m_y-1,14,2))
        # Wird Benutzt, da ein Fehler auftritt wenn das Fadenkreuz genutzt wird
        Neuer_Cursor = pygame.draw.rect(Sprunghilfe,(coursor_Farbe),(m_x-1,m_y-1,2,2))
        #Farbe des coursors ändern wenn es in einen möglichen Block ist der abgebaut werden kann
        if AbbauHintergrundCheck.colliderect(Neuer_Cursor):
            coursor_Farbe = (255,0,0)
        else:
            coursor_Farbe = coursor_Farbe_Default

            

        # Abbauen des Blockes wenn Links gedrückt und wenn Neuer_Cursor in AbbauhintergrundCheck ist
        if Neuer_Cursor.collidelist(Formen)!=-1 and AbbauHintergrundCheck.colliderect(Neuer_Cursor)==True and Links_klick == True:
            # Uhr die die Zeit festhält, wenn was abgebaut wird
            Erst_Kontakt = math.floor(time.time())
            # Abbaukraft des Items, auf dem der Zeiger im inventar ist bekommen
            try:
                Iventar_Item_Abbaukraft = Inventar[Inv_Pointer-1].Abbaukraft
            except:
                Iventar_Item_Abbaukraft = 1
            # Herausfinden wie schwer es sein soll, das Item abzubauen
            Block = dict[Neuer_Cursor.collidelist(Formen)]
            # Abbaustärke des abzubauenden Blockes bekommen
            Abbau_Staerke = Block.Abbaukraft
            # Herausfinden ob der Zeiger immernoch auf dem Block ist, während er es abbaut
            Noch_Colidet = pygame.draw.rect(Sprunghilfe,(0,0,0),(Block.xPosition,Block.yPosition,Blockgroesse,Blockgroesse))
            # an der Stelle Block wird der Block aus der Liste entfernt, möglicher Stackunderflow
            Abbau = False
            Links_klick = False
            Abbaukraft_Bekommen = False
        else:
            Links_klick = False
        # Finaler Abbau mit Abbaukraft
        try:
            if Abbau_Pos == False:
                Block = dict[Neuer_Cursor.collidelist(Formen)]
                # Abbaustärke des abzubauenden Blockes bekommen
                Abbau_Staerke = Block.Abbaukraft
                Abbau_Pos = True
            # Herausfinden ob der Zeiger immernoch auf dem Block ist, während er es abbaut
            Noch_Colidet = pygame.draw.rect(Sprunghilfe,(0,0,0),(Block.xPosition,Block.yPosition,Blockgroesse,Blockgroesse))
            
            if not Abbau_Staerke-Iventar_Item_Abbaukraft<=0 and Abbau == False and Abbaukraft_Bekommen == False:
                Abbaudauer = Abbau_Staerke-Iventar_Item_Abbaukraft
                Abbaukraft_Bekommen = True
            elif Abbau == False and Abbau_Staerke-Iventar_Item_Abbaukraft<=0 and Abbaukraft_Bekommen == False:
                Abbaudauer = 1
                Abbaukraft_Bekommen = True

            # Abbauanimation
            if (Erst_Kontakt+Abbaudauer-math.floor(time.time()))>=-1 and Noch_Colidet.colliderect(Neuer_Cursor):
                Hilfe = Erst_Kontakt+Abbaudauer-math.floor(time.time())
                if Hilfe >= 9:
                    Hilfe = 9
                Fenster.blit(Abbau_Animation[Hilfe],(Block.xPosition,Block.yPosition))

            # Wenn die Zwei Sekunden abgelaufen sind und nicht vorher direkt abgebaut wurde, sowie der cursor noch im Item ist wird abbgebaut
            if Erst_Kontakt+Abbaudauer == math.floor(time.time()) and Abbau==False and Noch_Colidet.colliderect(Neuer_Cursor):
                dict.pop(Neuer_Cursor.collidelist(Formen))
                # item zum Inventar hinzufügen
                Inventar = Funktionen.Block_zu_Gegenstand(Block.Blockart,Inventar)
                Abbau_Pos = False
                Abbau = True
        except:
            pass
        
        # Bilder hinzufügen, von den Gegenständen die im Inventar sind
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
        
        # Endlosgehen
        # Erstellen von Vierecken bei den X "Schranken"
        Links_Schranke = pygame.draw.rect(Sprunghilfe,(0,0,0),(0,y,Blockgroesse/2,Blockgroesse/2))
        Rechts_Schranke = pygame.draw.rect(Sprunghilfe,(0,0,0),(FensterBreite-Blockgroesse,y,Blockgroesse/2,Blockgroesse/2))
        # Links aus dem Bildschirm
        if x<-Blockgroesse and Rechts_Schranke.collidelist(Formen)==-1:
            x = FensterBreite
            y-=5
            Aus_Dem_Bildschirm = True
        # Rechts aus dem Bildschirm
        elif x>FensterBreite and Links_Schranke.collidelist(Formen)==-1:
            y-=5
            x = 1
            Aus_Dem_Bildschirm = True
            Rechts_Behinderung = True
        # Nicht nach Links wenn dort ein Block ist
        elif Links_Schranke.collidelist(Formen)!=-1 and x>FensterBreite-Blockgroesse:
            x = FensterBreite-Blockgroesse
            Links_Behinderung = True
            Aus_Dem_Bildschirm = True
        # Nicht nach Rechts wenn dort ein Block steht
        elif Rechts_Schranke.collidelist(Formen)!=-1 and x <= 0:
            x = 0
            Rechts_Behinderung = True
            Aus_Dem_Bildschirm = True
        else:
            Aus_Dem_Bildschirm = False
            Rechts_Behinderung = False
            Links_Behinderung = False

        # Hier Platzieren einfügen (MausX, MausY)
        if Neuer_Cursor.collidelist(Formen)==-1 and AbbauHintergrundCheck.colliderect(Neuer_Cursor)==True and Rechts_klick == True:
            try:
                while MausX%Blockgroesse != 0:
                    MausX-=1
                while MausY%Blockgroesse != 0:
                    MausY-=1
                # Potenzieller Finaler Block, rect(Fenster,Farbe,(x,y,Breite,Hoehe))
                potenzieller_block = pygame.draw.rect(Sprunghilfe,(0,0,0),(MausX,MausY,Blockgroesse,Blockgroesse))
                # Blöcke die Testen ob Links, Rechts, Oben oder Unten ein anderer Block ist damit die sachen nicht in der Luft platizert werden können
                Links = pygame.draw.rect(Sprunghilfe,(0,0,0),(MausX-Blockgroesse,MausY,Blockgroesse,Blockgroesse))
                Rechts = pygame.draw.rect(Sprunghilfe,(0,0,0),(MausX+Blockgroesse,MausY,Blockgroesse,Blockgroesse))
                Oben = pygame.draw.rect(Sprunghilfe,(0,0,0),(MausX,(MausY-Blockgroesse),Blockgroesse,Blockgroesse))
                Unten = pygame.draw.rect(Sprunghilfe,(0,0,0),(MausX,MausY+Blockgroesse,Blockgroesse,Blockgroesse))
                if Links.collidelist(Formen)!=-1 or Rechts.collidelist(Formen)!=-1 or Oben.collidelist(Formen)!=-1 or Unten.collidelist(Formen)!=-1:
                    Nicht_in_Luft = True
                else:
                    Nicht_in_Luft = False
                if not Inventar[Inv_Pointer-1].Gegenstandsart in ["Spitzhacke", "Schwert"] and Figur.colliderect(Neuer_Cursor)==False and Figur.colliderect(potenzieller_block)==False and Nicht_in_Luft==True:
                    Gegenstand = Inventar[Inv_Pointer-1]
                    Gegenstand_Art = Gegenstand.Gegenstandsart
                    if Gegenstand.Anzahl > 1:
                        Inventar[Inv_Pointer-1].Anzahl -= 1
                    else:
                        Inventar.pop(Inv_Pointer-1)
                    if Gegenstand_Art == "ReinerStein":
                        Neuer_Block = klassen.ReinerStein(MausX,MausY)
                    elif Gegenstand_Art == "Erde":
                        Neuer_Block = klassen.Erde(MausX,MausY)
                        Neuer_Block.Blockart = "Erde"
                    elif Gegenstand_Art == "Eisen":
                        Neuer_Block = klassen.Eisen(MausX,MausY)
                    elif Gegenstand_Art == "Gold":
                        Neuer_Block = klassen.Gold(MausX,MausY)
                    elif Gegenstand_Art == "Diamant":
                        Neuer_Block = klassen.Diamant(MausX,MausY)
                    elif Gegenstand_Art == "Eiche":
                        Neuer_Block = klassen.Eiche(MausX,MausY)
                    elif Gegenstand_Art == "Birke":
                        Neuer_Block = klassen.Birke(MausX,MausY)
                    elif Gegenstand_Art == "Bruchstein":
                        Neuer_Block = klassen.Bruchstein(MausX,MausY)
                    dict.append(Neuer_Block)
                    
                else:
                    Rechts_klick = False
            except:
                pass
        Rechts_klick = False

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
            if UntenCheckFigur.collidelist(Formen)==-1 and not y+Blockgroesse>FensterHoehe and Aus_Dem_Bildschirm == False:
                y+=Geschwindigkeit
        if TastenAbfangen[pygame.K_d]:
            if Figur.collidelist(Formen)==-1 and Links_Behinderung == False or Rechtserlaubnis==True  :
                RechtsBewegung = True
                x+=Geschwindigkeit
                Sprungverbot = False
                Rechtserlaubnis = False
                Linkserlaubnis = True
    
        # Linksbewegung
        if LinksCheckFigur.collidelist(Formen)!=-1:
            Linkserlaubnis= False
            if UntenCheckFigur.collidelist(Formen)==-1 and not y+Blockgroesse>FensterHoehe and Aus_Dem_Bildschirm == False:
                y+=Geschwindigkeit
        if TastenAbfangen[pygame.K_a]:
            if Figur.collidelist(Formen)==-1 and Rechts_Behinderung == False or Linkserlaubnis==True :
                RechtsBewegung = False
                x-=Geschwindigkeit
                Sprungverbot=False
                Rechtserlaubnis = True
                Linkserlaubnis=False

        # Konstantes Fallen
        if Figur.collidelist(Formen)==-1 and not y+(Blockgroesse)>FensterHoehe and Aus_Dem_Bildschirm == False:
            if Aus_Dem_Bildschirm == False:
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