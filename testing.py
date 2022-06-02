import pygame
import time
 
 
# initializing pygame
 
pygame.init()
 
# defining variables
 
clock = pygame.time.Clock()
ver = "Beta 0.0.0.1"
autog = 0
coins = 0
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
light_blue = (173, 216, 230)
grey = (128, 128, 128)
blue = (0, 100, 250)
bitcoin_logo = pygame.image.load(r'bitcoin.png')
bitcoin_logo = pygame.transform.scale(bitcoin_logo, (200, 200)) 

# creating display and caption
 
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Crypto Miner")
 
# defining functions
 
def circle(display, color, x, y, radius):
    pygame.draw.circle(display, color, [x, y], radius)
 
def autominer():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog
 
 
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)
 
 
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
 
 
def main_loop():
    global clock
    global autog
    global ver
    global color1
    global color2
    global color3
    mong = 1
    cost = 50
    cost2 = 50
    global coins
    game_running = True
    while game_running:
        if game_running: 
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos[0] >= 300:
                    if mopos[0] <= 500:
                        if mopos[1] >= 300:
                            if mopos[1] <= 500:
                                coins += mong
 
                if mopos <= (800, 0):
                    if mopos >= (600, 0):
                        if coins >= cost:
                            coins = coins - cost
                            cost = cost * 1.5
                            mong = mong * 1.1
                            cost = round(cost, 0)
 
                if mopos >= (50, 0):
                    if mopos <= (245, 0):
                        if coins >= cost2:
                            coins = coins - cost2
                            cost2 = cost2 * 1.5
                            autog = autog + 0.5
                            cost2 = round(cost2, 0)
 
                if coins == 2147483647:
                    print("You Beat the game")
                    game_running = False
 
 
 
        # drawing stuff
 
        gameDisplay.fill(light_blue)
        DrawText("Crypto Miner", black, light_blue, 400, 100, 50)
        DrawText("you have " + str(f'{coins:.2f}') + " bitcoins", black, light_blue, 100, 50, 20)
        DrawText("upgrade blokchain " + str(cost), black, light_blue, 700, 300, 20)
        DrawText("buy gpu miner " + str(cost2), black, light_blue, 150, 370, 20)
        DrawText("Version: " + ver, black, light_blue, 650, 50, 20)
        rectangle(gameDisplay, blue, 50, 400, 200, 300)
        gameDisplay.blit(bitcoin_logo, (300,300))
        rectangle(gameDisplay, blue, 600, 317, 200, 300)
        pygame.display.update()
        clock.tick(60)
 
# ending the program
 
main_loop()
pygame.quit()
quit()