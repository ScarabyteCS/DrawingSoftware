import pygame as py
import sys
size = (1080, 720)
screen = py.display.set_mode(size)

mousedown = False

black = (0,0,0)
red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
purple = (255, 0 ,255)

center = (250, 200)
col = (255, 255, 255)

keys=py.key.get_pressed()

while True:
    for ev in py.event.get():
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_BACKSPACE:
                screen.fill((0,0,0))
                py.display.update()
                print("A key has been pressed")
            elif ev.key == py.K_r:
                col = (red)
                print("Your color is now red")
                py.display.update()
            elif ev.key == py.K_g:
                col = (green)
                print("Your color is now green")
                py.display.update()
            elif ev.key == py.K_b:
                col = (blue)
                print("Your color is now blue")
                py.display.update()
            elif ev.key == py.K_c:
                col = (cyan)
                print("Your color is now cyan")
                py.display.update()
            elif ev.key == py.K_y:
                col = (yellow)
                print("Your color is now yellow")
                py.display.update()
            elif ev.key == py.K_p:
                print("Your color is now purple")
                col = (purple)
                py.display.update()
            elif ev.key == py.K_e:
                col = (black)
                print("You are now using the eraser")
                py.display.update()
        if ev.type == py.MOUSEBUTTONDOWN:
            mousedown = True
        if ev.type == py.MOUSEBUTTONUP:
            if col != (black):
                pos = py.mouse.get_pos()
                py.draw.circle(
                    screen, col, pos, 15, 5
                )
                mousedown = False
                py.display.update()
        if ev.type == py.MOUSEMOTION and mousedown == True:
                pos2 = py.mouse.get_pos()
                py.draw.circle(
                    screen, col, pos2, 1, 1
                )
                if col == (black):
                    py.draw.circle(
                    screen, col, pos2, 30, 30
                )
                py.display.update()
    if py.event.get(py.QUIT): exit()