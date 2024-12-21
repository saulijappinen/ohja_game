# Metatekstiä arvioitsijalle 
# Tarkoitus
# - pelin päätarkoitus on kerätä 10 kolikkoa
# - kolikon kerääminen nostaa robon nopeutta max 3:een 
# - hirviöitä ilmestyy pisteiden mukaan ja niihin törmääminen vähentää kolikoita (ja pistää nopeuden ykköseksi)
# Teknisiä huomioita
# - koetettu koodata niin että parametrit helppo muuttaa (max pisteet jne.). Käytännössä esim. robon maksiminopeutta ei kannata säätää liian isoksi koska muuten ei ehkä koskaan törmää kolikkoon, oveen jne. 
# - muutama asia funktioitettu mutta enemmänkin olis voinut
# - loppunäkymä tehty nyt kökösti niin että näyttö jäätyy 5 sekunniksi ja sitten pelistä tulee pakotettu exit
#   - en saanut toimimaan ajan laskemisen lopettamista pelin päättymiseen millään tavalla... 
# - hirviöiden luominen listana peliloopin sisällä tuntui omalla koneella vähemmän tökkivältä tavalta toteuttaa vs. loopin ulkopuolella

import pygame
from random import randint
from random import choice
#from time import time 

# load resources

# 1 Define classes 

class Robot: 
    def __init__(self, x: int, y:int, movement_speed: int = 1): 
        self.x = x
        self.y = y
        self.pic = pygame.image.load("./resources/robo.png")
        # for plotting
        self.width = pygame.image.load("./resources/robo.png").get_width()
        self.heigth = pygame.image.load("./resources/robo.png").get_height()
        self.center_x = self.x + self.width/2 
        self.center_y = self.y + self.heigth/2 
        self.speed = movement_speed
 
    def draw(self, screen):
        screen.blit(self.pic, (self.x, self.y))        
 
    def move_rigth(self, step = int):
        self.x += step
 
    def move_left(self, step = int):
        self.x -= step
 
    def move_up(self, step = int):
        self.y -= step
 
    def move_down(self, step = int):
        self.y += step

class Monster: 
    def __init__(self, x: int, y:int, direction = str):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("./resources/hirvio.png")
        # which direction is running 
        self.direction = direction
 
    def draw(self, screen):
        screen.blit(self.pic, (self.x, self.y))        

class Door: 
    def __init__(self):
        self.pic = pygame.image.load("./resources/ovi.png")
        # for plotting
        self.width = pygame.image.load("./resources/ovi.png").get_width()
        self.heigth = pygame.image.load("./resources/ovi.png").get_height()
        # using global parameters here, don't know if wise cause these have to be defined before door
        self.x = randint(int(object_robo.width/2), int(w_screen - self.width))
        self.y = randint(h_upper_banner, int(h_screen - self.heigth))
        self.x_center = self.x + self.width/2 
        self.y_center = self.y + self.heigth/2 
 
    def draw(self, screen):
        screen.blit(self.pic, (self.x, self.y))   

class Coin:
    def __init__(self):
        self.pic = pygame.image.load("./resources/kolikko.png")
        # for plotting
        self.width = pygame.image.load("./resources/kolikko.png").get_width()
        self.heigth = pygame.image.load("./resources/kolikko.png").get_height()
        # using global parameters here, don't know if wise cause these have to be defined before 
        self.x = randint(10, w_screen - self.pic.get_width() - 15)
        self.y = randint(h_upper_banner + 10, h_screen - self.pic.get_height() - 15)
        self.x_center = self.x + self.pic.get_width()/2 
        self.y_center = self.y + self.pic.get_height()/2

    def draw(self, screen):
        screen.blit(self.pic, (self.x, self.y)) 


# Functions

def init_screen(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    # default color = white / somehow bugs the colors, fill now in while loop stil...
    #screen.fill((0, 0, 0))
    return screen

def check_coin_encounter():
    global point_counter
    global point_max_points
    global object_robo
    global encounter_limit
    global object_coin
    if point_counter <= int(point_max_points - 1) and abs(object_robo.x + object_robo.width/2 - object_coin.x_center) <= encounter_limit and abs(object_robo.y + object_robo.heigth/2 - object_coin.y_center)  <= encounter_limit:
        # screen.blit(text_coin_found, (200, h_screen/3))
        # pygame.display.flip() # update so that text is showing
        # pygame.time.wait(1000) # 
        point_counter += 1
        # create new coin with new location
        object_coin = Coin()
        # x_coin = randint(10, w_screen - coin.get_width() - 15)
        # y_coin = randint(h_upper_banner + 10, h_screen - coin.get_height() - 15)
        # speed increase
        if object_robo.speed < max_robo_speed:
            object_robo.speed += 1
        print("coin found")


def check_monster_encounter(list_monsters):
    global point_counter
    global point_max_points
    global object_robo
    global encounter_limit
    global object_coin
    global monster_counter
    for mon in list_monsters:
        if abs(object_robo.x + object_robo.width/2 - (mon.x + w_monster/2)) <= encounter_limit and abs(object_robo.y + object_robo.heigth/2 - (mon.y + h_monster/2)) <= encounter_limit:
            print("monster encountered!")
            text_monster = font.render(plain_text_monster, True, (255, 0, 0))
            screen.blit(text_monster, (90, h_screen/3))
            pygame.display.flip() # update so that text is showing
            pygame.time.wait(2000) # 
            # robot appears in upper corner 
            object_robo = Robot(0, h_upper_banner + 5)
            monster_counter += 1
            if point_counter >= 1: 
                point_counter -= 1
            else: 
                point_counter = 0
            # decrease speed / somehow decreases always to zero?
            if object_robo.speed > 1:
                object_robo.speed -= 1


# PART 0: init screen 

w_screen = 800
h_screen = 600

screen = init_screen(w_screen, h_screen)
# start_time = pygame.time.get_ticks()



# PART 1: set game universal parameters first:  

game_name = "Robot Coin Hunt"
 
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

rate_fps = 60

point_max_points = 10

## how close to get to coins, monsters (abs)
encounter_limit = 10


# PART 2: Text parameters 

font = pygame.font.SysFont("Georgia", 20)

## upper banner height / for txt
h_upper_banner = 35

plain_text_monster = "Oh no! A monster stole one coin and slowed you down!"
plain_text_end_time = "Wuhuu! You mastered the game in"
plain_text_monster_counter = "Scary monsters encountered during coin hunt:" 
plain_text_game_exit = "The game will now close, come again!"

# PART 3: Game objects 

## 3.1 Robot 

# robot to the upper left corner always at start
# w = randint(10, w_screen-100)
# h = randint(h_upper_banner, h_screen-100)


max_robo_speed = 3 # set max speed to be achieved by collecting coins // NOT SURE IF THE ROBOT IS ABLE TO FIND STUFF IF SPEED IS TOO HIGH!
object_robo = Robot(0, h_upper_banner)


rigth = False
left = False
up = False
down = False


## 3.2 Monsters 

w_monster = pygame.image.load("./resources/hirvio.png").get_width()
h_monster = pygame.image.load("./resources/hirvio.png").get_height()

list_monsters = [] # list for all the monsters; a separate list for those already plotted in screen based on points

for _ in range(6): # 
    # not in the 0,0 corner where robot reborns 
    x_mon = randint(int(object_robo.width/2), int(w_screen - w_monster - 10))
    y_mon = choice([h_upper_banner + 5, (h_screen - h_monster)]) # can only be plotted at first to upper/lower side
    if y_mon == h_screen - h_monster:
        direction = "up"
    else: 
        direction = "down"
    monster = Monster(x_mon, y_mon, direction)
    list_monsters.append(monster)


## 3.3 Coins

object_coin = Coin() # the first coin here


## 3.4 Door 

object_door = Door() # randomized coord inside class



# Part 4: Constant parameters 

## game status
game_finalized = False

## counters 
point_counter = 0 # should be flexible 1-10
monster_counter = 0


## time
start_time = pygame.time.get_ticks()
elapsed_time = 0



elapsed_time = 0
game_finalized_time = 0



# GAME LOOP: 

while True:

    screen.fill((255, 255, 255))
 
    # plotted monsters 
    # list for plotted monsters / gets slow if outside game loop... 
    list_monsters_plotted = []
    
    # draw monsters based on points 
    if point_counter <= 1:
        list_monsters_plotted.append(list_monsters[0])
    elif point_counter <= 2:
        list_monsters_plotted.append(list_monsters[0])
        list_monsters_plotted.append(list_monsters[1])
    elif point_counter >= 3 and point_counter < 5: # those added before are already on the list
        list_monsters_plotted.append(list_monsters[0])
        list_monsters_plotted.append(list_monsters[1])
        list_monsters_plotted.append(list_monsters[2])
    elif point_counter >= 5 and point_counter < 7:
        list_monsters_plotted.append(list_monsters[0])
        list_monsters_plotted.append(list_monsters[1])
        list_monsters_plotted.append(list_monsters[2])
        list_monsters_plotted.append(list_monsters[3])
    elif point_counter >= 7 and point_counter < 9:
        list_monsters_plotted.append(list_monsters[0])
        list_monsters_plotted.append(list_monsters[1])
        list_monsters_plotted.append(list_monsters[2])
        list_monsters_plotted.append(list_monsters[3])
        list_monsters_plotted.append(list_monsters[4])
    elif point_counter >= 9:
        list_monsters_plotted.append(list_monsters[0])
        list_monsters_plotted.append(list_monsters[1])
        list_monsters_plotted.append(list_monsters[2])
        list_monsters_plotted.append(list_monsters[3])
        list_monsters_plotted.append(list_monsters[4])
        list_monsters_plotted.append(list_monsters[5])
  

    # help prints for developer 
    for mon in list_monsters: print(mon.x, mon.y, mon.direction)
    print("door location", object_door.x_center, object_door.y_center)
    print("robo is in location", object_robo.x, object_robo.y)
    print("robo center", object_robo.x + object_robo.width/2, object_robo.y + object_robo.heigth/2)
    #print("coin center", coin_center_x, coin_center_y)
    print("coin center", object_coin.x_center, object_coin.y_center)
    #print("monster location", object_monster.x, object_monster.y, "and center", object_monster.x + w_monster/2, object_monster.y + h_monster/2)

    # robo to screen
    object_robo.draw(screen)

    # Monsters
    for mon in list_monsters_plotted:
        mon.draw(screen) 

    # where to draw coins 
    if point_counter <= int(point_max_points - 1):
        object_coin.draw(screen) # when points 0, the first coin, created outside game loop 

    # check for coins and monsters        
    check_coin_encounter()
    check_monster_encounter(list_monsters_plotted)

    # Final coin collected, draw door object  
    if point_counter == int(point_max_points):
        object_door.draw(screen)

    # Enter the door / only when point_conter is max points!
    if point_counter == point_max_points and abs(point_counter == point_max_points and object_robo.x + object_robo.width/2 - object_door.x_center) <= encounter_limit and abs(object_robo.y + object_robo.heigth/2 - object_door.y_center)  <= encounter_limit:
        elapsed_time = pygame.time.get_ticks() - start_time
        game_finalized = True 

    
    # Game stats if not game finalized
    if game_finalized == False: 
        # Upper bar: point counter, time counter // could be converted to a surface? 
        pygame.draw.line(screen, (0, 0, 0), (0,h_upper_banner), (w_screen, h_upper_banner), 2)
        # - point counter
        text_point_counter = font.render(f"Coins collected: {point_counter}", True, (0, 0, 0))
        screen.blit(text_point_counter, (25, 5))
        # - game time: 
        current_time = pygame.time.get_ticks()
        gametime = int((current_time - start_time)/1000)
        #gametime = int(pygame.time.get_ticks() / 1000)
        text_timer = font.render(f"Seconds played: {gametime}", True, (0, 0, 0))
        screen.blit(text_timer, (275, 5))
        # speed 
        text_robo_speed = font.render(f"Robo speed: {object_robo.speed}", True, (0, 0, 0))
        screen.blit(text_robo_speed, (550, 5))
    
    # Final freeze screen
    if game_finalized:
        text_end = font.render(f"{plain_text_end_time} {round(float(elapsed_time / 1000), 1)} seconds", True, (255, 0, 0))
        screen.blit(text_end, (150, h_screen/3))
        text_monsters_encountered = font.render(f"{plain_text_monster_counter} {monster_counter}", True, (255, 0, 0))
        screen.blit(text_monsters_encountered, (150, h_screen/3 + 25))
        text_exit = font.render(f"{plain_text_game_exit}", True, (255, 0, 0))
        screen.blit(text_exit, (150, h_screen/3 + 50))
        # doing this in insane way because couldn't find a solution to stop the time from continuing to run
        pygame.display.flip() # update so that text is showing
        pygame.time.wait(5000) # 
        exit()

    for tapahtuma in pygame.event.get():

        # global events
        if tapahtuma.type == pygame.QUIT:
            exit()

        # if game_finalized: 
        #     game_finalized_time = pygame.time.get_ticks() - start_time
 
        # Robo movement 
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
    

 
    # Movement if game is not finalized

    if game_finalized == False:

        rate_movement_robo = object_robo.speed

        if rigth and object_robo.x < (w_screen - object_robo.width):
            object_robo.move_rigth(rate_movement_robo) 
        if left and object_robo.x >= 0:
            object_robo.move_left(rate_movement_robo) 
        if up and object_robo.y >= h_upper_banner:
            object_robo.move_up(rate_movement_robo) 
        if down and object_robo.y < (h_screen - object_robo.heigth):
            object_robo.move_down(rate_movement_robo) 

        monster_speed = min(point_counter + 1, 3) # not too fast 
        
        for mon in list_monsters_plotted: 
            
            monster_dir = mon.direction

            if abs(h_screen - mon.y) <= h_monster: # after this low point, change dir to up 
                mon.direction = "up"

            if abs(mon.y - h_upper_banner) <= 3: # three cause max speed is three 
                mon.direction = "down" 

            if monster_dir == "down":
                mon.y += monster_speed
            elif monster_dir == "up": 
                mon.y -= monster_speed
    
    #print("timer time is", timer.get_time())
    print("tick time is", pygame.time.get_ticks())
    # changes
    pygame.display.flip()
    # fps
    clock.tick(rate_fps)