from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

draw_line(200, 400, 300, 400, s, c)
draw_line(200, 400, 300, 400, s, c)
draw_line(200, 400, 300, 400, s, c)
draw_line(200, 400, 300, 400, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
