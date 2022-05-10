import math
import pygame
import random

# Inicializando o pygame
pygame.init()

# Criar tela do jogo
screen = pygame.display.set_mode((800, 600))

#Image de fundo
background = pygame.image.load('Space_background.jpg')

# Alterar Titulo e Icone da Página
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('001-spaceship.png')
pygame.display.set_icon(icon)

# Jogador
playerImg = pygame.image.load('001-arcade-game.png')
playerX = 370
playerY = 480
playerX_change = 0

# Inimigo
enemyImg = pygame.image.load('001-enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 30

#Bala
#Armado - Não é possível ver a bala na tela
#fire - a bala está se movendo
bulletImg = pygame.image.load('001-bullet.png')
bulletX = 0
bulletY = 480
bullet_change = 0
bulletY_change = 0.75
bullet_state = 'armado'

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    #usada a formula abaixo para calcular a distância entre duas duas cordenadas
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27: #valor em pixels
        return True
    else:
        return False


# Criando um loop para a tela do jogo continuar aberta
running = True
while running:

    # Colocando cor no fundo da tela - RGB
    screen.fill((102, 204, 0))
    #Imagem de fundo
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Verificador se a tecla para esq. ou dir. foi pressionada
        if event.type == pygame.KEYDOWN:
            #print('Uma tecla foi pressionada')
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == 'armado':
                    #Para obter a coordenada 'X' da espaçonave no momento do tiro e armazenar na variável
                    #em seguida dispara o tiro usando a variavél como coordenada
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Faz a somatoria dos movimentos quando as telas de setas são precionadas,
    #movimentando a espaçonave na tela
    playerX += playerX_change

    #Mantem a espaçonave dentro dos limites da janela
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Faz a somatoria dos movimentos quando as telas de setas são precionadas,
    # movimentando o inimigo na tela
    enemyX += enemyX_change

    # Mantem a inimigo dentro dos limites da janela
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    #Movimento da bala
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'armado'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Colisão entre a bala e o alienígena
    colisao = isCollision(enemyX, enemyY, bulletX, bulletY)
    if colisao:
        bulletY = 480
        bullet_state = 'armado'
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
