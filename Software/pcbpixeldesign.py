from PIL import Image, ImageColor
import random
import time



x_pixel = 10
y_pixel = 10
spacing = 2

x_pixel_length = 50
y_pixel_length = 10

x_pcb_image_size = (x_pixel+spacing)*x_pixel_length
y_pcb_image_size = (y_pixel+spacing)*y_pixel_length

blackpcb = [(28,28,28),(45,45,45),(254,236,134),(235,237,249)]

def drawpixel(xpos, ypos, color):
    global pixelcounter
    for x in range(x_pixel):
        for y in range(y_pixel):
            pixel_image.putpixel((xpos + x, ypos + y), ImageColor.getcolor(color, 'RGB'))  # or whatever color you wish


def drawpixelrow(yline):
    for x in range(x_pixel_length):
        color = 'rgb' + str(random.choices(blackpcb, weights=[5*x,3*x,2*(x_pixel_length-x),x_pixel_length-x])).replace('[','').replace(']','')
        drawpixel((x_pixel+spacing)*x,yline, color)

if  0*0 < 3600*3600:
    pixel_image = Image.new(mode = 'RGB', size = (x_pcb_image_size, y_pcb_image_size), color = blackpcb[0]) # mode try P, RGB, 1

    for y in range(y_pixel_length):
        drawpixelrow((y_pixel+spacing)*y)


    pixel_image.save('01_PCBWallet_Design.png')  # or any image format
    pixel_image.show()

else:
    print("Please use smaller Framesize")
