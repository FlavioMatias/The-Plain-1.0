import pygame, math
pygame.init()

projectiles = []

class Player:
    sprite = pygame.image.load("sprites/player.png")
    sprite = pygame.transform.scale(sprite, (100, 100))
    sprite_flipped = pygame.transform.flip(sprite, True, False)
    
    sprite_red = sprite.copy()  
    flip_red = sprite_flipped.copy()  

    sprite_red.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)
    flip_red.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)
    
    rect = sprite.get_rect()
    rect.x, rect.y  = 600, 300
    atk = 50
    hp = 400
    speed = 8
    is_damaged = False
    damage_timer = 0
    
    def move(keys):
        if keys[pygame.K_a]: 
            Player.rect.x -= Player.speed
            
        if keys[pygame.K_d]: 
            Player.rect.x += Player.speed
            
        if keys[pygame.K_w]: 
            Player.rect.y -= Player.speed
            
        if keys[pygame.K_s]: 
            Player.rect.y += Player.speed
            
        if Player.rect.x < 0:
            Player.rect.x = 0
        if Player.rect.right > 1450:
            Player.rect.right = 1450
        if Player.rect.y < 0:
            Player.rect.y = 0
        if Player.rect.bottom > 830:
            Player.rect.bottom = 830
        
