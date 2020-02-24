from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 0 ]
matrix = new_matrix(0,0)
testMatrix = new_matrix(3,3)
testMatrix2 = new_matrix(3,3)

#testing matrix functions
print("identity 3*3 matrix")
ident(testMatrix)
print_matrix(testMatrix)
testMatrix2[0][0] = 2
testMatrix2[1][1] = 2
testMatrix2[2][2] = 2

print("testing matrix multiplication")
print_matrix(testMatrix2)
print( "times" )
print_matrix(testMatrix)
print( "equals" )
print_matrix(matrix_mult(testMatrix2, testMatrix))

#drawing
x = 0
while x < 4:
    #stick figure
    add_edge(matrix, 10 + x,5,0, 55 + x,45,0 )
    add_edge(matrix, 85 + x,5,0, 55 + x,45,0 )
    add_edge(matrix, 55 + x,45,0, 55 + x,150,0 )
    add_edge(matrix, 25 + x,150 + x,0, 85 + x,150 + x,0 )
    add_edge(matrix, 25 + x,150,0, 25 + x,210,0 )
    add_edge(matrix, 85 + x,150,0, 85 + x,210,0 )
    add_edge(matrix, 25 + x,210 + x,0, 85 + x,210 + x,0 )
    add_edge(matrix, 55 + x,90,0, 20 + x,120,0 )
    add_edge(matrix, 55 + x,90,0, 90 + x,120,0 )

    #sword
    add_edge(matrix, 70 + x,125,0, 93 + x,105,0 )
    add_edge(matrix, 70 + x,125,0, 115 + x,165,0 )
    add_edge(matrix, 93 + x,105,0, 138 + x,145,0 )
    add_edge(matrix, 80 + x,200,0, 115 + x,165,0 )
    add_edge(matrix, 173 + x,110,0, 138 + x,145,0 )
    add_edge(matrix, 80 + x,200,0, 430 + x,490,0 )
    add_edge(matrix, 173 + x,110,0, 420 + x,297,0 )
    add_edge(matrix, 430 + x,490,0, 420 + x,297,0 )

    x = x + 1

draw_lines( matrix, screen, color )
display(screen)
