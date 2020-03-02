from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
for x in range(100):
    add_edge(edges, 0, 0 + x, 0, 100, 0 + x, 0)
    add_edge(edges, 100, 0 + x, 0, 100, 0 + x, 100)
    add_edge(edges, 0, 0, 0 + x, 100, 0, 0 + x)
    draw_lines(edges, screen, color)
parse_file( 'script', edges, transform, screen, color )
