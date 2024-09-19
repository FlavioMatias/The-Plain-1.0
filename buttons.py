import pygame
pygame.init()

class Button:
    class Start:
        img = pygame.image.load("sprites/start_button.bmp")
        img_hover = pygame.image.load("sprites/starthover (1).bmp")
        rect = img.get_rect()
        rect.x, rect.y = 600, 350
        
    class Option:
        img = pygame.image.load("sprites/options_button.bmp")
        img_hover = pygame.image.load("sprites/optionshover (1).bmp")
        rect = img.get_rect()
        rect.x, rect.y = 600, 350 + 100
    
    class Exit:
        img = pygame.image.load("sprites/exit_button.bmp")
        img_hover = pygame.image.load("sprites/exithover.png")
        rect = img.get_rect()
        rect.x, rect.y = 600, 350 + 200
        
    class reset:
        img = pygame.image.load("sprites/reset_ button.png")
        img_hover = pygame.image.load("sprites/resethover.png")
        rect = img.get_rect()
        rect.x, rect.y = 710, 350 + 170
        
    class menu:
        img = pygame.image.load("sprites/menu_button.png")
        img_hover = pygame.image.load("sprites/menuhover.png")
        rect = img.get_rect()
        rect.x, rect.y = 440, 350 + 170
        
    class effect_VR:
        img = pygame.image.load("sprites/right_button.png")
        img_click = pygame.image.load("sprites/click_right.png")
        rect = img.get_rect()
        rect.x, rect.y = 750 + 250, 272
        
    class effect_VL:
        img = pygame.image.load("sprites/left_button.png")
        img_click = pygame.image.load("sprites/click_left.png")
        rect = img.get_rect()
        rect.x, rect.y = 750, 272
        
    class music_VR:
        img = pygame.image.load("sprites/right_button.png")
        img_click = pygame.image.load("sprites/click_right.png")
        rect = img.get_rect()
        rect.x, rect.y = 750 + 250, 272 + 140
        
    class music_VL:
        img = pygame.image.load("sprites/left_button.png")
        img_click = pygame.image.load("sprites/click_left.png")
        rect = img.get_rect()
        rect.x, rect.y = 750, 272 + 140
        
    class difR:
        img = pygame.image.load("sprites/right_button.png")
        img_click = pygame.image.load("sprites/click_right.png")
        rect = img.get_rect()
        rect.x, rect.y = 740 + 275, 272 + 310
        
    class difL:
        img = pygame.image.load("sprites/left_button.png")
        img_click = pygame.image.load("sprites/click_left.png")
        rect = img.get_rect()
        rect.x, rect.y = 740, 272 + 310
    
    class exitop:
        img = pygame.image.load("sprites/exit_options.png")
        rect = img.get_rect()
        rect.x, rect.y = 1170, 76
    
    class resume:
        img = pygame.image.load("sprites/resume_button.png")
        rect = img.get_rect()
        rect.x, rect.y = 525, 300

    class menupause:
        img = pygame.image.load("sprites/menu_button_op.png")
        rect = img.get_rect()
        rect.x, rect.y = 525, 500

    class resetpause:
        img = pygame.image.load("sprites/reset_button_op.png")
        rect = img.get_rect()
        rect.x, rect.y = 525, 400