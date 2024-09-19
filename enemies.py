import pygame, math, random
from aud.audios import damage_sound
from config import Tela

Create_goblin = pygame.USEREVENT + 1 
Create_ranged = pygame.USEREVENT + 2 
Create_golem = pygame.USEREVENT + 3 

goblin_S = 0
magic_S = 0
golem_S = 0

enemy_projectiles = []
enemies = []

class goblin:
    def __init__(self, target):
        self.img = pygame.image.load("sprites/gobli-1.bmp")
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.img_flip = pygame.transform.flip(self.img, True, False)
        spawn_offset = 100  

        match random.choice(["top", "bottom", "left", "right"]):
            case "top":
                self.rect = self.img.get_rect(midtop=(random.randint(0, Tela.width), -spawn_offset))
            case "bottom":
                self.rect = self.img.get_rect(midbottom=(random.randint(0, Tela.width), Tela.height + spawn_offset))
            case "left":
                self.rect = self.img.get_rect(midleft=(-spawn_offset, random.randint(0, Tela.height)))
            case "right":
                self.rect = self.img.get_rect(midright=(Tela.width + spawn_offset, random.randint(0, Tela.height)))
                
        self.speed = random.randint(6, 8)
        self.target = target
        self.last_atack = pygame.time.get_ticks()
        self.hp = 100
        self.atk = 50
        
    def move(self):
        target_x, target_y = self.target.rect.center
        distance = math.hypot(target_x - self.rect.centerx, target_y - self.rect.centery)

        if distance > 35:
            rel_x, rel_y = target_x - self.rect.centerx, target_y - self.rect.centery
            angle = math.atan2(rel_y, rel_x)
            
            self.rect.x += self.speed * math.cos(angle)
            self.rect.y += self.speed * math.sin(angle)
        
    def draw(self, player,  screen):
        if self.rect.x > player.rect.x:
            screen.blit(self.img, self.rect)
        else:
            screen.blit(self.img_flip, self.rect)
        
    def colid(self, target):
        return self.rect.colliderect(target.rect)
    
    def atack(self, target):
        time = pygame.time.get_ticks() 
        if time - self.last_atack >= 1000:
            if self.colid(target):
                damage_sound.play()
                target.is_damaged = True
                target.damage_time = 9000
                target.hp -= self.atk
                self.last_atack = time 

class enemy_proj: 
    def __init__(self, x, y, angle):
        self.img = pygame.image.load("sprites/enemy_proj.png")
        self.img = pygame.transform.scale(self.img, (25, 25)) 
        self.rect = self.img.get_rect(center=(x, y))
        self.speed = 6
        self.angle = angle
        self.atk = 50

    def move(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        
    def colid(self, target):
        return self.rect.colliderect(target.rect)
    
class ranged:
    def __init__(self, target):
        self.img = pygame.image.load("sprites/magic.bmp")
        self.img = pygame.transform.scale(self.img, (80, 100))
        self.img_flip = pygame.transform.flip(self.img, True, False)
        spawn_offset = 50  

        match random.choice(["top", "bottom", "left", "right"]):
            case "top":
                self.rect = self.img.get_rect(midtop=(random.randint(0, Tela.width), -spawn_offset))
            case "bottom":
                self.rect = self.img.get_rect(midbottom=(random.randint(0, Tela.width), Tela.height + spawn_offset))
            case "left":
                self.rect = self.img.get_rect(midleft=(-spawn_offset, random.randint(0, Tela.height)))
            case "right":
                self.rect = self.img.get_rect(midright=(Tela.width + spawn_offset, random.randint(0, Tela.height)))
        
        self.speed = random.randint(5, 6)
        self.target = target
        self.last_attack = pygame.time.get_ticks()
        self.hp = 50
        self.atk = 50
        self.atk_spd = random.randint(1200, 1500)

    def move(self):
        target_x, target_y = self.target.rect.center
        distance = math.hypot(target_x - self.rect.centerx, target_y - self.rect.centery)

        if distance > 600:
            rel_x, rel_y = target_x - self.rect.centerx, target_y - self.rect.centery
            angle = math.atan2(rel_y, rel_x)
            
            self.rect.x += self.speed * math.cos(angle)
            self.rect.y += self.speed * math.sin(angle)
        
    def draw(self, player, screen):
        if self.rect.x < player.rect.x:
            screen.blit(self.img, self.rect)
        else:
            screen.blit(self.img_flip, self.rect)

    def colid(self, target):
        return self.rect.colliderect(target.rect)
    
    def atack(self, player):
        time = pygame.time.get_ticks()
        if time - self.last_attack >= self.atk_spd:
            target_x, target_y = self.target.rect.center
            rel_x, rel_y = target_x - self.rect.centerx, target_y - self.rect.centery
            angle = math.atan2(rel_y, rel_x)

            new_bullet = enemy_proj(self.rect.centerx, self.rect.centery, angle)
            enemy_projectiles.append(new_bullet) 
            self.last_attack = time

class golem:
    def __init__(self, target):
        self.img = pygame.image.load("sprites/golem.bmp")
        self.img = pygame.transform.scale(self.img, (250, 250))
        self.img_flip = pygame.transform.flip(self.img, True, False)
        spawn_offset = 50

        match random.choice(["top", "bottom", "left", "right"]):
            case "top":
                self.rect = self.img.get_rect(midtop=(random.randint(0, Tela.width), -spawn_offset))
            case "bottom":
                self.rect = self.img.get_rect(midbottom=(random.randint(0, Tela.width), Tela.height + spawn_offset))
            case "left":
                self.rect = self.img.get_rect(midleft=(-spawn_offset, random.randint(0, Tela.height)))
            case "right":
                self.rect = self.img.get_rect(midright=(Tela.width + spawn_offset, random.randint(0, Tela.height)))
        lifes = [1500, 1200, 1000]
        self.speed = random.randint(1, 3)
        self.target = target
        self.last_atack = pygame.time.get_ticks()
        self.hp = lifes[self.speed - 1]
        self.atk = 100
        
    def move(self):
        target_x, target_y = self.target.rect.center
        distance = math.hypot(target_x - self.rect.centerx, target_y - self.rect.centery)

        if distance > 45:
            rel_x, rel_y = target_x - self.rect.centerx, target_y - self.rect.centery
            angle = math.atan2(rel_y, rel_x)
            
            self.rect.x += self.speed * math.cos(angle)
            self.rect.y += self.speed * math.sin(angle)
    def draw(self, player,  screen):
        if self.rect.x > player.rect.x:
            screen.blit(self.img_flip, self.rect)
        else:
            screen.blit(self.img, self.rect)
        
    def colid(self, target):
        return self.rect.colliderect(target.rect)
    
    def atack(self, target):
        time = pygame.time.get_ticks() 
        if time - self.last_atack >= 3000:
            if self.colid(target):
                damage_sound.play()
                target.is_damaged = True
                target.damage_time = 9000
                target.hp -= self.atk
                self.last_atack = time  