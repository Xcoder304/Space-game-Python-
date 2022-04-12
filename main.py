import random
from tkinter import font
import pygame
import math
from pygame import mixer
pygame.init()


screen = pygame.display.set_mode((1366,800))

# changing the title of the window of the pygame
pygame.display.set_caption("Space Battle")

# change the icon of pygame window
icon = pygame.image.load('D:\Coding\Python\pygame\paratice\Space Game\\icon.png')
pygame.display.set_icon(icon)
runWin = True 

mixer.music.load('D:\Coding\Python\pygame\paratice\Space Game\\background.wav')
mixer.music.play(-1)
# score
points = 0
font = pygame.font.Font('freesansbold.ttf',32)

# game Over Font
gameOverFont = pygame.font.Font('freesansbold.ttf',70)

def GameOver():
    show_gameOver = gameOverFont.render("GAME OVER",True,(255,255,255))
    screen.blit(show_gameOver,(500,300))
    gameOverSound = mixer.Sound('D:\Coding\Python\pygame\paratice\Space Game\\gameOver.wav')
    gameOverSound.play(1)

textX = 10
textY = 20 

def show_score(x,y):
    show = font.render("Score : "+str(points), True , (255,255,255))
    screen.blit(show,(x,y))
# adding the player
playerimg = pygame.image.load('D:\Coding\Python\pygame\paratice\Space Game\\player.png')
playerX = 683
playerX_change = 0
playerY = 700
playerY_change = 0  
def Player(x,y):
    screen.blit(playerimg,(x,y))

# making the enemy

# making multipal enemys 
enemyimg = []
enemyX = []
enemyX_change = []
enemyY = []
enemyY_change = []
enemyY_change = []
number_of_enmey = 12

for i in range(number_of_enmey):
    enemyimg.append(pygame.image.load('D:\Coding\Python\pygame\paratice\Space Game\\alien2.png'))
    enemyX.append(random.randint(0,1300))
    enemyX_change.append(3)
    enemyY.append(random.randint(0,150))
    enemyY_change.append(40)


def Enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

# for the bullet
bulletimg = pygame.image.load('D:\Coding\Python\pygame\paratice\Space Game\\bullet.png')
bulletX = 0
bulletY = 700
bulletY_change = 6.2
bullet_state = "ready"

def Fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x,y+10))

def Collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# looping the window 
while runWin:
    screen.fill((26,26,26))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            runWin = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                playerX_change += -0.7
            if events.key == pygame.K_UP:
                playerY_change = -0.7
            if events.key == pygame.K_RIGHT:
                playerX_change += 0.7
            if events.key == pygame.K_DOWN:
                playerY_change = 0.7
            if events.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet_sound = mixer.Sound('D:\Coding\Python\pygame\paratice\Space Game\\laser.wav')
                    bullet_sound.play()
                    Fire_bullet(bulletX,bulletY)
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                playerX_change = 0 
            if events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # making the boundaries around the window 
    if playerX <= 0:
        playerX = 0

    elif playerX > 1300:
        playerX = 1300

    if playerY > 710:
        playerY = 710

    if playerY < 200:
        playerY = 200

    # for the enemy
    for i in range(number_of_enmey):

        # game over
        if enemyY[i] > 670:
            for j in range(number_of_enmey):
                enemyY[j] = 2000
            GameOver()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] > 1300:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        isCollision = Collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if isCollision:
            bulletY = 700
            bullet_state = "ready"
            points += 1
            print(points)
            enemyX[i] = random.randint(0,1300)
            enemyY[i] = random.randint(0,150)
            explostion = mixer.Sound('D:\Coding\Python\pygame\paratice\Space Game\\explosion.wav')
            explostion.play()
            
        Enemy(enemyX[i],enemyY[i],i)
        
    # for bullet fire

# for multipal bullets
    if bulletY <= 0:
        bulletY = 700
        bullet_state = "ready"

    if bullet_state is "fire":
        Fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    show_score(textX,textY)
    Player(playerX,playerY)
    pygame.display.update()