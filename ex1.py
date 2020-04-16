from tkinter import *

def putPixel(x,y, color="red"):
    img.put(color, (x, y))

def DDAalgorithm(x1=5,y1=4,x2=50,y2=30):
    m = slope = (y2-y1) / (x2-x1)
    if x2-x1 > y2-y1:
        steps = x2-x1
    else:
        steps = y2-y1
    x_inc = (x2-x1) / steps
    y_inc = (y2-y1) / steps
    x_curr = x1
    x_arr = []
    x_arr.append(x_curr)
    y_curr = y1
    y_arr = []
    y_arr.append(y_curr)
    while x_curr < x2 and y_curr < y2:
        x_curr += x_inc
        x_arr.append(x_curr)
        y_curr += y_inc
        y_arr.append(y_curr)

    for i in range(len(x_arr)):
        x_arr[i] = round(x_arr[i])
        y_arr[i] = round(y_arr[i])
        putPixel(x_arr[i], y_arr[i])

def motion(event):
    x, y = event.x, event.y
    putPixel(x,y)


screen_width = 600
screen_height = 600
window = Tk()
window.title("EX1")

w=Canvas(window, width=screen_width, height=screen_height, bg="black")
w.pack()

img = PhotoImage(width=screen_width, height=screen_height)
w.create_image((screen_width/2, screen_height/2), image=img, state="normal")

DDAalgorithm()
window.bind('<Motion>', motion)
window.mainloop()