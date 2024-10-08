import pygame, random, time
from pygame.locals import *

# inicialização da biblioteca
pygame.init()

# interface
screen_width = (600,600)
screen = pygame.display.set_mode(screen_width)
pygame.display.set_caption('Jogo da Cobrinha')

# direções da cobra
esquerda = K_LEFT  
direita = K_RIGHT
cima = K_UP
baixo = K_DOWN

# variavel de quando a cobrinha vai se mopvimentar
passo = 10

# criação das variáveis
snake = [(200, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))
snake_dir = baixo

# funçao de colisao
def gerar_posicao_maca():
    while True:
        nova_posicao = (random.randint(0, (screen[0]// 10)-1) * 10, random.randint(0, (screen[1]// 10)-1) * 10)
        if nova_posicao not in snake:
            return nova_posicao

maca_img = pygame.image.load("maca.png")
img_redimencionada = pygame.transform.scale(maca_img, (25,25))
maca_pos = gerar_posicao_maca()

while True:
    screen.fill((0, 0, 0))
    pygame.time.Clock().tick(10)

    # verificar as posiçoes do corpo da cobra e exibir na tela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key in [cima, baixo, esquerda, direita]:
                snake_dir = event.key
        
        # Movimento da cobrinha
    if snake_dir == cima:
        nova_posicao = (snake[0][0], snake[0][1]-passo)
    if snake_dir == baixo:
        nova_posicao = (snake[0][0], snake[0][1]+passo)
    if snake_dir ==  esquerda:
        nova_posicao = (snake[0][0]-passo, snake[0][1])
    if snake_dir == direita:
        nova_posicao = (snake[0][0]+passo, snake[0][1])
    snake.insert(0, nova_posicao)
    snake.pop()

    for pos in snake:
        screen.blit(snake_skin, pos)

    screen.blit(img_redimencionada, maca_pos)

    pygame.display.update()
