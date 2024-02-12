import pygame
from Classes import *


def select(selected_item, hotbar_group: pygame.sprite.Group, pos, hud_group: pygame.sprite.Group):
    index = 0

    for h in hotbar_group:
        if h.collider.collidepoint(pos):
            if selected_item == h.index:
                index = 0
                for hu in hud_group:
                    if hu.index == selected_item:
                        hud_group.remove(hu)

            else:
                hud = HUD(h.index, h.rect.center)
                hud_group.add(hud)
                index = h.index
        break

    return index


def draw_text(screen, text, font, text_col, x, y, ):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))