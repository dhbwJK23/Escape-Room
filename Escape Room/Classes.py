import pygame
from pygame.sprite import *  

#This class represents a Heads-Up Display (HUD) element
class HUD(pygame.sprite.Sprite):
    #Initializes the HUD
    def __init__(self,pos_x,pos_y,width,height,scale):
        super().__init__()
        self.scale=scale
        self.image=pygame.image.load("Sprites/Empty.png")
        self.rect=self.image.get_rect()
        self.rect.center=[pos_x,pos_y]
        self.index=0
        self.collider=pygame.Rect(pos_x*self.scale,pos_y*self.scale,width*self.scale,height*self.scale)
        self.selected=False
        self.pos_x=pos_x
        self.pos_y=pos_y
        
    #Deselects all other HUD elements
    #Creates an Indicator sprite at the same position
    def select(self,hud_group,indicator_group):
        for i in indicator_group:
            indicator_group.remove(i)
        for h in hud_group:
            h.selected=False
        self.selected=True
        indicator=Indicator(self.pos_x*self.scale,self.pos_y*self.scale,self.scale)
        indicator_group.add(indicator)
        print(self.index)

    #loads an image, scales it, and updates the HUD’s attributes
    def addItem(self,image,index):
        self.image=pygame.image.load(image).convert_alpha()
        self.image=pygame.transform.scale_by(self.image,self.scale)
        self.rect=self.image.get_rect()
        self.rect.center=[self.pos_x*self.scale+self.rect.width/2,self.pos_y*self.scale+self.rect.height/2]
        self.index=index
        
    #resets the HUD’s image and index
    def removeItem(self):
        self.image=pygame.image.load("Sprites/Empty.png")
        self.rect=self.image.get_rect()
        self.index=0
        

#Indicates wich Item is selected
class Indicator(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,scale):
        super().__init__()
        self.scale=scale
        self.image=pygame.image.load("Sprites/Indicator.png").convert_alpha()
        self.image=pygame.transform.scale_by(self.image,self.scale)
        self.rect=self.rect=self.image.get_rect()
        self.rect.center=[pos_x+self.rect.width/2,pos_y+self.rect.height/2]


#provides the furniture for each room
class Furniture(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y,width,height,index,screen_widht,screen_height,scale):
        super().__init__()
        self.scale=scale
        self.image=pygame.image.load(image).convert_alpha()
        self.image=pygame.transform.scale_by(self.image,self.scale)
        self.rect=self.image.get_rect()
        self.rect.center = [screen_widht/2,screen_height/2]
        self.collider=pygame.Rect(pos_x*self.scale,pos_y*self.scale,width*self.scale,height*self.scale)
        self.index=index
        self.screen_widht=screen_widht
        self.screen_height=screen_height
        self.opened=False
    
    def open(self,hud_group,item_group):
        match self.index:
            case 1.1:
                image_opened="Sprites/Closet-1.2.png"
                item_picture="Sprites/Key-1.1.png"
                key_item=0
            case 1.2:
                image_opened="Sprites/Door-1.2.png"
                item_picture=None
                key_item=1.1
            case 2.1:
                image_opened="Sprites/Bed-2.2.png"
                item_picture="Sprites/Note-2.1.png"
                key_item=0
            case 2.2:
                image_opened="Sprites/Door-2.2.png"
                item_picture=None
                key_item=0
            case 2.3:
                image_opened="Sprites/Floor-Door-2.2.png"
                item_picture="Sprites/Golden-Key-2.1.png"
                key_item=0
            case 2.4:
                image_opened="Sprites/Vent-2.2.png"
                item_picture="Sprites/Key-2.1.png"
                key_item=4.1
            case 3.1:
                image_opened="Sprites/Door-3.2.png"
                item_picture=None
                key_item=0
            case 3.2:
                image_opened="Sprites/Door-3.2.2.png"
                item_picture=None
                key_item=2.4
            case 3.3:
                image_opened="Sprites/Empty.png"
                item_picture=None
                key_item=4.2
            case 3.4:
                image_opened="Sprites/Empty.png"
                item_picture=None
                key_item=5.1
            case 4.1:
                image_opened="Sprites/Fridge-4.2.png"
                item_picture="Sprites/Screwdriver-4.1.png"
                key_item=0
            case 4.2:
                image_opened="Sprites/Drawer-4.2.png"
                item_picture="Sprites/Key-4.1.png"
                key_item=2.3
            case 5.1:
                image_opened="Sprites/Safe-5.2.png"
                item_picture=None
                key_item=0

        if key_item==0:
            self.image=pygame.image.load(image_opened).convert_alpha()
            self.image=pygame.transform.scale_by(self.image,self.scale)
            self.opened=True
            if item_picture != None:
                item=Item(self.collider,item_picture,self.index,self.screen_widht,self.screen_height,self.scale)
                item_group.add(item)
                self.collider=pygame.Rect(0,0,0,0)
        else:
            for h in hud_group:
                if h.index==key_item and h.selected==True:
                    self.image=pygame.image.load(image_opened).convert_alpha()
                    self.image=pygame.transform.scale_by(self.image,self.scale)
                    self.opened=True
                    h.removeItem()
                    if item_picture != None:
                        item=Item(self.collider,item_picture,self.index,self.screen_widht,self.screen_height,self.scale)
                        item_group.add(item)
                        self.collider=pygame.Rect(0,0,0,0)
                    break
        

#defines all the Items
class Item(pygame.sprite.Sprite):
    def __init__(self,collider,image,index,screen_widht,screen_height,scale):
        super().__init__()
        self.scale=scale
        self.image=pygame.image.load(image).convert_alpha()
        self.image=pygame.transform.scale_by(self.image,self.scale) 
        self.rect=self.image.get_rect()
        self.rect.center=[screen_widht/2,screen_height/2]
        self.index=index
        self.collider=collider
    
    def collect(self,hud_group,item_group):
        match self.index:
            case 1.1:
                picture="Sprites/Key-1.2.png"
            case 2.1:
                picture="Sprites/Note-2.2.png"
            case 2.3:
                picture="Sprites/Golden-Key-2.2.png"
            case 2.4:
                picture="Sprites/Key-2.2.png"
            case 4.1:
                picture="Sprites/Screwdriver-4.2.png"
            case 4.2:
                picture="Sprites/Key-4.2.png"
            case 5.1:
                picture="Sprites/Key-5.2.png"
                
        for h in hud_group:
            if h.index==0:
                h.addItem(picture,self.index)
                break
        item_group.remove(self)

#makes transitions between scenes "levels" possible
class Transitioner(pygame.sprite.Sprite):
    def __init__(self,level_index,collider):
        super().__init__()
        self.level_index=level_index
        self.collider=collider
    
    def transition(self,level):
        for l in range (0,len(level)):
            level[l]=False
        level[self.level_index]=True




