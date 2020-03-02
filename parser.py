from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
               then multiply the transform matrix by the translation matrix -
               takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open("script","r")
    script = file.readlines()
    x = 0
    while x < len(script):
        if script[x] == "line\n":
            inputs = script[x+1].split()
            add_edge(points, int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]), int(inputs[4]), int(inputs[5]))

        if script[x] == "display\n":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display( screen )

        if script[x] == "ident\n":
            ident(transform)

        if script[x] == "scale\n":
            inputs = script[x+1].split()
            scale_Matrix = make_scale(int(inputs[0]), int(inputs[1]), int(inputs[2]))
            matrix_mult(scale_Matrix, transform)

        if script[x] == "apply\n":
            matrix_mult(transform, points)
            for r in range( len( points[0] ) ):
                for c in range( len(points) ):
                    points[c][r] = int(points[c][r])

        if script[x] == "move\n":
            inputs = script[x+1].split()
            translation_Matrix = make_translate(int(inputs[0]), int(inputs[1]), int(inputs[2]))
            matrix_mult(translation_Matrix, transform)

        if script[x] == "rotate\n":
            inputs = script[x+1].split()
            if inputs[0] == "x":
                rot_Matrix = make_rotX(int(inputs[1]))
            if inputs[0] == "y":
                rot_Matrix = make_rotY(int(inputs[1]))
            if inputs[0] == "z":
                rot_Matrix = make_rotZ(int(inputs[1]))
            matrix_mult(rot_Matrix, transform)

        if script[x] == "save\n":
            inputs = script[x+1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, inputs[:-1])

        if script[x] == "quit\n":
            pass
            
        x = x + 1
