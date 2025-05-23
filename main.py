from tkinter import *
import random
import time  # Import the time module

root = Tk()
root.geometry("800x600")
root.config(bg="teal")

'''MODEL'''
def game_loop(snake, apple, count): # Create a function for the game loop
   snake[0].move(snake, apple)
   canvas.after(110, lambda: game_loop(snake, apple, count))

def start():
    canvas.delete("all")
    sq_size = 40
    for y in range(0, int(700/sq_size)):
        for x in range(0,int(760/sq_size)):
            if (x + y) % 2 == 0:
                canvas.create_rectangle(x * sq_size, y * sq_size, (x * sq_size) + sq_size, (y * sq_size) + sq_size, fill="white", width=0)

    apple = Apple(canvas)
    snake = [Head(canvas)]
    count = 0
    game_loop(snake, apple, count)

class Apple():
    def __init__(self, canvas):
        self.x_coor = random.randint(0, 18)*40+20
        self.y_coor = random.randint(0, 12)*40+20
        self.radius = 18
        self.apple = canvas.create_oval(self.x_coor - self.radius, self.y_coor - self.radius, 
                                        self.x_coor + self.radius, self.y_coor + self.radius,
                                        fill = "red")

    def relocate(self):
        self.x_coor = random.randint(0, 18)*40+20
        self.y_coor = random.randint(0, 12)*40+20
        canvas.coords(self.apple, 
                      self.x_coor - self.radius, self.y_coor - self.radius,
                      self.x_coor + self.radius, self.y_coor + self.radius)

class Head:
    def __init__(self, canvas):
        self.x_coor = 9*40+20
        self.y_coor = 8*40+20
        self.simp_x_coor = 9
        self.simp_y_coor = 6
        self.alive = True
        self.direction = "north"
        root.bind("<Up>", self.north)
        root.bind("<Down>", self.south)
        root.bind("<Left>", self.west)
        root.bind("<Right>", self.east)
        self.head_segment = canvas.create_rectangle(self.x_coor - 20, self.y_coor - 20,
                                                    self.x_coor + 20, self.y_coor + 20,
                                                    fill= "green")

    def move(self, snake, apple):
        if self.direction == 'north':
           canvas.move(self.head_segment, 0, -40)
           self.y_coor -= 40
        elif self.direction == 'south':
            canvas.move(self.head_segment, 0, 40)
            self.y_coor += 40
        elif self.direction == 'west':
            canvas.move(self.head_segment, -40, 0)
            self.x_coor -= 40
        elif self.direction == 'east':
            canvas.move(self.head_segment, 40, 0)
            self.x_coor += 40

    def collide(self, obj):
        pass

    def north(self, event=None):
        if self.direction != "south":
            self.direction = 'north'

    def east(self, event=None):
        if self.direction != 'west':
            self.direction = 'east'

    def south(self, event=None):
        if self.direction != 'north':
            self.direction = 'south'

    def west(self, event=None):
        if self.direction != 'east':
            self.direction = 'west'

class Segment:
    def __init__(self,canvas, obj, color):
        pass
   
    def relocate(self,obj):
        pass
       

'''CONTROLLER'''
start_button = Button(root, text = "Press to Start", fg = "white", bg = "teal", command = start)
start_button.place(x=20, y = 10, width = 100, height = 40)
'''VIEW'''
canvas = Canvas(root, bg="light gray")
canvas.place(x=20, y=60, width=760, height=520)

sq_size = 40
for y in range(0, int(520/sq_size)):
    for x in range(0,int(760/sq_size)):
        if (x + y) % 2 == 0:
            canvas.create_rectangle(x * sq_size, y * sq_size, (x * sq_size) + sq_size, (y * sq_size) + sq_size, fill="white", width=0)

root.mainloop()