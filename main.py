from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

def square(x,y,length,c):
    draw_line(x, y, x + length, y, s, c)
    draw_line(x, y - length, x + length, y - length, s, c)
    draw_line(x, y - length, x, y, s, c)
    draw_line(x + length, y - length, x + length, y, s, c);

for x in range(0,100):
    c = [ random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    square(random.randint(-490,490), random.randint(-490,490), random.randint(1,300), c)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
