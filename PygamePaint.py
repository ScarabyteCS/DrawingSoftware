import pygame as py
import sys
size = (1080, 720)
screen = py.display.set_mode(size)

mousedown = False

white = (255,255,255)
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

rmb = py.mouse.get_pressed()[2]
lmb = py.mouse.get_pressed()[0]

circlesize = 15
circlethickness = 5

buttontype = 0
while True:
    for ev in py.event.get():
        if circlesize < 5:
            circlesize = 5
            print("Your circle is too small")
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
            elif ev.key == py.K_w:
                print("Your color is now white")
                col = (white)
                py.display.update()
        if ev.type == py.MOUSEWHEEL:
            print(ev.x, ev.y)
            if ev.y == (1):
                circlesize += 10
            if ev.y == (-1):
                circlesize -= 10        
        if ev.type == py.MOUSEBUTTONDOWN:
            mousedown = True
            buttontype = ev.button
        if ev.type == py.MOUSEMOTION and mousedown == True and buttontype == 1:
            pos2 = py.mouse.get_pos()
            py.draw.circle(
                screen, col, pos2, 1, 1
            )
            if col == (black):
                py.draw.circle(
                screen, col, pos2, 30, 30
            )
            py.display.update()        
        if ev.type == py.MOUSEBUTTONUP:
            mousedown = False
            if ev.button == 3:
                if col != (black):
                    pos = py.mouse.get_pos()
                    py.draw.circle(
                        screen, col, pos, circlesize, 5
                    )
                    py.display.update()
                    print(ev.button)
    if py.event.get(py.QUIT): exit()