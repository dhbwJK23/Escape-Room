import pygame, sys
from Classes import *
from Functions import *

pygame.init()

SCREEN_WIDTH = 256 * 3
SCREEN_HEIGHT = 256 * 3

font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape Game")
room = pygame.image.load("Sprites/Room-01.png")
room2 = pygame.image.load("Sprites/Raum-02.png")
titel = pygame.image.load("Sprites/Titel.png")

hotbar = []
hotbar.append({"position_x": 66,
               "position_y": 695})
hotbar.append({"position_x": 210,
               "position_y": 695})
hotbar.append({"position_x": 354,
               "position_y": 695})
hotbar.append({"position_x": 499,
               "position_y": 695})
hotbar.append({"position_x": 646,
               "position_y": 695})

selected_item = 0

closet = Closet(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
door = Door(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
bed = Bed(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
door2 = Door2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)


furniture_group = pygame.sprite.Group()
furniture_group.add(closet)
furniture_group.add(door)
furniture_group2 = pygame.sprite.Group()
furniture_group2.add(bed)
furniture_group2.add(door2)

item_group = pygame.sprite.Group()

hotbar_group = pygame.sprite.Group()

hud_group = pygame.sprite.Group()

running = True

game_start = False

game_stage_1 = False

while True:

    if game_start == False:
        screen.blit(titel, (1, 1))
        draw_text(screen, "Press Space", font, TEXT_COL, 250, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
    else:
        if game_stage_1 == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)

                    for i in item_group:
                        if i.collider.collidepoint(pos):
                            i.collect(item_group, hotbar, hotbar_group)

                    for f in furniture_group:
                        if f.collider.collidepoint(pos):
                            game_stage_1=f.open(item_group, selected_item, SCREEN_WIDTH, SCREEN_HEIGHT)

                    selected_item = select(selected_item, hotbar_group, pos, hud_group)

                 #hier abfragen if door == open and ccklick on door
                                    #game_stage_1 = True

            screen.blit(room, (1, 1))
            furniture_group.draw(screen)
            item_group.draw(screen)
            hotbar_group.draw(screen)
            hud_group.draw(screen)

            """for h in hotbar_group:
                pygame.draw.rect(screen,[255,0,0],h.collider)
            """
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)

                    for i in item_group:
                        if i.collider.collidepoint(pos):
                            i.collect(item_group, hotbar, hotbar_group)

                    for f in furniture_group2:
                        if f.collider.collidepoint(pos):
                            f.open(item_group, selected_item, SCREEN_WIDTH, SCREEN_HEIGHT)

                    selected_item = select(selected_item, hotbar_group, pos, hud_group)

            screen.blit(room2, (1, 1))
            furniture_group2.draw(screen)
            item_group.draw(screen)
            hotbar_group.draw(screen)
            hud_group.draw(screen)

    pygame.display.flip()