"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c]),
        print("")


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for c in range(len(matrix)):
        for r in range(len(matrix)):
            if c == r:
                matrix[c][r] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    product = new_matrix(len(m1),len(m1[0]))
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            for i in range(len(m2)):
                product[r][c] = product[r][c] + m1[r][i] * m2[i][c]
    return product

def new_matrix(rows, cols):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
