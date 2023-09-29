import pygame
from pygame.locals import*
pygame.init()
from time import sleep
import random

#       INIZIO PLAYER

img = pygame.image.load("sprite/personaggio.png")
img = pygame.transform.scale(img,(500,400))

player = img.get_rect()
player.y = 800 - 400
player.x = 1400 - 1500

#       FINE PLAYER

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1600

una_Vita = pygame.image.load("sprite/vite/unaVita.png")
una_Vita = pygame.transform.scale(una_Vita,(125,125))

due_Vite = pygame.image.load("sprite/vite/dueVite.png")
due_Vite = pygame.transform.scale(due_Vite,(125,125))

tre_Vite = pygame.image.load("sprite/vite/treVite.png")
tre_Vite = pygame.transform.scale(tre_Vite,(225,225))

quattro_Vite = pygame.image.load("sprite/vite/quattroVite.png")
quattro_Vite = pygame.transform.scale(quattro_Vite,(125,125))

cinque_Vite = pygame.image.load("sprite/vite/cinqueVite.png")
cinque_Vite= pygame.transform.scale(cinque_Vite,(125,125))

vite1 = una_Vita.get_rect()
vite2 = due_Vite.get_rect()
vite3 = tre_Vite.get_rect()
vite4 = quattro_Vite.get_rect()
vite5 = cinque_Vite.get_rect()
vita = 1

#   INIZIO SOUND

walk1 = pygame.mixer.Sound("audio/passiPlayer.mp3")
walk2 = pygame.mixer.Sound("audio/passiPlayer.mp3")

#   FINE SOUND

#    INIZIO PROIETTILI

pro1 = pygame.image.load("sprite/proiettile 1.png")
pro1 = pygame.transform.scale(pro1,(50,100))
proiettile1 = pro1.get_rect()
proiettile = True

#    FINE PROIETTILI


pesce1 = pygame.image.load("sprite/pesce1.png")
pesce1 = pygame.transform.scale(pesce1,(60,60))
pesc1 = pesce1.get_rect()
pesc1.x = 1600
pesc1.y = random.randint(10,790)

pesce2 = pygame.image.load("sprite/pesce2.png")
pesce2 = pygame.transform.scale(pesce2,(100,100))
pesc2 = pesce2.get_rect()
pesc2.x = 1600
pesc2.y = random.randint(10,790)

pesce3 = pygame.image.load("sprite/pesce3.png")
pesce3 = pygame.transform.scale(pesce3,(100,100))
pesc3 = pesce3.get_rect()
pesc3.x = 1600
pesc3.y = random.randint(10,790)

pesci = True
pesci_uccisi = 0
record_pesci_uccisi = 0

menu = 1
esci_regole = False
inizio_facile = True
inizio_medio = True
inizio_difficile = True

clk = pygame.time.Clock()

screen = pygame.display.set_mode([1800,900])
WINDOW_HEIGHT, WINDOW_WIDTH = screen.get_size()
start = pygame.image.load("sprite/start.png")
start = pygame.transform.scale(start, (WINDOW_HEIGHT, WINDOW_WIDTH))
background = pygame.image.load("sprite/sfondo.jpg")
background = pygame.transform.scale(background, (WINDOW_HEIGHT, WINDOW_WIDTH))
menuBack = pygame.image.load("sprite/menu.png")
menuBack = pygame.transform.scale(menuBack, (WINDOW_HEIGHT, WINDOW_WIDTH))
persoBack = pygame.image.load("sprite/perso.jpg")
persoBack = pygame.transform.scale(persoBack, (WINDOW_HEIGHT, WINDOW_WIDTH))
regoleBack = pygame.image.load("sprite/regole.png")
regoleBack = pygame.transform.scale(regoleBack, (WINDOW_HEIGHT, WINDOW_WIDTH))

starta = 0
facile = False
medio = False
difficile = False
regole = False
start_proiettile = False
perso = False

font_pesci_uccisi = pygame.font.SysFont("Arial", 50)
font_record_pesci_uccisi = pygame.font.SysFont("Arial", 50)

font_menu = pygame.font.Font(None, 50) 
button_facile_menu = pygame.Rect(100, 100, 300, 58) 
button_facile_menu.x = WINDOW_WIDTH / 2 - 350  
button_facile_menu.y = WINDOW_HEIGHT / 2 - 600 
facile_text_menu = font_menu.render("FACILE", True, "black") 
text_rect_menu_facile = facile_text_menu.get_rect(center=(button_facile_menu.x + 150, button_facile_menu.y + 30)) 

button_medio_menu = pygame.Rect(100, 100, 300, 58) 
button_medio_menu.x = WINDOW_WIDTH / 2 - 350  
button_medio_menu.y = WINDOW_HEIGHT / 2 - 450 
medio_text_menu = font_menu.render("MEDIO", True, "black") 
text_rect_menu_medio= medio_text_menu.get_rect(center=(button_medio_menu.x + 150, button_medio_menu.y + 30))

button_difficile_menu = pygame.Rect(100, 100, 300, 58) 
button_difficile_menu.x = WINDOW_WIDTH / 2 - 350  
button_difficile_menu.y = WINDOW_HEIGHT / 2 - 300 
difficile_text_menu = font_menu.render("DIFFICILE", True, "black") 
text_rect_menu_difficile = difficile_text_menu.get_rect(center=(button_difficile_menu.x + 150, button_difficile_menu.y + 30))

button_regole_menu = pygame.Rect(100, 100, 300, 58) 
button_regole_menu.x = WINDOW_WIDTH / 2 - 350  
button_regole_menu.y = WINDOW_HEIGHT / 2 - 150 
regole_text_menu = font_menu.render("REGOLE", True, "black") 
text_rect_menu_regole = regole_text_menu.get_rect(center=(button_regole_menu.x + 150, button_regole_menu.y + 30))

button_esci = pygame.Rect(100, 100, 300, 58) 
button_esci.x = WINDOW_WIDTH / 2 + 1040 
button_esci.y = WINDOW_HEIGHT / 2 - 890
esci_text = font_menu.render("CHIUDI", True, "black") 
text_rect_esci = esci_text.get_rect(center=(button_esci.x + 150, button_esci.y + 30))

button_esc_regole = pygame.Rect(100, 100, 300, 58) 
button_esc_regole.x = WINDOW_WIDTH /2 + 1040
button_esc_regole.y = WINDOW_HEIGHT /2 - 70
esc_regole_text = font_menu.render("ESC", True, "black") 
text_rect_esc_regole = esc_regole_text.get_rect(center=(button_esc_regole.x + 150, button_esc_regole.y + 30))


running = True
while running: 

    eventlist = pygame.event.get()
    for ev in eventlist:
        if ev.type == pygame.QUIT:
            running = False

    if (starta == 0):
        screen.fill("black")
        screen.blit(start,(0,0))
        pygame.display.flip()
        sleep(3)
        starta = 1
        menu = 0
        pesci = False


    #      MENÙ

    if (menu == 0):
        
        pesci = False
        
        screen.blit(menuBack,(0,0))
        pygame.draw.rect(screen, "white", button_esci, 0, 10)       
        screen.blit(esci_text, text_rect_esci)
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if button_esci.collidepoint(ev.pos):
                running = False

    pygame.draw.rect(screen, "white", button_facile_menu, 0, 10)
    screen.blit(facile_text_menu, text_rect_menu_facile)
    if ev.type == pygame.MOUSEBUTTONDOWN:
        if button_facile_menu.collidepoint(ev.pos):
            facile = True
            
    pygame.draw.rect(screen, "white", button_medio_menu, 0, 10)
    screen.blit(medio_text_menu, text_rect_menu_medio)
    if ev.type == pygame.MOUSEBUTTONDOWN:
        if button_medio_menu.collidepoint(ev.pos):
            medio = True
            
    pygame.draw.rect(screen, "white", button_difficile_menu, 0, 10)       
    screen.blit(difficile_text_menu, text_rect_menu_difficile) 
    if ev.type == pygame.MOUSEBUTTONDOWN: 
        if button_difficile_menu.collidepoint(ev.pos): 
            difficile = True
            
    pygame.draw.rect(screen, "white", button_regole_menu, 0, 10)       
    screen.blit(regole_text_menu, text_rect_menu_regole) 
    if ev.type == pygame.MOUSEBUTTONDOWN: 
        if button_regole_menu.collidepoint(ev.pos): 
            regole = True

    record_text = font_pesci_uccisi.render("Record pesci uccisi (qualsiasi modalità): " + str(record_pesci_uccisi), True, "white")
    record_rect_text = record_text.get_rect()
    record_rect_text.x = 550
    record_rect_text.y = 300
    screen.blit(record_text, record_rect_text)
    
    #   FINE MENÙ


    #   INIZIO LIVELLO FACILE
    
    if (facile == True):
        screen.fill("green")
        screen.blit(background,(0,0))
        pesci = True
        perso = False
        
        if (inizio_facile == True):
            vita = 5
            pesc1.x = 1600
            pesc2.x = 1600
            pesc3.x = 1600
            pesci_uccisi = 0
            inizio_facile = False
            

        pygame.draw.line(screen, "red", [150, 0], [150,WINDOW_HEIGHT], 5)
        pygame.draw.rect(screen, "green", pygame.Rect(0, 0, 150, WINDOW_HEIGHT))

        screen.blit(img, player)
        
        if (vita == 5):
            screen.blit(cinque_Vite,(0,-32))
            
        if (vita == 4):
            screen.blit(quattro_Vite,(0,-32))
                
        if (vita == 3):
            screen.blit(tre_Vite,(0,0))
            
        if (vita == 2):
            screen.blit(due_Vite,(0,-32))
        
        if (vita == 1):
            screen.blit(una_Vita,(0,-32))
            
        surf_text = font_pesci_uccisi.render("Pesci uccisi:" + str(pesci_uccisi), True, "white")
        rect_text = surf_text.get_rect()
        rect_text.x = 1500
        rect_text.y = 10

        screen.blit(surf_text, rect_text)

        if player.y >= -167:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:  
                player.y-=8
                walk1.play()      
            else:
                walk1.stop()
                    

        if player.y <= 650:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                player.y+=8
                walk2.play
        
        if (proiettile == 1):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                screen.blit(pro1,(player.x + 220, player.y + 150))    
                proiettile1.x = player.x + 220
                proiettile1.y = player.y + 150
                start_proiettile = True
              
        if start_proiettile == True:
            proiettile1.x += 20
            screen.blit(pro1,(proiettile1.x, proiettile1.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            facile = False
            menu = 0
            
        if (pesci == True):
            screen.blit(pesce1,pesc1)
            screen.blit(pesce2,pesc2)
            screen.blit(pesce3,pesc3)
            pesc1.x -= random.randint(1,5)
            pesc2.x -= random.randint(1,5)
            pesc3.x -= random.randint(1,5)
                
        if proiettile1.colliderect(pesc1):
            pesc1.y =  random.randint(10,790)
            pesc1.x = 1600
            pesci_uccisi += 1

        if proiettile1.colliderect(pesc2):
            pesc2.y =  random.randint(10,790)
            pesc2.x = 1600
            pesci_uccisi += 1
            
        if proiettile1.colliderect(pesc3):
            pesc3.y =  random.randint(10,790)
            pesc3.x = 1600
            pesci_uccisi += 1

        if (pesci_uccisi > record_pesci_uccisi):
            record_pesci_uccisi = pesci_uccisi

        if (pesc1.x <= 150):
            pesc1.x = 1600
            vita -= 1
        
        if (pesc2.x <= 150):
            pesc2.x = 1600
            vita -= 1
        
        if (pesc3.x <= 150):
            pesc3.x = 1600
            vita -= 1

        if (vita <= 0):
            perso = True
        
        if (perso == True):
            screen.fill("black")
            screen.blit(persoBack,(16,16))
            pesci = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_8]:
                facile = False
                menu = 0
                perso = False
                inizio_facile = True

    #   FINE LIVELLO FACILE


    #   INIZIO LIVELLO MEDIO
    
    if (medio == True):
        screen.fill("green")
        screen.blit(background,(0,0))
        pesci = True
        perso = False
        
        if (inizio_medio == True):
            vita = 3
            pesc1.x = 1600
            pesc2.x = 1600
            pesc3.x = 1600
            pesci_uccisi = 0
            inizio_medio = False

        if (pesci_uccisi > record_pesci_uccisi):
            record_pesci_uccisi = pesci_uccisi

        pygame.draw.line(screen, "red", [150, 0], [150,WINDOW_HEIGHT], 5)
        pygame.draw.rect(screen, "yellow", pygame.Rect(0, 0, 150, WINDOW_HEIGHT))

        screen.blit(img, player)
                
        if (vita == 3):
            screen.blit(tre_Vite,(0,0))
            
        if (vita == 2):
            screen.blit(due_Vite,(0,-32))
        
        if (vita == 1):
            screen.blit(una_Vita,(0,-32))

        surf_text = font_pesci_uccisi.render("Pesci uccisi:" + str(pesci_uccisi), True, "white")
        rect_text = surf_text.get_rect()
        rect_text.x = 1500
        rect_text.y = 10

        screen.blit(surf_text, rect_text)

        if player.y >= -167:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:  
                player.y-=9
                walk1.play()      
            else:
                walk1.stop()
                    

        if player.y <= 650:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                player.y+=9
                walk2.play
        
        if (proiettile == 1):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                screen.blit(pro1,(player.x + 220, player.y + 150))    
                proiettile1.x = player.x + 220
                proiettile1.y = player.y + 150
                start_proiettile = True
              
        if start_proiettile == True:
            proiettile1.x += 20
            screen.blit(pro1,(proiettile1.x, proiettile1.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            medio = False
            menu = 0
            
        if (pesci == True):
            screen.blit(pesce1,pesc1)
            screen.blit(pesce2,pesc2)
            screen.blit(pesce3,pesc3)
            pesc1.x -= random.randint(1,10)
            pesc2.x -= random.randint(1,10)
            pesc3.x -= random.randint(1,10)
                
        if proiettile1.colliderect(pesc1):
            pesc1.y =  random.randint(10,790)
            pesc1.x = 1600
            pesci_uccisi += 1

        if proiettile1.colliderect(pesc2):
            pesc2.y =  random.randint(10,790)
            pesc2.x = 1600
            pesci_uccisi += 1 

        if proiettile1.colliderect(pesc3):
            pesc3.y =  random.randint(10,790)
            pesc3.x = 1600
            pesci_uccisi += 1
            
        if (pesc1.x <= 150):
            pesc1.x = 1600
            vita -= 1
        
        if (pesc2.x <= 150):
            pesc2.x = 1600
            vita -= 1
        
        if (pesc3.x <= 150):
            pesc3.x = 1600
            vita -= 1

        if (vita <= 0):
            perso = True
        
        if (perso == True):
            screen.fill("black")
            screen.blit(persoBack,(16,16))
            pesci = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_8]:
                medio = False
                menu = 0
                perso = False
                inizio_medio = True

    #   FINE LIVELLO MEDIO
    

    #   INIZIO LIVELLO DIFFICILE
    
    if (difficile == True):
        screen.fill("green")
        screen.blit(background,(0,0))
        pesci = True
        perso = False
        
        if (inizio_difficile == True):
            vita = 1
            pesc1.x = 1600
            pesc2.x = 1600
            pesc3.x = 1600
            pesci_uccisi = 0
            inizio_difficile = False

        if (pesci_uccisi > record_pesci_uccisi):
            record_pesci_uccisi = pesci_uccisi

        pygame.draw.line(screen, "green", [150, 0], [150,WINDOW_HEIGHT], 5)
        pygame.draw.rect(screen, "red", pygame.Rect(0, 0, 150, WINDOW_HEIGHT))

        screen.blit(img, player)
        
        if (vita == 1):
            screen.blit(una_Vita,(0,-32))

        surf_text = font_pesci_uccisi.render("Pesci uccisi:" + str(pesci_uccisi), True, "white")
        rect_text = surf_text.get_rect()
        rect_text.x = 1500
        rect_text.y = 10

        screen.blit(surf_text, rect_text)

        if player.y >= -167:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:  
                player.y-=11
                walk1.play()      
            else:
                walk1.stop()
                

        if player.y <= 650:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                player.y+=11
                walk2.play
        
        if (proiettile == 1):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                screen.blit(pro1,(player.x + 220, player.y + 150))    
                proiettile1.x = player.x + 220
                proiettile1.y = player.y + 150
                start_proiettile = True
            
        if start_proiettile == True:
            proiettile1.x += 20
            screen.blit(pro1,(proiettile1.x, proiettile1.y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            difficile = False
            menu = 0
            
        if (pesci == True):
            screen.blit(pesce1,pesc1)
            screen.blit(pesce2,pesc2)
            screen.blit(pesce3,pesc3)
            pesc1.x -= random.randint(1,15)
            pesc2.x -= random.randint(1,15)
            pesc3.x -= random.randint(1,15)
                
        if proiettile1.colliderect(pesc1):
            pesc1.y =  random.randint(10,790)
            pesc1.x = 1600
            pesci_uccisi += 1
            
        if proiettile1.colliderect(pesc2):
            pesc2.y =  random.randint(10,790)
            pesc2.x = 1600
            pesci_uccisi += 1
                       
        if proiettile1.colliderect(pesc3):
            pesc3.y =  random.randint(10,790)
            pesc3.x = 1600
            pesci_uccisi += 1

        if (pesc1.x <= 150):
            pesc1.x = 1600
            vita -= 1
        
        if (pesc2.x <= 150):
            pesc2.x = 1600
            vita -= 1
        
        if (pesc3.x <= 150):
            pesc3.x = 1600
            vita -= 1

        if (vita <= 0):
            perso = True
        
        if (perso == True):
            screen.fill("black")
            screen.blit(persoBack,(16,16))
            pesci = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_8]:
                difficile = False
                menu = 0
                perso = False
                inizio_difficile = True
  
    #   FINE LIVELLO DIFFICILE


    #   INIZIO REGOLE

    if (regole == True):
        screen.fill("black")
        screen.blit(regoleBack,(0,0))
        esci_regole = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            regole = False
            menu = 0
            esci_regole = False
            
    if (esci_regole == True):    
        pygame.draw.rect(screen, "white", button_esc_regole, 0, 10)       
        screen.blit(esc_regole_text, text_rect_esc_regole) 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if button_esc_regole.collidepoint(ev.pos): 
                regole = False
                menu = 0
                esci_regole = False

    #   FINE REGOLE


    pygame.display.flip()
    screen.fill((161,173,255))

    clk.tick(90)