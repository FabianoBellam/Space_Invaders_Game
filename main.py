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

def player():
    screen.blit(playerImg, (playerX, playerY))


#Criando um loop para a tela do jogo continuar aberta
running = True
while running:

    # Colocando cor no fundo da tela - RGB
    screen.fill((102, 204, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()


