import pygame
import random
import os
pygame.init()

# Add Music function
pygame.mixer.init()

# Define Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# Creating Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hungry Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 55)

# Game Icon
icon = pygame.image.load("img_icon.png")
pygame.display.set_icon(icon)

# Welcome Image
wel_img = pygame.image.load("img_welcome.png")
wel_img = pygame.transform.scale(wel_img, (screen_width, screen_height)).convert_alpha()

# Game Play Background Image
bg_img = pygame.image.load("img_bg.png")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()

# Game Over Image
over_img = pygame.image.load("img_over.png")
over_img = pygame.transform.scale(over_img, (screen_width, screen_height)).convert_alpha()

# Write Text on Screen.
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# Increase Snake length.
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Welcome Screen
def welcome():
    pygame.mixer.music.load('music_welcome.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        # pygame.mixer.music.stop()
        gameWindow.fill((0,0,0))
        gameWindow.blit(wel_img, (0, 0))
        # text_screen("Welcome to Hungry Snakes World", white, 160,250)
        # text_screen("Press Space Bar to Play", white, 232, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
            
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 50
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    score = 0
    fps = 60
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(55, screen_width/2)
    snk_list = []
    snk_length = 1

     # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    #while - GAME LOOP
    while not exit_game:
        #Game OVER
        if game_over:
            # Update Hi-Score
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            # text_screen("Game Over! Press Enter To Restart", red, 140, 250)
            gameWindow.blit(over_img, (0, 0))
            text_screen("Score: "+ str(score)+"      Hi-Score: "+ str(hiscore), white, 275, 420)

            # Game Over.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                # Game Exit.
                if event.type == pygame.QUIT:
                    exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            # Movements - Turn Right, Left, Up and Down.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Cheat Code - If You Press i Button. Your Score will increase by 10. [Enjoy!!]
                    if event.key == pygame.K_i:
                        score += 10
            
            # Increase Co-ordinates
            snake_x += velocity_x
            snake_y += velocity_y
            
            # Eat Food & Update Score
            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score += 10
                pygame.mixer.music.load('music_eat.mp3')
                pygame.mixer.music.play()
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(55, screen_width/2)
                snk_length += 5
                if int(hiscore) < score:
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bg_img, (0, 0))
            text_screen("                      Score: "+ str(score)+"          Hi-Score: "+ str(hiscore), black, 5, 7)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True
                # Game Over Music
                pygame.mixer.music.load('music_over.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<50 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('music_over.mp3')
                pygame.mixer.music.play()
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
            # Game Border
            pygame.draw.rect(gameWindow, black, [1, 50, screen_width, screen_height],4)
            pygame.draw.rect(gameWindow, black, [1, 1, screen_width, screen_height],4)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

# Game Starts
welcome()