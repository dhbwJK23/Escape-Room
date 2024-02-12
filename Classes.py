import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Sprites/Door-1.1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.collider = pygame.Rect(219 * 3, 46 * 3, 3 * 100, 3 * 150)
        self.rect.center = [pos_x, pos_y]
        self.zustand = False

    def open(self, item_group: pygame.sprite.Group, selected_item, screen_width, screen_height):
        if self.zustand==True:
            return True
        if selected_item == 1.1:
            self.image = pygame.image.load("Sprites/Door-1.2.png").convert_alpha()
            self.zustand = True
            return False


class Closet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Sprites/Closet-1.1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.collider = pygame.Rect(49 * 3, 70 * 3, 50 * 3, 3 * 100)
        self.rect.center = [pos_x, pos_y]
        self.unopened = True

    def open(self, item_group: pygame.sprite.Group, selected_item, screen_width, screen_height):
        if self.unopened:
            self.image = pygame.image.load("Sprites/Closet-1.2.png").convert_alpha()
            item = Item(screen_width / 2, screen_height / 2, "Sprites/Key(Room).png", 1.1, 49 * 3, 90 * 3, 50 * 3,
                        3 * 50)
            item_group.add(item)
            self.unopened = False

        return False


class Item(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture, index, collider_left, collider_top, collider_width, collider_height):
        super().__init__()
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.collider = self.collider = pygame.Rect(collider_left, collider_top, collider_width, collider_height)
        self.rect.center = [pos_x, pos_y]
        self.index = index

    def collect(self, item_group: pygame.sprite.Group, hotbar: list, hotbar_group: pygame.sprite.Group):
        item_group.remove(self)
        match self.index:
            case 1.1:
                picture = "Sprites/Key-1.1.png"
            case 2.1:
                picture = "Sprites/Note(Item)-2.png"
        item = Item(hotbar[len(hotbar_group)]["position_x"], hotbar[len(hotbar_group)]["position_y"], picture,
                    self.index, hotbar[len(hotbar_group)]["position_x"] - 50,
                    hotbar[len(hotbar_group)]["position_y"] - 50, 100, 100)
        hotbar_group.add(item)


class HUD(pygame.sprite.Sprite):
    def __init__(self, index, center):
        super().__init__()
        self.image = pygame.image.load("Sprites/Indicator.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.index = index

    def change_position(self, center):
        self.rect.center = center


class Door2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Sprites/Tür-2.1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.collider = pygame.Rect(360, 260, 3 * 100, 3 * 150)
        self.rect.center = [pos_x, pos_y]

    def open(self, item_group: pygame.sprite.Group, selected_item, screen_width, screen_height):
        if selected_item == 2.1:
            self.image = pygame.image.load("Sprites/Tür-2.2.png").convert_alpha()



class Bed(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("Sprites/Bed-2.1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.collider = pygame.Rect(100, 515, 50 * 3, 3 * 50)
        self.rect.center = [pos_x, pos_y]
        self.unopened = True

    def open(self, item_group: pygame.sprite.Group, selected_item, screen_width, screen_height):
        if self.unopened:
            self.image = pygame.image.load("Sprites/Bed-2.2.png").convert_alpha()
            item = Item(screen_width / 2, screen_height / 2, "Sprites/Note-2.png", 2.1, 100, 515, 50 * 3, 3 * 50)
            item_group.add(item)
            self.unopened = False