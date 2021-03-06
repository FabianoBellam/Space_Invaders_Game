import math
import random
import pygame
import sys
from pygame import mixer

# Inicializando o pygame
pygame.init()

# Criar tela do jogo
screen = pygame.display.set_mode((800, 600))

# Image de fundo
background = pygame.image.load('Space_background.jpg')

# Música de fundo
mixer.music.load('background.wav')
mixer.music.play(-1)

# Alterar Titulo e Icone da Página
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('001-spaceship.png')
pygame.display.set_icon(icon)

# Jogador
playerImg = pygame.image.load('001-arcade-game.png')
playerX = 370
playerY = 480
playerX_change = 0

# Inimigo(s)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('001-enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.4)
    enemyY_change.append(30)

# Bala
# Armado (Não é possível ver a bala na tela)
# Fire (a bala está em movimento)
bulletImg = pygame.image.load('001-bullet.png')
bulletX = 0
bulletY = 480
bullet_change = 0
bulletY_change = 0.85
bullet_state = 'armado'

# Definindo um marcador de pontuação
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Vari[aveis para determinar a localização do Score na tela
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    # usada a formula abaixo para calcular a distância entre duas duas cordenadas
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:  # valor em pixels
        return True
    else:
        return False


# Criando um loop para a tela do jogo continuar aberta
running = True
while running:

    # Colocando cor no fundo da tela - RGB
    screen.fill((102, 204, 0))

    # Imagem de fundo
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Verificador se a tecla para esq. ou dir. foi pressionada
        if event.type == pygame.KEYDOWN:
            # print('Uma tecla foi pressionada')
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state == 'armado':
                    # Introduzindo som de disparo da bala
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()

                    # Para obter a coordenada 'X' da espaçonave no momento do tiro e armazenar na variável
                    # em seguida dispara o tiro usando a variavél como coordenada
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Faz a somatoria dos movimentos quando as teclas de setas são precionadas,
    # movimentando a espaçonave na tela
    playerX += playerX_change

    # Mantem a espaçonave dentro dos limites da janela
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Movimento do inimigo na tela
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        # Mantem a inimigo dentro dos limites da janela
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]

        # Colisão entre a bala e o alienígena
        colisao = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if colisao:
            # Introduzindo som de explosão quando o alien é atingido
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()

            bulletY = 480
            bullet_state = 'armado'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Movimento da bala
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'armado'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
