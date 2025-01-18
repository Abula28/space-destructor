import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_START_X = SCREEN_WIDTH / 2 - 32
PLAYER_START_Y = SCREEN_HEIGHT / 2 + 200

MOVEMENT_SPEED = 0.3
ENEMY_Y_CHANGE = 40

font = pygame.font.SysFont('sans-serif', 32)
game_over_font = pygame.font.SysFont('sans-serif', 64)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.transform.scale(pygame.image.load(
    'background.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space destructor")

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

score_value = 0
game_over = False

playerImg = pygame.transform.scale(pygame.image.load('player.png'), (64, 64))
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.transform.scale(
        pygame.image.load('enemy.png'), (32, 32)))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 90))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(MOVEMENT_SPEED)
    enemyY_change.append(ENEMY_Y_CHANGE)

bulletImg = pygame.transform.scale(pygame.image.load('bullet.png'), (32, 32))
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = MOVEMENT_SPEED
bullet_state = False


def show_score():
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (10, 10))


def game_over_text():
    over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = True
    screen.blit(bulletImg, (x + 16, y + 10))


def collition(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)) < 27


run = True

while run:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    if game_over:
        show_score()
        game_over_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= MOVEMENT_SPEED
            if event.key == pygame.K_RIGHT:
                playerX_change += MOVEMENT_SPEED

            if event.key == pygame.K_SPACE:
                if not bullet_state:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # ========= PLAYER =========
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64

    # ========= ENEMY =========

    for i in range(num_of_enemies):
        if collition(playerX, playerY, enemyX[i], enemyY[i]):
            game_over = True
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = MOVEMENT_SPEED
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= SCREEN_WIDTH - 32:
            enemyX_change[i] = -MOVEMENT_SPEED
            enemyY[i] += enemyY_change[i]

        if collition(enemyX[i], enemyY[i], bulletX, bulletY) and bullet_state:

            bulletY = PLAYER_START_Y
            bullet_state = False
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 90)
            enemyY[i] = random.randint(50, 150)
            score_value += 1

            if score_value % 3 == 0:
                num_of_enemies += 1
                enemyImg.append(pygame.transform.scale(
                    pygame.image.load('enemy.png'), (32, 32)))
                enemyX.append(random.randint(0, SCREEN_WIDTH - 90))
                enemyY.append(random.randint(50, 150))
                enemyX_change.append(MOVEMENT_SPEED)
                enemyY_change.append(ENEMY_Y_CHANGE)

        enemy(enemyX[i], enemyY[i], i)

    # ========= BULLET =========

    if bulletY <= 0:
        bullet_state = False
        bulletY = PLAYER_START_Y

    if bullet_state:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # ========= COLLISIONS =========

    player(playerX, playerY)
    show_score()
    pygame.display.update()
