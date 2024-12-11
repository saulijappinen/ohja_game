# dev game here 

import pygame
from random import randint
from random import choice
from time import time 

# load resources

# 1 Define classes 
# - classes: robot, monster, cause they both move
# - just appear: coins. and door?  


class Robot: 
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("./resources/robo.png")
        # for plotting
        self.width = pygame.image.load("./resources/robo.png").get_width()
        self.heigth = pygame.image.load("./resources/robo.png").get_height()
        self.center_x = self.x + self.width/2 
        self.center_y = self.y + self.heigth/2 
 
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
    def __init__(self, x: int, y:int, direction = str):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("./resources/hirvio.png")
        # which direction is running 
        self.direction = direction
 
    def draw(self, naytto):
        naytto.blit(self.pic, (self.x, self.y))        
 

# pelin aloitus ja näytön speksaus
 
pygame.init()

start_time = time()

w_screen = 800
h_screen = 600
 
naytto = pygame.display.set_mode((w_screen, h_screen))
pygame.display.set_caption("Robot Coin Rally")
 
clock = pygame.time.Clock()
 
# parametrit 
 
rate_fps = 60



# objects

## upper banner height / for txt
h_upper_banner = 35

# robot to the upper left corner always at start
# w = randint(10, w_screen-100)
# h = randint(h_upper_banner, h_screen-100)

object_robo = Robot(0, h_upper_banner)
rate_movement_robo = 1 

rigth = False
left = False
up = False
down = False


## monsters ---- 

w_monster = pygame.image.load("./resources/hirvio.png").get_width()
h_monster = pygame.image.load("./resources/hirvio.png").get_height()

list_monsters = [] # this list works, just need to get directions working for these 
for _ in range(6): # every second point from 1 onwards  
    # not in the 0,0 corner where robot reborns 
    x_mon = randint(int(object_robo.width/2), int(w_screen - w_monster - 10))
    y_mon = choice([h_upper_banner + 5, (h_screen - h_monster)]) # can only be plotted at first to upper/lower side
    if y_mon == h_screen - h_monster:
        direction = "up"
    else: 
        direction = "down"
    monster = Monster(x_mon, y_mon, direction)
    list_monsters.append(monster)

coin = pygame.image.load("./resources/kolikko.png")

# x_coin = randint(0, 300)
# y_coin = randint(0, 400)

x_coin = 300
y_coin = 400

# for plotting / could also be just the center that should be hit?
# coin_rigth_border = x_coin + coin.get_width()
# coin_down_border = y_coin + coin.get_height()
coin_center_x = x_coin + coin.get_width()/2
coin_center_y = y_coin + coin.get_height()/2


door = pygame.image.load("./resources/ovi.png")
# door_x = w_screen-100
# door_y = h_screen-100
door_x = randint(int(object_robo.width/2), int(w_screen - door.get_width()/2))
door_y = randint(h_upper_banner, int(h_screen - door.get_height()/2))

door_center_x = door_x + door.get_width()/2
door_center_y = door_y + door.get_height()/2



# first values: 

point_counter = 0 
point_max_points = 10

game_finalized = False

# texts

font = pygame.font.SysFont("Georgia", 20)
text_coin_found = font.render("Coin found, you are a rich robot!", True, (255, 0, 0))

# time
#start_time = pygame.time.get_ticks()
elapsed_time = 0


encounter_limit = 10
# game 

# Alustaa pelin
# scr = init() 
timer = pygame.time.Clock()
# sys time and sys.time - start time and this would be visible 




while True:

    print("taas alkoi pelikierros")
    print(len(list_monsters))
    naytto.fill((255, 255, 255))
 
    object_robo.draw(naytto)


    # plotted monsters 
    # list for plotted monsters
    list_monsters_plotted = []
    
    # draw monsters based on points 
    if point_counter <= 1:
        list_monsters_plotted.append(list_monsters[0])
    elif point_counter <= 2:
        list_monsters_plotted.append(list_monsters[0])
        list_monsters_plotted.append(list_monsters[1])
    elif point_counter >= 3 and point_counter < 5: 
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


    for mon in list_monsters_plotted:
        mon.draw(naytto)

    # robot's outer limits 
    robot_border_right = object_robo.x + object_robo.width
    robot_border_down = object_robo.y + object_robo.heigth
    #robot_center = object_robo.x + object_robo.width/2


    # where to draw coins 
    if point_counter <= int(point_max_points - 1):
        naytto.blit(coin, (x_coin, y_coin))
        coin_center_x = x_coin + coin.get_width()/2
        coin_center_y = y_coin + coin.get_height()/2

    # Upper bar: point counter, time counter // could be converted to a surface? 
    pygame.draw.line(naytto, (0, 0, 0), (0,h_upper_banner), (w_screen, h_upper_banner), 2)
    # - point counter
    text_point_counter = font.render(f"Coins collected: {point_counter}", True, (0, 0, 0))
    naytto.blit(text_point_counter, (25, 5))
    # - game time: 
    gametime = int(pygame.time.get_ticks() / 1000) # ms -> s
    text_timer = font.render(f"Seconds played: {gametime}", True, (0, 0, 0))
    naytto.blit(text_timer, (275, 5))
    # speed 
    text_robo_speed = font.render(f"Robo speed: {rate_movement_robo}", True, (0, 0, 0))
    naytto.blit(text_robo_speed, (550, 5))




    # help prints to developer 
    for mon in list_monsters: print(mon.x, mon.y, mon.direction)
    print("door location", door_center_x, door_center_y)
    print("robo is in location", object_robo.x, object_robo.y, "and its borders are", robot_border_right, robot_border_down)
    print("robo center", object_robo.x + object_robo.width/2, object_robo.y + object_robo.heigth/2)
    print("coin center", coin_center_x, coin_center_y)
    # Coin found 
    # - 3 coord points offset ok from center 
    if point_counter <= int(point_max_points - 1) and abs(object_robo.x + object_robo.width/2 - coin_center_x) <= encounter_limit and abs(object_robo.y + object_robo.heigth/2 - coin_center_y)  <= encounter_limit:
        naytto.blit(text_coin_found, (w_screen/2, 100))
        point_counter += 1
        x_coin = randint(10, w_screen - coin.get_width() - 15)
        y_coin = randint(h_upper_banner + 10, h_screen - coin.get_height() - 15)
        if rate_movement_robo == 1:
            rate_movement_robo = 2

    # Final coin collected, show door 
    if point_counter == int(point_max_points):
        naytto.blit(door, (door_x, door_y))


    # Enter the door / only when point_conter is max points!
    if point_counter == point_max_points and abs(point_counter == point_max_points and object_robo.x + object_robo.width/2 - door_center_x) <= encounter_limit and abs(object_robo.y + object_robo.heigth/2 - door_center_y)  <= encounter_limit:
        # stop all movement
        game_finalized = True 
        end_time = time()


    # Monster encounter 

    for mon in list_monsters_plotted: ## MUST BE FOR THOSE THAT HAVE BEEN PLOTTED, OTHERWISE THE COLLISION COMES WITH MONSTERS THAT NOT YET PLOTTED!
        
        if abs(object_robo.x + object_robo.width/2 - (mon.x + w_monster/2)) <= encounter_limit and abs(object_robo.y + object_robo.heigth/2 - (mon.y + h_monster/2)) <= encounter_limit:
            print("monster encountered!")
            text_monster = font.render(f"Oh no, unfriendly monster took your coin!", True, (255, 0, 0))
            naytto.blit(text_monster, (150, h_screen/2))
            pygame.time.wait(500) # 
            # robot appears in upper corner 
            object_robo = Robot(0, h_upper_banner + 5)
            if point_counter >= 1: 
                point_counter -= 1
            else: 
                point_counter = 0
            # decrease speed
            if rate_movement_robo == 2:
                rate_movement_robo = 1
        

    # game end 
    if game_finalized:
        elapsed_time = end_time - start_time ## FIXME!
        text_end = font.render(f"Wuhuu, you finalized the game in: {elapsed_time} seconds", True, (255, 0, 0))
        naytto.blit(text_end, (150, h_screen/2))


    for tapahtuma in pygame.event.get():
 
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
    
 
 
    # yhteinen exit
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    # Movement if game is not finalized

    if game_finalized == False:

        if rigth and object_robo.x < (w_screen - object_robo.width):
            object_robo.move_rigth(rate_movement_robo) 
        if left and object_robo.x >= 0:
            object_robo.move_left(rate_movement_robo) 
        if up and object_robo.y >= h_upper_banner:
            object_robo.move_up(rate_movement_robo) 
        if down and object_robo.y < (h_screen - object_robo.heigth):
            object_robo.move_down(rate_movement_robo) 

        # - monsters
        #random = randint(1, 4)

        monster_speed = min(point_counter + 1, 3) # not too fast 
        
        for mon in list_monsters_plotted: #CONTINUE FROM THIS!
            
            monster_dir = mon.direction

            if abs(h_screen - mon.y) <= h_monster: # after this low point, change dir to up 
                mon.direction = "up"

            if abs(mon.y - h_upper_banner) <= 3: # three cause max speed is three 
                mon.direction = "down" 

            if monster_dir == "down":
                mon.y += monster_speed
            elif monster_dir == "up": 
                mon.y -= monster_speed

 
    # yhteiset 
    # if print_text:
    #     naytto.blit(teksti, (200, 50))
 
    # asiat peliin 
    pygame.display.flip()
 
    # fps
    clock.tick(rate_fps)# dev game here 

