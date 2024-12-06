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

coin = pygame.image.load("./resources/kolikko.png")
# x_coin = randint(0, 300)
# y_coin = randint(0, 400)

x_coin = 300
y_coin = 400

door = pygame.image.load("./resources/ovi.png")

# first values: 

point_counter = 0 

monster_movement = False


# texts

font = pygame.font.SysFont("Georgia", 20)
text_coin_found = font.render("Coin found, you are a rich robot!", True, (255, 0, 0))



# game 

# Alustaa pelin
# scr = init() 
timer = pygame.time.Clock()
# sys time and sys.time - start time and this would be visible 

high = 0
lives = 3
score = 0

while True:
 
    naytto.fill((255, 255, 255))
 
    object_robo.draw(naytto)
    object_monster.draw(naytto)

    naytto.blit(coin, (x_coin, y_coin))

    # Upper bar: point counter, time counter 
    text_point_counter = font.render(f"points are now {point_counter}", True, (255, 0, 0))
    naytto.blit(text_point_counter, (25, 5))
    text_timer = font.render(f"time is now {timer}", True, (255, 0, 0))
    naytto.blit(text_timer, (350, 5))

    print("robo is in location", object_robo.x, object_robo.y)

    if object_robo.x == x_coin and object_robo.y == y_coin:
        naytto.blit(text_coin_found, (w_screen/2, 100))
        point_counter += 1
        #x_coin += 50 
        #y_coin += 50

    if point_counter == 0:
        naytto.blit(door, (w_screen-100, h_screen-100))
        #x_coin += 50 
        #y_coin += 50

    for tapahtuma in pygame.event.get():
 
        # if robot hits coin

        
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

            monster_movement = True 
            
 
        if tapahtuma.type == pygame.KEYUP:
            
            if tapahtuma.key == pygame.K_LEFT:
               left = False
            
            if tapahtuma.key == pygame.K_RIGHT:
                rigth = False
 
            if tapahtuma.key == pygame.K_UP:
                up = False
            
            if tapahtuma.key == pygame.K_DOWN:
                down = False
            
            monster_movement = False 
 
 
        
    # yhteiset muut asiat
 
        # if tapahtuma.type == pygame.KEYDOWN and tapahtuma.key == pygame.K_b:
        #     print("otetaan tauko")
 
        # if tapahtuma.type == pygame.KEYDOWN and tapahtuma.key == pygame.K_t:
        #     print_text = True
 
    # yhteinen exit
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    # Movement 
 
    if rigth:
        object_robo.move_rigth(rate_movement_robo) 
    if left:
        object_robo.move_left(rate_movement_robo) 
    if up:
        object_robo.move_up(rate_movement_robo) 
    if down:
        object_robo.move_down(rate_movement_robo) 

    # - monsters
    random = randint(1, 4)

    if random == 1: 
        object_monster.x += 2
    elif random == 2: 
        object_monster.x -= 2
    elif random == 3: 
        object_monster.y -= 2
    elif random == 4: 
        object_monster.y += 2

    # coins 



    
 
    # yhteiset 
    # if print_text:
    #     naytto.blit(teksti, (200, 50))
 
    # asiat peliin 
    pygame.display.flip()
 
    # fps
    clock.tick(rate_fps)# dev game here 

