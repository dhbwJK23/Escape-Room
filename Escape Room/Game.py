import pygame, sys
from Classes import *

pygame.init()
pygame.font.init()

scale=1

font=pygame.font.SysFont("Comic Sans MS",int(60*scale))

SCREEN_WIDTH = 256*3*scale
SCREEN_HEIGHT = 256*3*scale

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape Game")

hud_group=pygame.sprite.Group()
hud_1=HUD(0,630,140,140,scale)
hud_2=HUD(150,630,140,140,scale)
hud_3=HUD(290,630,140,140,scale)
hud_4=HUD(440,630,140,140,scale)
hud_5=HUD(570,630,140,140,scale)
hud_group.add(hud_1)
hud_group.add(hud_2)
hud_group.add(hud_3)
hud_group.add(hud_4)
hud_group.add(hud_5)

indicator_group=pygame.sprite.Group()

item_group=pygame.sprite.Group()

level_group_1=pygame.sprite.Group()

level_group_2=pygame.sprite.Group()
transition_2_3=Transitioner(3,pygame.Rect(530*scale,300*scale,50*scale,60*scale))
level_group_2.add(transition_2_3)

level_group_3=pygame.sprite.Group()
transition_3_2=Transitioner(2,pygame.Rect(650*scale,40*scale,100*scale,100*scale))
level_group_3.add(transition_3_2)

level_group_4=pygame.sprite.Group()
transition_4_2=Transitioner(2,pygame.Rect(430*scale,80*scale,80*scale,500*scale))
level_group_4.add(transition_4_2)

level_group_5=pygame.sprite.Group()
transition_5_4=Transitioner(4,pygame.Rect(650*scale,120*scale,100*scale,400*scale))
level_group_5.add(transition_5_4)

level_group_6=pygame.sprite.Group()
transition_6_4=Transitioner(4,pygame.Rect(500*scale,150*scale,100*scale,380*scale))
transition_6_7=Transitioner(7,pygame.Rect(360*scale,390*scale,50*scale,60*scale))
level_group_6.add(transition_6_4)
level_group_6.add(transition_6_7)

level_group_7=pygame.sprite.Group()
transition_7_6=Transitioner(6,pygame.Rect(650*scale,40*scale,100*scale,100*scale))
level_group_7.add(transition_7_6)

level_group_8=pygame.sprite.Group()
transition_8_9=Transitioner(9,pygame.Rect(250*scale,130*scale,150*scale,280*scale))
level_group_8.add(transition_8_9)

level_group_9=pygame.sprite.Group()
    
furniture_group_1=pygame.sprite.Group()
door_1_1=Furniture("Sprites/Door-1.1.png",650,150,100,350,1.2,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
closet_1_1=Furniture("Sprites/Closet-1.1.png",200,220,100,260,1.1,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
furniture_group_1.add(door_1_1)
furniture_group_1.add(closet_1_1)

furniture_group_2=pygame.sprite.Group()
door_2_1=Furniture("Sprites/Door-2.1.png",0,0,0,0,2.2,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
bed_2_1=Furniture("Sprites/Bed-2.1.png",0,400,200,200,2.1,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
floor_door_2_1=Furniture("Sprites/Floor-Door-2.1.png",550,500,100,100,2.3,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
vent_2_1=Furniture("Sprites/Vent-2.1.png",650,250,100,150,2.4,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
furniture_group_2.add(door_2_1)
furniture_group_2.add(bed_2_1)
furniture_group_2.add(floor_door_2_1)
furniture_group_2.add(vent_2_1)

furniture_group_3=pygame.sprite.Group()

furniture_group_4=pygame.sprite.Group()
door_3_1=Furniture("Sprites/Door-3.1.png",50,30,100,600,3.1,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
door_3_2=Furniture("Sprites/Door-3.2.1.png",180,80,60,500,3.2,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
lock_3_1=Furniture("Sprites/Lock-3.1.png",250,130,150,280,3.3,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
lock_3_2=Furniture("Sprites/Lock-3.2.png",250,130,150,280,3.4,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
furniture_group_4.add(door_3_1)
furniture_group_4.add(door_3_2)
furniture_group_4.add(lock_3_1)
furniture_group_4.add(lock_3_2)

furniture_group_5=pygame.sprite.Group()
fridge_4_1=Furniture("Sprites/Fridge-4.1.png",80,230,100,300,4.1,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
drawer_4_1=Furniture("Sprites/Drawer-4.1.png",480,400,100,100,4.2,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
furniture_group_5.add(fridge_4_1)
furniture_group_5.add(drawer_4_1)

furniture_group_6=pygame.sprite.Group()
safe_5_1=Furniture("Sprites/Safe-5.1.png",0,0,0,0,5.1,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
furniture_group_6.add(safe_5_1)

furniture_group_7=pygame.sprite.Group()

furniture_group_8=pygame.sprite.Group()

furniture_group_9=pygame.sprite.Group()

furniture_group=pygame.sprite.Group()
level_group=pygame.sprite.Group()

running=True
level=list()
level.append(True)
level.append(False)
level.append(False)
level.append(False)
level.append(False)
level.append(False)
level.append(False)
level.append(False)
level.append(False)
level.append(False)


keypad_input=""
safe_input=""

while(running):

    if level[0]:
        image=pygame.image.load("Sprites/Titel.png")

    if level[1]:
        image=pygame.image.load("Sprites/Room-01.png")
        furniture_group=furniture_group_1
        level_group=level_group_1

        for f in furniture_group:
            if f.index==1.2:
                if f.opened:
                    level_transition=Transitioner(2,pygame.Rect(650*scale,150*scale,100*scale,350*scale))
                    level_group_1.add(level_transition)
    

    if level[2]:
        image=pygame.image.load("Sprites/Room-02.png")
        furniture_group=furniture_group_2
        level_group=level_group_2

        for f in furniture_group:
            if f.index==2.2:
                if f.opened:
                    level_transition=Transitioner(4,pygame.Rect(350*scale,150*scale,200*scale,350*scale))
                    level_group_2.add(level_transition)
    
    if level[3]:
        image=pygame.image.load("Sprites/Keypad.png")
        furniture_group=furniture_group_3
        level_group=level_group_3

        if keypad_input=="2594":
            for f in furniture_group_2:
                if f.index==2.2:
                    f.open(hud_group,item_group)
            for l in level_group_2:
                if l.level_index==3:
                    level_group_2.remove(l)
            for h in hud_group:
                if h.index==2.1:
                    h.removeItem()

            for l in level_group_3:
                l.transition(level)
                break
            
        if len(keypad_input)>3:
            keypad_input=""
            
    if level[4]:
        image=pygame.image.load("Sprites/Room-03.png")
        furniture_group=furniture_group_4
        level_group=level_group_4
        
        red=False
        blue=False

        for f in furniture_group:
            if f.index==3.1:
                if f.opened:
                    level_transition=Transitioner(5,f.collider)
                    level_group_4.add(level_transition)
                    
        for f in furniture_group:
            if f.index==3.2:
                if f.opened:
                    level_transition=Transitioner(6,f.collider)
                    level_group_4.add(level_transition)
                    
        for f in furniture_group:
            if f.index==3.3:
                if f.opened:
                    red=True
                    
        for f in furniture_group:
            if f.index==3.4:
                if f.opened:
                    blue=True
                    
        if red and blue:
            Transitioner(8,pygame.Rect(0,0,0,0)).transition(level)

    if level[5]:
        image=pygame.image.load("Sprites/Room-04.png")
        furniture_group=furniture_group_5
        level_group=level_group_5
        
    if level[6]:
        image=pygame.image.load("Sprites/Room-05.png")
        furniture_group=furniture_group_6
        level_group=level_group_6
        
    if level[7]:
        image=pygame.image.load("Sprites/Keypad.png")
        furniture_group=furniture_group_7
        level_group=level_group_7

        if safe_input=="8257":
            for f in furniture_group_6:
                if f.index==5.1:
                    f.open(hud_group,item_group)
            for l in level_group_6:
                if l.level_index==7:
                    level_group_6.remove(l)
            item=Item(pygame.Rect(350,450,50,50),"Sprites/Key-5.1.png",5.1,SCREEN_WIDTH,SCREEN_HEIGHT,scale)
            item_group.add(item)

            for l in level_group_7:
                l.transition(level)
                break
            
        if len(safe_input)>3:
            safe_input=""
            
    if level[8]:
        image=pygame.image.load("Sprites/Room-Final.png")
        furniture_group=furniture_group_8
        level_group=level_group_8
        indicator_group=pygame.sprite.Group()
    
    if level[9]:
        image=pygame.image.load("Sprites/End_Screen.png")
        furniture_group=furniture_group_9
        level_group=level_group_9
        indicator_group=pygame.sprite.Group()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            # print(pos)
            # print(level)
            # print(keypad_input)

            for i in item_group:
                if i.collider.collidepoint(pos):
                    i.collect(hud_group,item_group)

            for f in furniture_group:
                if f.collider.collidepoint(pos):
                    f.open(hud_group,item_group)  

            for h in hud_group:
                if h.collider.collidepoint(pos):
                    print(h.selected)
                    h.select(hud_group,indicator_group)
                    print(h.selected)  

            for l in level_group:
                if l.collider.collidepoint(pos):
                    l.transition(level) 

        if level[0]:
            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_SPACE:   
                    transitioner=Transitioner(1,pygame.Rect(0,0,0,0)) 
                    transitioner.transition(level)     

        if level[3]:

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_0:
                    keypad_input=keypad_input+"0"

                if event.key == pygame.K_1:
                    keypad_input=keypad_input+"1"
 
                if event.key == pygame.K_2:
                    keypad_input=keypad_input+"2"

                if event.key == pygame.K_3:
                    keypad_input=keypad_input+"3"

                if event.key == pygame.K_4:
                    keypad_input=keypad_input+"4"

                if event.key == pygame.K_5:
                    keypad_input=keypad_input+"5"

                if event.key == pygame.K_6:
                    keypad_input=keypad_input+"6"

                if event.key == pygame.K_7:
                    keypad_input=keypad_input+"7"

                if event.key == pygame.K_8:
                    keypad_input=keypad_input+"8"

                if event.key == pygame.K_9:
                    keypad_input=keypad_input+"9"

        if level[7]:

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_0:
                    safe_input=safe_input+"0"

                if event.key == pygame.K_1:
                    safe_input=safe_input+"1"
 
                if event.key == pygame.K_2:
                    safe_input=safe_input+"2"

                if event.key == pygame.K_3:
                    safe_input=safe_input+"3"

                if event.key == pygame.K_4:
                    safe_input=safe_input+"4"

                if event.key == pygame.K_5:
                    safe_input=safe_input+"5"

                if event.key == pygame.K_6:
                    safe_input=safe_input+"6"

                if event.key == pygame.K_7:
                    safe_input=safe_input+"7"

                if event.key == pygame.K_8:
                    safe_input=safe_input+"8"

                if event.key == pygame.K_9:
                    safe_input=safe_input+"9"


    background=pygame.transform.scale_by(image,scale)
    screen.blit(background,(1,1))

    if level[0]:
        text=font.render("Press Space to start",True,(250,0,0))
        screen.blit(text,(100*scale,300*scale))

    if level[3]:
        text=font.render(keypad_input,True,(250,0,0))
        screen.blit(text,(200*scale,160*scale))
        text=font.render("Enter with Keyboard",True,(250,0,0))
        screen.blit(text,(0*scale,10*scale))
        
    if level[7]:
        text=font.render(safe_input,True,(250,0,0))
        screen.blit(text,(200*scale,160*scale))

    
    if level[9]:
        text=font.render("You Escaped!",True,(255,0,0))
        screen.blit(text,(200*scale,100*scale))
        text=font.render("Credits:",True,(0,0,0))
        screen.blit(text,(200*scale,200*scale))
        text=font.render("Game Programming:",True,(0,0,255))
        screen.blit(text,(200*scale,280*scale))
        text=font.render("Massimo Keil",True,(0,0,0))
        screen.blit(text,(200*scale,360*scale))
        text=font.render("Johannes Kommer",True,(0,0,0))
        screen.blit(text,(200*scale,460*scale))
        text=font.render("Game Art:",True,(255,0,255))
        screen.blit(text,(200*scale,560*scale))
        text=font.render("Massimo Keil",True,(0,0,0))
        screen.blit(text,(200*scale,640*scale))

    furniture_group.draw(screen)
    hud_group.draw(screen)
    indicator_group.draw(screen)
    item_group.draw(screen)

    # for f in furniture_group:
    #     pygame.draw.rect(screen,[255,0,0],f.collider)

    #  for h in hud_group:
    #    pygame.draw.rect(screen,[0,255,0],h.collider)
        
    # for i in item_group:
    #     pygame.draw.rect(screen,[0,0,255],i.collider)
    
    # for l in level_group:
    #     pygame.draw.rect(screen,[255,0,255],l.collider)

    pygame.display.flip()





    