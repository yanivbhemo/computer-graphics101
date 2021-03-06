from tkinter import *
import time
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
        myBezier(coordinates[0],coordinates[2],coordinates[4],coordinates[6], coordinates[1], coordinates[3], coordinates[5], coordinates[7], numOfSegments_g)

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


def myBezier(x1,x2,x3,x4,y1,y2,y3,y4,numOfSegments):
    path_positions = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

    P0 = path_positions[0]
    P1 = path_positions[1]
    P2 = path_positions[2]
    P3 = path_positions[3]

    speed = 1 / numOfSegments
    t = 0
    old_pos_x, old_pos_y = (x1,y1)
    while t < 1:
        t += speed
        P0_x = pow((1 - t), 3) * P0[0]
        P0_y = pow((1 - t), 3) * P0[1]

        P1_x = 3 * pow((1 - t), 2) * t * P1[0]
        P1_y = 3 * pow((1 - t), 2) * t * P1[1]

        P2_x = 3 * (1 - t) * pow(t, 2) * P2[0]
        P2_y = 3.0 * (1 - t) * pow(t, 2) * P2[1]

        P3_x = pow(t, 3) * P3[0]
        P3_y = pow(t, 3) * P3[1]

        formular = ((P0_x + P1_x + P2_x + P3_x), (P0_y + P1_y + P2_y + P3_y))
        x, y = formular
        myLine(round(old_pos_x),round(old_pos_y),round(x),round(y))
        old_pos_x, old_pos_y = (x,y)
        time.sleep(0.02)

def handle_line_menu():
    window.bind('<Button-1>', drawAline)


def handle_circle_menu():
    window.bind('<Button-1>', drawAcircle)


def handle_curve_menu(numOfSegments):
    window.bind('<Button-1>', drawAcurve)
    print(numOfSegments)
    global numOfSegments_g
    numOfSegments_g = numOfSegments

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
curvemenu = Menu(drawmenu, tearoff=0)
drawmenu.add_cascade(label='Curve', menu=curvemenu)
curvemenu.add_command(label='4', command=lambda: handle_curve_menu(4))
curvemenu.add_command(label='10', command=lambda: handle_curve_menu(10))
curvemenu.add_command(label='20', command=lambda: handle_curve_menu(20))
curvemenu.add_command(label='30', command=lambda: handle_curve_menu(30))
curvemenu.add_command(label='40', command=lambda: handle_curve_menu(40))

w.pack()
window.mainloop()
