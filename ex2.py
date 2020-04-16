from tkinter import *
import math
import line
import circle
import curve

screen_width = 600
screen_height = 600


def drawAline(event):
    if line.motion(event):
        coordinates = line.get_line_coordinates()
        myLine(coordinates[0], coordinates[1], coordinates[2], coordinates[3])


def drawAcircle(event):
    if circle.motion(event):
        coordinates = circle.get_radius_coordinates()
        myCircle1(coordinates[0], coordinates[1], coordinates[2], coordinates[3])


def drawAcurve(event):
    if curve.motion(event):
        coordinates = curve.get_line_coordinates()
        putPixel(coordinates[0], coordinates[1])
        putPixel(coordinates[2], coordinates[3])
        putPixel(coordinates[4], coordinates[5])
        putPixel(coordinates[6], coordinates[7])

def putPixel(x, y, color="red"):
    img.put(color, (x, y))
    img.put(color, (x+1, y))
    img.put(color, (x, y+1))
    img.put(color, (x-1, y))
    img.put(color, (x, y-1))


def myLine(X0, Y0, X1, Y1):
    # Based on DDA Algorithm
    # // calculate dx & dy
    dx = X1 - X0
    dy = Y1 - Y0

    # // calculate steps required for generating pixels
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    # // calculate increment in x & y for each steps
    Xinc = dx / steps
    Yinc = dy / steps

    # // Put pixel for each step
    X = X0
    Y = Y0
    for i in range(steps):
        putPixel(int(X), int(Y), color="RED")  # // put pixel at (X,Y)
        X += Xinc  # // increment in x at each step
        Y += Yinc  # // increment in y at each step


def myCircle1(xc, yc, x2, y2):
    radius = pow(pow(x2 - xc, 2) + pow(y2 - yc, 2), 0.5)
    # print("radius: " + str(radius))
    G = radius * 2 * 3.141
    angle = 1 / radius
    for i in range(360):
        new_x2 = xc + radius * math.cos(i)
        new_y2 = yc + radius * math.sin(i)
        try:
            putPixel(round(new_x2), round(new_y2))
        except:
            pass


def plot_circle_points(xc, yc, y, x=0):
    putPixel(round(xc + x), round(yc + y))
    putPixel(round(xc - x), round(yc + y))
    putPixel(round(xc + x), round(yc - y))
    putPixel(round(xc - x), round(yc - y))
    putPixel(round(xc + y), round(yc + x))
    putPixel(round(xc - y), round(yc + x))
    putPixel(round(xc + y), round(yc - x))
    putPixel(round(xc - y), round(yc - x))


def myCircle2(xc, x2, yc, y2):
    radius = pow(pow(x2 - xc, 2) + pow(y2 - yc, 2), 0.5)
    x = 0
    y = radius
    p = 3 - 2 * radius
    while x < y:
        plot_circle_points(xc, yc, y, x)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        x = x + 1
    if x == y:
        plot_circle_points(xc, yc, y, x)


def handle_line_menu():
    window.bind('<Button-1>', drawAline)


def handle_circle_menu():
    window.bind('<Button-1>', drawAcircle)


def handle_curve_menu():
    window.bind('<Button-1>', drawAcurve)


line = line.Line()
circle = circle.Circle()
curve = curve.Curve()
window = Tk()
window.title("EX1")

w = Canvas(window, width=screen_width, height=screen_height)
img = PhotoImage(width=screen_width, height=screen_height)
w.create_image((screen_width / 2, screen_height / 2), image=img, state="normal")

menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=window.quit)

drawmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Draw', menu=drawmenu)
drawmenu.add_command(label='Line', command=handle_line_menu)
drawmenu.add_command(label='Circle', command=handle_circle_menu)
drawmenu.add_command(label='Curve', command=handle_curve_menu)

w.pack()
window.mainloop()
