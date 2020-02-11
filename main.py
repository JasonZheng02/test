from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

def square(x,y,length):
    draw_line(x, y, x + length, y, s, c)
    draw_line(x, y - length, x + length, y - length, s, c)
    draw_line(x, y - length, x, y, s, c)
    draw_line(0, YRES/2, XRES-1, YRES/2, s, c)
square(300,300,100)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
