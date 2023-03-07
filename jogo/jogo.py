import pygame as pg
from pygame.locals import *

# Iniciar o pygame
pg.init()

# Definir o tamanho da tela
size = 640, 320
width, height = size
screen = pg.display.set_mode(size)

# Definir o título da janela
pg.display.set_caption('"Joguinho"')

# Rodar o game
running = True

# Definir cor
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 50)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
white = (255, 255, 255)
background = gray = (127, 127, 127)

# Dicionário de cores, onde cada tecla possui a sua respectiva cor
key_dict = {K_k:black, K_r:red, K_g:green, K_b:blue, K_y:yellow, K_c:cyan, K_m:magenta, K_w:white}

ball = pg.image.load("D:\workspace\pygame\imagens\intro_ball.gif")
rect = ball.get_rect()
speed = [1, 1]

# Enquanto rodar, irá realizar tudo o que há dentro do loop
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

        # Definir a cor da tela com a cor escolhida
        screen.fill(green)

        # Se apertar qualquer tecla do key_dict, o background mudará de cor
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

        rect = rect.move(speed)
        if rect.left < 0 or rect.right > width:
            speed[0] = -speed[0]
        if rect.top < 0 or rect.bottom > height:
            speed[1] = -speed[1]

        pg.draw.rect(screen, red, rect, 1)
        screen.blit(ball, rect)
        # Atualizar a tela
        pg.display.update()

        print(event)
# Encerrar o pygame
pg.quit()