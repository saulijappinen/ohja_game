
# Tähän alkuun jotain yleistä pelistä vielä


import pygame
import random

class Robotti: 
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("robo.png")

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
rate_movement = 2 




# robojen luonti 

n_robots = 2 

w = random.randint(0, w_screen-100)
h = random.randint(0, h_screen-100)

robo1 = Robotti(w, h)

w = random.randint(0, w_screen-100)
h = random.randint(0, h_screen-100)

robo2 = Robotti(w, h)

# vakkarijutut

r1_rigth = False
r1_left = False
r1_up = False
r1_down = False

r2_rigth = False
r2_left = False
r2_up = False
r2_down = False

print_text = False



while True:

    naytto.fill((0, 0, 0))


    robo1.draw(naytto)
    robo2.draw(naytto)

    fontti = pygame.font.SysFont("Arial", 24)
    teksti = fontti.render("Vitsikäs teksti", True, (255, 0, 0))

    for tapahtuma in pygame.event.get():

        # Robo 1:n jutut 

        if tapahtuma.type == pygame.KEYDOWN:
            
            if tapahtuma.key == pygame.K_LEFT:
                print("vasen näppäin alas")
                r1_left = True
            
            if tapahtuma.key == pygame.K_RIGHT:
                print("oikea näppäin alas")
                r1_rigth = True
            
            if tapahtuma.key == pygame.K_UP:
                print("ylös näppäin alas")
                r1_up = True

            if tapahtuma.key == pygame.K_DOWN:
                print("alas näppäin alas")
                r1_down = True

        if tapahtuma.type == pygame.KEYUP:
            
            if tapahtuma.key == pygame.K_LEFT:
               r1_left = False
            
            if tapahtuma.key == pygame.K_RIGHT:
                r1_rigth = False

            if tapahtuma.key == pygame.K_UP:
                r1_up = False
            
            if tapahtuma.key == pygame.K_DOWN:
                r1_down = False


        # Robo 2:n jutut 

        if tapahtuma.type == pygame.KEYDOWN:
            
            if tapahtuma.key == pygame.K_a:
                print("vasen näppäin alas")
                r2_left = True
            
            if tapahtuma.key == pygame.K_d:
                print("oikea näppäin alas")
                r2_rigth = True
            
            if tapahtuma.key == pygame.K_w:
                print("ylös näppäin alas")
                r2_up = True

            if tapahtuma.key == pygame.K_s:
                print("alas näppäin alas")
                r2_down = True

        if tapahtuma.type == pygame.KEYUP:
            
            if tapahtuma.key == pygame.K_a:
               r2_left = False
            
            if tapahtuma.key == pygame.K_d:
                r2_rigth = False

            if tapahtuma.key == pygame.K_w:
                r2_up = False
            
            if tapahtuma.key == pygame.K_s:
                r2_down = False

    # yhteiset muut asiat

        if tapahtuma.type == pygame.KEYDOWN and tapahtuma.key == pygame.K_b:
            print("otetaan tauko")

        if tapahtuma.type == pygame.KEYDOWN and tapahtuma.key == pygame.K_t:
            print_text = True

    # yhteinen exit
        if tapahtuma.type == pygame.QUIT:
            exit()

    # liikkumisen määrät 

    if r1_rigth:
        robo1.move_rigth(rate_movement) 
    if r1_left:
        robo1.move_left(rate_movement) 
    if r1_up:
        robo1.move_up(rate_movement) 
    if r1_down:
        robo1.move_down(rate_movement) 
    
    if r2_rigth:
        robo2.move_rigth(rate_movement) 
    if r2_left:
        robo2.move_left(rate_movement) 
    if r2_up:
        robo2.move_up(rate_movement) 
    if r2_down:
        robo2.move_down(rate_movement) 

    # yhteiset 
    if print_text:
        naytto.blit(teksti, (200, 50))

    # asiat peliin 
    pygame.display.flip()

    # fps
    clock.tick(rate_fps)