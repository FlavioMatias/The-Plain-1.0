import pygame, math
from itens import Arsenal
pygame.init()

class Tela:
    game_name = "The Plain"
    width, height = 1450, 830

def mouse():
    mousex, mousey = pygame.mouse.get_pos()
    rel_x, rel_y = mousex - Arsenal.Pistol.rect.centerx, mousey - Arsenal.Pistol.rect.centery
    angle = math.degrees(math.atan2(rel_y, rel_x))
    return angle, mousex


screen = pygame.display.set_mode((Tela.width, Tela.height))
pygame.display.set_caption(Tela.game_name)

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
pause_start_time = 0  
total_pause_time = 0

Run = True
paused = False
state = "menu"


dif_select = ["easy", "medium", "hard"]
dif_cursor = 0
difficulty = "easy"

font = pygame.font.Font("font/PressStart2P.ttf", 15)
fontOP = pygame.font.Font("font/PressStart2P.ttf", 30)


def draw_hp(text, screen):
    text_surface = font.render(text, True, (255, 0, 0)) 
    screen.blit(text_surface, (15, 15)) 