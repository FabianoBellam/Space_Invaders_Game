import pygame

#Inicializando o pygame
pygame.init()

#Criar tela do jogo
screen = pygame.display.set_mode((800, 600))

#Alterar Titulo e Icone da Página
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('001-spaceship.png')
pygame.display.set_icon(icon)

#Jogador
playerImg = pygame.image.load('001-arcade-game.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

#Criando um loop para a tela do jogo continuar aberta
running = True
while running:

    # Colocando cor no fundo da tela - RGB
    screen.fill((102, 204, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Verificador se a tecla para esq. ou dir. foi pressionada
        if event.type == pygame.KEYDOWN:
            print('Uma tecla foi pressionada')
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()


