import pygame
from PPlay import window
from PPlay import keyboard
from PPlay import gameobject
from PPlay import sprite

width, height = 640, 480
janela = window.Window(width, height)
janela.set_title("PONG")

bola = sprite.Sprite("assets/ball.png")
ball_speed = 200
ballX = ballY = ball_speed

pad1 = sprite.Sprite("assets/pad1.png")
pad1.set_position(0, height/2)
pad2 = sprite.Sprite("assets/pad2.png")
pad2.set_position(janela.width - pad2.width, height/2)
pad_vel = 300

teclado = keyboard.Keyboard()

def rst_pos(GameObject):
    GameObject.set_position(width / 2, height / 2)

while True:
    janela.set_background_color((100, 50, 80))
    bola.draw()
    pad1.draw()
    pad2.draw()
    #bola.update()
    janela.update()
    bola.move_x(ballX*janela.delta_time())
    bola.move_y(ballY*janela.delta_time())
    if 0 > bola.x:
        #gol da dir
        rst_pos(bola)
        ballX *= -1
        ballX = ballY = ball_speed
    if bola.x> janela.width:
        # gol da esq
        rst_pos(bola)
        #ballX+=20
        ballX = ballY = ball_speed
        ballX *= -1
    if bola.height > (bola.y) or (bola.y ) > janela.height -  bola.height:
        ballY+=50
        ballY *= -1


    if teclado.key_pressed("UP") and pad2.y >0 :
        pad2.move_y(-pad_vel*janela.delta_time())
    elif teclado.key_pressed("DOWN") and pad2.y < height-pad2.height:
        pad2.move_y(pad_vel*janela.delta_time())

    if teclado.key_pressed("W") and pad1.y >0 :
        pad1.move_y(-pad_vel*janela.delta_time())
    elif teclado.key_pressed("S") and pad1.y < height-pad1.height:
        pad1.move_y(pad_vel*janela.delta_time())

    if bola.collided(pad1) or bola.collided(pad2):
        ballX*=-1