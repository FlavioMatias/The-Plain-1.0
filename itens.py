import pygame,math
from random import randint
pygame.init()

potions_list = []
spw_potion = False
arma_atual = "magic_book"


class Potions:
    class Cura:
        def __init__(self):
            self.sprite = pygame.image.load("sprites/potion.png")
            self.sprite = pygame.transform.scale(self.sprite,(30,50))
            self.rect = self.sprite.get_rect()
            self.rect.x, self.rect.y  = randint(50, 1000), randint(50, 700)
            
        def colid(self, target):
            return self.rect.colliderect(target.rect)
        
        
class Arsenal:
    def get_weapon(arma_atual):
        match arma_atual:
            case "magic_book":
                
                return Arsenal.Pistol
            case "steff":

                return Arsenal.steff
            
    def drop_weapon(a):
        match a:
            case "magic_book":
                
                return Arsenal.steff
            case "steff":

                return Arsenal.Pistol
        
        
            
    class steff:

        
        sprite = pygame.image.load("sprites/cajado of.png")
        sprite_close = pygame.image.load("sprites/cajado of.png")
        
        sprite = pygame.transform.scale(sprite, (25, 55))
        sprite_close = pygame.transform.scale(sprite_close, (35, 60))
        
        sprite_flipped = pygame.transform.flip(sprite, False, True)
        sprite_flipped_close = pygame.transform.flip(sprite_close, False, True)
        rect = sprite.get_rect()
        rect.y, rect.x = 300, 800
    
        def rotate_pistol(In, screen, angle):
            Pistolrotated_image = pygame.transform.rotate(In, -angle)
            Pistolrotated_rect = Pistolrotated_image.get_rect(center=Arsenal.steff.rect.center)
            screen.blit(Pistolrotated_image, Pistolrotated_rect)

        
    class Pistol:
        sprite = pygame.image.load("sprites/book_open.bmp")
        sprite_close = pygame.image.load("sprites/book_close.bmp")
        
        sprite = pygame.transform.scale(sprite, (62, 62))
        sprite_close = pygame.transform.scale(sprite_close, (45, 45))
        
        sprite_flipped = pygame.transform.flip(sprite, False, True)
        sprite_flipped_close = pygame.transform.flip(sprite_close, False, True)
        
        rect = sprite.get_rect()
        rect.y, rect.x = 300, 800
    
        def rotate_pistol(In, screen, angle):
            Pistolrotated_image = pygame.transform.rotate(In, -angle)
            Pistolrotated_rect = Pistolrotated_image.get_rect(center=Arsenal.Pistol.rect.center)
            screen.blit(Pistolrotated_image, Pistolrotated_rect) 
      
    class projetil:
        def __init__(self, x, y, angle,x_proj, y_proj, speed = 20):
            self.img = pygame.image.load("sprites/player_proj.png")
            self.img = pygame.transform.scale(self.img, (x_proj, y_proj))
            self.rect = self.img.get_rect(topleft=(x, y))
            
            self.speed = speed
            self.angle = angle
            
        def up(self):
            radian_angle = math.radians(self.angle)
            
            self.rect.x += self.speed * math.cos(radian_angle)
            self.rect.y += self.speed * math.sin(radian_angle)
        
        def draw(self, surface):
            surface.blit(self.img, self.rect)
            
        def colid(self, target):
            return self.rect.colliderect(target.rect)