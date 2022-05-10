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
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 30

#Bala
#Bala - Não é possível ver a bala na tela
#fire - a bala está se movendo
bulletImg = pygame.image.load('001-bullet.png')
bulletX = 0
bulletY = 480
bullet_change = 0
bulletY_change = 0.5
bullet_state = 'pronto'

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


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
                fire_bullet(playerX, bulletY)

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
    if bullet_state is 'fire':
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
