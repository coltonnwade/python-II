import tkinter as tk

root = tk.Tk()

# Flag Canvas
flag = tk.Canvas(bg="#BA0101", height=300, width=500)
flag.pack()

# White / Blue Line to the Right
BlueLine = flag.create_rectangle(510, 310, 470, 0, fill="#003366", outline="#003366")
WhiteLine = flag.create_rectangle(470, 310, 465, 0, fill="#FFFFFF", outline="#FFFFFF")


# Create Circle Method
def create_circle(x, y, r, canvasName, fill, outline, width):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill=fill, outline=outline, width=width)


# Creates Circle's
create_circle(240, 150, 74, flag, "#003366", "#FFFFFF", 6)  # Blue Circle

# Creates Stars
# One(x,y) Two(x,y) Three(x,y) Four(x,y) Five(x,y)
flag.create_polygon(220, 170, 235, 145, 200, 155, 251, 156, 195, 145)
root.mainloop()