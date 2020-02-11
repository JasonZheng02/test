from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    if (x0 > x1 and y0 > y1):
        x0, x1, y0, y1 = x1, x0, y1, y0
    A = y1 - y0
    B = (x1 - x0) * -1
    x = x0
    y = y0

    if (B == 0):
        if (x1 > x0):
            while (x <= x1):
                plot(screen, color, x, y)
                x = x + 1
        else:
            while (y <= y1):
                plot(screen, color, x, y)
                y = y + 1

    else:
        slope = (A / B) * -1
        if (slope <= 1 and slope > 0):
            D = 2 * A + B
            while (x <= x1):
                plot(screen, color, x, y)
                if (D > 0):
                    y = y + 1
                    D = D + 2 * B
                x = x + 1
                D = D + 2 * A

        elif (slope > 1):
            D = A + 2 * B
            while (y <= y1):
                plot(screen, color, x, y)
                if (D < 0):
                    x = x + 1
                    D = D + 2 * A
                y = y + 1
                D = D + 2 * B

        elif (slope < -1):
            D = -1 * A + 2 * B
            while (y <= y1):
                plot(screen, color, x, y)
                if (D > 0):
                    x = x - 1
                    D = D - 2 * A
                y = y + 1
                D = D + 2 * B

        else:
            D = 2 * A - B
            while (x <= x1):
                plot(screen, color, x, y)
                if (D < 0):
                    y = y - 1
                    D = D - 2 * B
                x = x + 1
                D = D + 2 * A
