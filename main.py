import random
import time

import pygame
from PPlay import window
from PPlay import keyboard
from PPlay import gameobject
from PPlay import sprite


width, height = 640, 480
janela = window.Window(width, height)
janela.set_title("PONG")
dificuldade = 2

pnt_1 = 0
pnt_2 = 0

started = True

div = sprite.Sprite("assets/divider.png")
div.x = (janela.width - div.width)/2

bola = sprite.Sprite("assets/ball.png")
ball_speed = 200
ballX = ballY = ball_speed

rand = random.randint(0, 100)

pad1 = sprite.Sprite(f"assets/{dificuldade}pad1.png")
pad1.set_position(0, height/2)
pad2 = sprite.Sprite(f"assets/{dificuldade}pad2.png")
pad2.set_position(janela.width - pad2.width, height/2)
pad_vel = 300
branco = (255, 255, 255)
preto = (0, 0, 0)

teclado = keyboard.Keyboard()

def rst_pos(GameObject):
    GameObject.set_position(width / 2, height / 2)

while True:
    janela.set_background_color((100, 50, 50))
    div.draw()
    bola.draw()
    pad1.draw()
    pad2.draw()
    #bola.update()
    bola.move_x(ballX*janela.delta_time()* dificuldade)
    bola.move_y(ballY*janela.delta_time()* dificuldade)
    if pad1.x + pad1.width - 2 > bola.x and started:
        #gol da dir
        pnt_2 += 1
        rst_pos(bola)
        ballX *= -1
        ballY *= -1
    if bola.x + bola.width - 2 > pad2.x and started:
        # gol da esq
        pnt_1 +=1
        rst_pos(bola)
        ballX *= -1
        ballY *= -1
    if 0 > (bola.y)  or (bola.y ) > janela.height - bola.height:
        ball_speed += 50
        ballY *= -1
        if 0 > bola.y:
            bola.y = 2
        if bola.y > janela.height + bola.height:
            bola.y = janela.height + bola.height - 2
    #ballX = ballY = ball_speed

    janela.draw_text(f"{pnt_1}", janela.width/4, 50, size=45 ,color=preto)
    janela.draw_text(f"{pnt_1}", janela.width/4, 50, size=40 ,color=branco)

    janela.draw_text(f"{pnt_2}", 3* janela.width/4, 50, size=45 ,color=preto)
    janela.draw_text(f"{pnt_2}", 3* janela.width/4, 50, size=40 ,color=branco)

    if  bola.y + rand <= pad2.y + pad2.height/2 and pad2.y > 0:
        pad2.move_y(-pad_vel*janela.delta_time() * dificuldade)
    elif bola.y - rand >= pad2.y and pad2.y < height-pad2.height:
        pad2.move_y(pad_vel*janela.delta_time() * dificuldade)

    if teclado.key_pressed("W") and pad1.y > 0:
        pad1.move_y(-pad_vel*janela.delta_time() * dificuldade)
    elif teclado.key_pressed("S") and pad1.y < height-pad1.height:
        pad1.move_y(pad_vel*janela.delta_time() * dificuldade)

    if bola.collided(pad1) or bola.collided(pad2):

        rand = random.randint(50, 200)
        if bola.x <= pad1.x:
            bola.x = pad1.x + bola.width + 2

        if bola.x >= pad2.x:
            rand = random.randint(50, 200)
            bola.x = pad2.x - bola.width - 2
        ballX*=-1
    print(rand)
    started = True
    janela.update()