import pygame
import random
pygame.init()
snake_height = 10
snake_width =10
snake_color = (200,0,0)
food_color = (255,255,255)
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
snakeB = [[150,40]]
background_color = (0,0,0)
game_over = False
snakeP = [150,40]
startx = 100
starty = 100
FPS = 15
fpsclock = pygame.time.Clock()
direction = 0
X = 600
Y = 50
Fy = 100
Fx = 200
Fruit = [Fx,Fy]
direction1 = 0
wall_color = (255,255,0)
n = 0
score = 0
font = pygame.font.SysFont(None, 24)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction1 = 1

            if event.key == pygame.K_RIGHT:
                direction1 = 2

            if event.key == pygame.K_UP:
                direction1 = 3

            if event.key == pygame.K_DOWN:
                direction1 = 4
    if direction1 == 1 and direction != 2:
        direction = 1

    if direction1 == 2 and direction != 1:
        direction = 2

    if direction1 == 3 and direction != 4:
        direction = 3

    if direction1 == 4 and direction != 3:
        direction = 4

    if direction == 1:
        snakeP[0] = snakeP[0] - 5

    elif direction == 2:
        snakeP[0] = snakeP[0] + 5

    elif direction == 3:
        snakeP[1] = snakeP[1] - 5

    elif direction == 4:
        snakeP[1] = snakeP[1] + 5
    won = snakeP[1]
    won2 = snakeP[0]
    if snakeP[0] in range(Fx - 10, (Fx + 10) + 1) and snakeP[1] in range(Fy - 10, (Fy + 10) + 1):
        ranx = random.randint(10, 800)
        rany = random.randint(10, 600)
        Fx = ranx
        Fy = rany
        FPS = FPS + 1
        score  = score + 5
    else:
        snakeB.pop()

    if snakeP[1] in range(0, 600) and snakeP[0] == 800:
        snakeP[0] = 0
        snakeP[1] = won
    if snakeP[0] in range(0, 800) and snakeP[1] == 600:
        snakeP[1] = 0
        snakeP[0] = won2
    if snakeP[1] in range(0, 600) and snakeP[0] == 0:
        snakeP[0] = 800
        snakeP[1] = won

    if snakeP[0] in range(0, 800) and snakeP[1] == 0:
        snakeP[1] = 600
        snakeP[0] = won2
    for k in snakeB:
        if snakeP[0] == k[0] and snakeP[1] == k[1]:
            pygame.quit()

    snakeB.insert(0, list(snakeP))
    screen.fill(background_color)
    pygame.draw.circle(screen, food_color, (Fx, Fy), 5)
    for P in snakeB:
        pygame.draw.rect(screen, snake_color, pygame.Rect(P[0], P[1], 10, 10))
    img = font.render(str(score), True, wall_color)
    screen.blit(img, (20, 20))
    pygame.draw.rect(screen, snake_color, pygame.Rect(0, 0, 5, 600))
    pygame.draw.rect(screen, snake_color, pygame.Rect(0, 595, 800 , 5))

    pygame.display.update()
    fpsclock.tick(FPS)
pygame.quit()