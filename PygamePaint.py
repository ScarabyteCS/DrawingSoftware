#Imports
import pygame as py
import sys

#Display Settings
size = (1080, 720)
screen = py.display.set_mode(size)

#Variable Declarations
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
#End of Variable Declarations

#Main Loop
while True:
    for ev in py.event.get():
        #If set your circle size to lower than 5, sets size back to 5 and prints that your circle is too small
        if circlesize < 5:
            circlesize = 5
            print("Your circle is too small")
        if ev.type == py.KEYDOWN:
            #If you press backspace, it'll clear the screen (fill it with black)
            if ev.key == py.K_BACKSPACE:
                screen.fill((0,0,0))
                py.display.update()
                print("The screen has been cleared")
            #If you press one of these keys, it will change the color of your drawing
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
        #If you scroll the wheel, it will dd or subtract 10 units to the size of the circle depending on which way you scroll
        if ev.type == py.MOUSEWHEEL:
            print(ev.x, ev.y)
            if ev.y == (1):
                circlesize += 10
            if ev.y == (-1):
                circlesize -= 10    
        #If you press the mouse down, it will declare the variable "mousedown" to be true    
        if ev.type == py.MOUSEBUTTONDOWN:
            mousedown = True
            buttontype = ev.button
        #If you move the mouse, are holding the mouse button down, and are using the left mouse button, it will draw a line with a width of 1 pixel by 1 pixel
        if ev.type == py.MOUSEMOTION and mousedown == True and buttontype == 1:
            pos2 = py.mouse.get_pos()
            py.draw.circle(
                screen, col, pos2, 1, 1
            )
        #If the color of the line is black (eraser), it will change the size of the line to 30 pixels by 30 pixels
            if col == (black):
                py.draw.circle(
                screen, col, pos2, 30, 30
            )
            py.display.update()     
        #When you release the right mouse button after pressing, it will draw a circle wherever your mouse is
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
    #If you quit out of the window, it will exit
    if py.event.get(py.QUIT): exit()