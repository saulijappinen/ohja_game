# dev game here 

import pygame
from random import randint

# load resources

# 1 Define classes 
# - classes: robot, monster, cause they both move
# - just appear: coins. and door?  


class Robot: 
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("./resources/robo.png")
 
    def draw(self, naytto):
        naytto.blit(self.pic, (self.x, self.y))        
 
    def move_rigth(self, step = int):
        self.x += step
 
    def move_left(self, step = int):
        self.x -= step
 
    def move_up(self, step = int):
        self.y -= step
 
    def move_down(self, step = int):
        self.y += step

class Monster: 
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("./resources/hirvio.png")
 
    def draw(self, naytto):
        naytto.blit(self.pic, (self.x, self.y))        
 
    def move_rigth(self, step = int):
        self.x += step
 
    def move_left(self, step = int):
        self.x -= step
 
    def move_up(self, step = int):
        self.y -= step
 
    def move_down(self, step = int):
        self.y += step



# pelin aloitus ja näytön speksaus
 
pygame.init()
 
w_screen = 800
h_screen = 600
 
naytto = pygame.display.set_mode((w_screen, h_screen))
 
clock = pygame.time.Clock()
 
# parametrit 
 
rate_fps = 60



# objects

w = randint(0, w_screen-100)
h = randint(0, h_screen-100)

object_robo = Robot(w, h)
rate_movement_robo = 1 

rigth = False
left = False
up = False
down = False

object_monster = Monster(500, 500)



# game 

while True:
 
    naytto.fill((255, 255, 255))
 
    object_robo.draw(naytto)
    object_monster.draw(naytto)
 
    for tapahtuma in pygame.event.get():
 
        # Robo 1:n jutut 
 
        if tapahtuma.type == pygame.KEYDOWN:
            
            if tapahtuma.key == pygame.K_LEFT:
                print("vasen näppäin alas")
                left = True
            
            if tapahtuma.key == pygame.K_RIGHT:
                print("oikea näppäin alas")
                rigth = True
            
            if tapahtuma.key == pygame.K_UP:
                print("ylös näppäin alas")
                up = True
 
            if tapahtuma.key == pygame.K_DOWN:
                print("alas näppäin alas")
                down = True
 
        if tapahtuma.type == pygame.KEYUP:
            
            if tapahtuma.key == pygame.K_LEFT:
               left = False
            
            if tapahtuma.key == pygame.K_RIGHT:
                rigth = False
 
            if tapahtuma.key == pygame.K_UP:
                up = False
            
            if tapahtuma.key == pygame.K_DOWN:
                down = False
 
 
        
    # yhteiset muut asiat
 
        # if tapahtuma.type == pygame.KEYDOWN and tapahtuma.key == pygame.K_b:
        #     print("otetaan tauko")
 
        # if tapahtuma.type == pygame.KEYDOWN and tapahtuma.key == pygame.K_t:
        #     print_text = True
 
    # yhteinen exit
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    # liikkumisen määrät 
 
    if rigth:
        object_robo.move_rigth(rate_movement_robo) 
    if left:
        object_robo.move_left(rate_movement_robo) 
    if up:
        object_robo.move_up(rate_movement_robo) 
    if down:
        object_robo.move_down(rate_movement_robo) 
    
 
    # yhteiset 
    # if print_text:
    #     naytto.blit(teksti, (200, 50))
 
    # asiat peliin 
    pygame.display.flip()
 
    # fps
    clock.tick(rate_fps)