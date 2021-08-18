import pygame
import random
import socket
import threading
host = "0.0.0.0"  # '#'127.0.0.1'
port = 5555
global soc
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((host, port))


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
wall_color = (255,10,100)
wall_color1 = (255,100,100)
n = 0
score = 0
font = pygame.font.SysFont(None, 24)
def get_min_max(window):
    min_window = min(window)
    max_window = max(window)
    min_index = window.index(min_window)
    max_index = window.index(max_window)
    diff = max_window - min_window
    return diff,max_index,min_index

def phone():
    x_data = []
    y_data = []
    z_data = []
    count = 0
    window_size = 70
    skip_size = 40
    thresh = 12.0
    last_checked = 0
    start_w = 0
    end_w = window_size
    is_valid = False
    global game_over
    global direction
    while count < 1000:
        # print('waiting...')
        message, address = soc.recvfrom(1024)
        # print(message)
        # print("received message: %s" % message)
        res = message
        res = (res.rstrip()).lstrip()
        res = res.decode("utf-8")
        data = res.split(",")

        data = [float(x) for x in data[2:5]]
        # print(data)
        x_data.append(data[0])
        y_data.append(data[1])
        z_data.append(data[2])
        count += 1
        if (count > window_size and (end_w - start_w) >= window_size and len(x_data) >= end_w):
            window_x = x_data[start_w:end_w]
            window_z = z_data[start_w:end_w]
            print("window length:", len(window_x))
            delta_x, max_i_x, min_i_x = get_min_max(window_x)
            delta_z, max_i_z, min_i_z = get_min_max(window_z)

            if delta_x > delta_z:
                dir = 'x'
                delta = delta_x
                min_index = min_i_x
                max_index = max_i_x
            else:
                dir = 'z'
                delta = delta_z
                min_index = min_i_z
                max_index = max_i_z

            if delta > thresh:
                if min_index < max_index:
                    if dir == 'x':
                        print("left", delta)
                        direction1 = 1
                    else:
                        print("down", delta)
                        direction1 = 4
                else:
                    if dir == 'x':
                        print("right", delta)
                        direction1 = 2
                    else:
                        print("up", delta)
                        direction1 = 3
                is_valid = True

            if is_valid:
                start_w += window_size
                end_w += window_size
            else:
                start_w += skip_size
                end_w += skip_size

thread1 = threading.Thread(target=phone, args=())
thread1.start()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1

            if event.key == pygame.K_RIGHT:
                direction = 2

            if event.key == pygame.K_UP:
                direction = 3

            if event.key == pygame.K_DOWN:
                direction = 4


    if direction == 1:
        snakeP[0] = snakeP[0] - 5

    elif direction == 2:
        snakeP[0] = snakeP[0] + 5

    elif direction == 3:
        snakeP[1] = snakeP[1] - 5

    elif direction == 4:
        snakeP[1] = snakeP[1] + 5


    if snakeP[0] in range(Fx - 20,(Fx + 20)+ 1) and snakeP[1] in range(Fy -20,(Fy + 20)+1):
        ranx = random.randint(10, 800)
        rany = random.randint(10, 600)
        Fx = ranx
        Fy = rany
        FPS = FPS + 1
        score = score + 5
    else:
        snakeB.pop()


    if snakeP[1] in range(0,600) and snakeP[0] == 795:
        pygame.quit()

    if snakeP[0] in range(0,800) and snakeP[1] == 595:
        pygame.quit()

    if snakeP[1] in range(0,600) and snakeP[0] == 5:
        pygame.quit()

    if snakeP[0] in range(0,800) and snakeP[1] == 5:
        pygame.quit()
    for k in snakeB:
        if snakeP[0] == k[0] and snakeP[1] == k[1]:
            pygame.quit()

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
        snakeB.insert(0, list(snakeP))
        if snakeP[0] in range(Fx - 10, (Fx + 10) + 1) and snakeP[1] in range(Fy - 10, (Fy + 10) + 1):
            ranx = random.randint(10, 800)
            rany = random.randint(10, 600)
            Fx = ranx
            Fy = rany
            FPS = FPS + 1
        else:
            snakeB.pop()

        if snakeP[1] in range(0, 600) and snakeP[0] == 795:
            pygame.quit()

        if snakeP[0] in range(0, 800) and snakeP[1] == 595:
            pygame.quit()

        if snakeP[1] in range(0, 600) and snakeP[0] == 5:
            pygame.quit()

        if snakeP[0] in range(0, 800) and snakeP[1] == 5:
            pygame.quit()
        for k in snakeB:
            if snakeP[0] == k[0] and snakeP[1] == k[1]:
                pygame.quit()
        if snakeP[0] in range(600, 610) and snakeP[1] in range(50, 150) or snakeP[0] in range(0, 10) and snakeP[
            1] in range(300, 400) or snakeP[0] in range(400, 410) and snakeP[1] in range(300, 400):
            pygame.quit()


        screen.fill(background_color)
        pygame.draw.circle(screen, food_color, (Fx, Fy), 5)
        for P in snakeB:
            pygame.draw.rect(screen, snake_color, pygame.Rect(P[0], P[1], 10, 10))

        pygame.draw.rect(screen, wall_color, pygame.Rect(X, Y, 10, 100))
        pygame.draw.rect(screen, wall_color, pygame.Rect(0, 300, 10, 100))
        pygame.draw.rect(screen, wall_color, pygame.Rect(400, 300, 10, 100))
        pygame.draw.rect(screen, wall_color1, pygame.Rect(0, 0, 5, 600))

        pygame.draw.rect(screen, wall_color1, pygame.Rect(0, 595, 800, 5))

        pygame.draw.rect(screen, wall_color1, pygame.Rect(0, 0, 800, 5))

        pygame.draw.rect(screen, wall_color1, pygame.Rect(795, 0, 5, 600))

        img = font.render(str(score), True, wall_color)
        screen.blit(img, (20, 20))
        pygame.display.update()
        fpsclock.tick(FPS)
    pygame.quit()
    screen.fill(background_color)
    pygame.draw.circle(screen,food_color,(Fx,Fy),5)
    for P in snakeB:
        pygame.draw.rect(screen, snake_color,pygame.Rect(P[0],P[1], 25, 25))


    img = font.render(str(score), True, wall_color)
    screen.blit(img, (20, 20))
    pygame.display.update()
    fpsclock.tick(FPS)
pygame.quit()
