import pygame
import random

WIDTH = 1920
HEIGHT = 1020
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Simulator 18")

LB = 173,216,230

FPS = 120

VEL = 3

MONKEY_WIDTH, MONKEY_HEIGHT = 100, 100
BANANA_WIDTH, BANANA_HEIGHT = 40, 25

#monkey
MONKEY_CHARACTER = pygame.image.load(
    'monkey.png')
MONKEY_CHARACTER = pygame.transform.scale(MONKEY_CHARACTER,(MONKEY_WIDTH, MONKEY_HEIGHT))

#banana
BANANA_TARGET = pygame.image.load(
    'banana.png')
BANANA_TARGET = pygame.transform.scale(BANANA_TARGET,(BANANA_WIDTH,BANANA_HEIGHT))




def draw_window(monkey, banana):
    WIN.fill(LB)
    WIN.blit(BANANA_TARGET,(banana.x, banana.y))
    WIN.blit(MONKEY_CHARACTER, (monkey.x, monkey.y))
    pygame.display.update()

def monkey_movement(keys_pressed, monkey):
     #left
    if keys_pressed[pygame.K_a] and monkey.x - VEL > 0: 
        monkey.x -= VEL
      #right
    if keys_pressed[pygame.K_d] and monkey.x + VEL < 1830:
        monkey.x += VEL
    #up
    if keys_pressed[pygame.K_w] and monkey.y + VEL > 0:
        monkey.y -= VEL
    #down
    if keys_pressed[pygame.K_s] and monkey.y - VEL < 900:
        monkey.y += VEL

def main():

    start_time = pygame.time.get_ticks()
    banana_active = True
    banana_active_time = 2500
    banana_inactive_time = 1000

    rsp_x = random.randrange(0, WIDTH)
    rsp_y = random.randrange(0, HEIGHT)

    monkey_rect = pygame.Rect(700, 300, MONKEY_WIDTH, MONKEY_HEIGHT)
    banana_rect = pygame.Rect(rsp_x,rsp_y,BANANA_WIDTH, BANANA_HEIGHT)
    monkey = (MONKEY_CHARACTER,monkey_rect)
    banana = (BANANA_TARGET,banana_rect)
    active_gameobjects = [monkey,banana]
    clock = pygame.time.Clock()

    run = True
    while run:
        if banana_active:
            print(pygame.time.get_ticks())
            if (pygame.time.get_ticks() - start_time) > banana_active_time:
                if banana in active_gameobjects:
                    active_gameobjects.remove(banana)
                start_time = pygame.time.get_ticks()
                banana_active = False
                banana[1].x = random.randrange(0,800)
                banana[1].y = random.randrange(0,800)
        else:
            if (pygame.time.get_ticks() - start_time) > banana_inactive_time:
                if banana not in active_gameobjects:
                    active_gameobjects.append(banana)
                start_time = pygame.time.get_ticks()
                banana_active = True

        WIN.fill(LB)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False        

        keys_pressed = pygame.key.get_pressed()
        monkey_movement(keys_pressed, monkey_rect)

        for gameobject in active_gameobjects:
            WIN.blit(gameobject[0],(gameobject[1].x, gameobject[1].y))

        pygame.display.update()
        


if __name__ == "__main__":
    main()
