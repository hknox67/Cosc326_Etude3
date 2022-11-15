from math import sqrt
from tkinter import ttk
import turtle
from tkinter import *
import tkinter as tk

## @Author Hayden Knox
# This is the Koch Snowflake UI interactive program that I have managed to create. 
# All the methods required for this program to run are placed within a single class
# which successively relies on renewing an instance of python turtle which has 
# been passed within an instance of Tkinter Canvas. 

class App:   

    # This method is called when the program user clicks the Draw button created in the python
    # main method. When the button is clicked, the current instances of the two python tkinter 
    # canvases are passed into the function including the current value associated with the slider
    # GUI component. The slider determines the order of complexity the koch snowflake will be drawn
    # and thusly the number of recursive method calls required to reproduce the snowflake in
    # various different simplistic or complicated forms. 

    def activate(self, slider):
        # This python programming statment determines the correct dimensions of the python draw_Canvas instance 
        # This is required before the length of the initial turtle drawing can be decided. 
        self.canvas.config(height = self.canvas.winfo_height() -4, width = self.canvas.winfo_width() -4)
        self.guiCanvas.config(height = 8) # This sets the height of the GUI Canvas against the drawing Canvas
        initialise = False
        if(initialise == False): # This boolean flag is used to conserve memory resources when redrawing a 
            # Python tirtle, Only if a drawing hasnt yet been made does this if statment execute. 
            self.screen = turtle.TurtleScreen(self.canvas)
            self.turtle = turtle.RawTurtle(self.screen)
            initialise = True
        self.screen.bgcolor("grey")            
        self.turtle.hideturtle()
        self.turtle.clear()
        self.turtle.reset() # resets the canvas for a new drawing when activate is clicked repeatedly.

        # This if statement determines the size of the triangles sides from each activation button click method call or resize method execution
        # The length of the initial triangle sides and all subsequent reucrsive calls to the drawing method all adhere to the length of each 
        # window size. However the length of the triangle sides is determined by which window dimension is shorter. As the shorter window of 
        # either winfo_height or winfo_width will fit dynamically into the drawing canvas. 
        if self.canvas.winfo_height() > self.canvas.winfo_width():
            self.turtle.length = self.canvas.winfo_width()/2.0
        else:
            self.turtle.length = self.canvas.winfo_height()/2.0
        
        #self.turtle.length = sqrt((self.canvas.winfo_height()**2  + self.canvas.winfo_width()**2)) / 4   # This statement sets the length of the Pythong drawing turtle
        # lines to a fraction of the area proportional the Draw canvas height and width. 
        self.turtle.penup()  
        sliderValue = self.guiCanvas.slider.get() # This programming statement 
        #retrives the number of recursive calls from the Slider GUI component used for the Koch snowflake drawing. Determining
        # determining the snowflakes complexity.
        self.turtle.backward(self.turtle.length/2.0) #here
        #self.turtle.right(90)
        #self.turtle.left(90)
        #self.turtle.forward(10) #here
        self.turtle.pendown()   
        self.turtle.hideturtle() # Hised the directional turtle arrow head
        self.screen.tracer(0) # turns off the turtle drawing animation

    # The for loop in this method determines the basic number of sides which are retquired to produce
    # The initial phase of the koch snowflake. Since A new series of vertecies is created from each side of a triangle
    # by dividing a triangle side into 3 and using the third central portion to draw a new equilateral vertex or tiangle, to produce a six pointed star
    # This for loop with a smallest complexity of 1 will produce an equilateral triangle. reference #1
        for i in range(3):
            # This is the python turtle method call which draws the koch snowflake.
            self.drawFlake(self.turtle.length, sliderValue)
            #reference #2 This turtle will rotate 3  times around a sigle point 120 degrees to produce a triangle.
            # A basic property of gemoetry is that all all cointerior angles of a triangle sum total to 360 degrees.
            self.turtle.left(120)
        self.screen.update()

    # This python bethod is executed in perpetuity in the event that the window dimensions to the koch snowflake UI 
    # change based on the users clicking and dragging of the mouse.
    # This method takes parameters of the event of resizing the UI window and the instance of the entire python UI.
    # This method resizes both the hieght of the draw_canvas instance and the width of the draw_canvas instance. 
    def resize(self, event):
        if(event.height != 0):
            self.h = event.height 
        if(event.width != 0):
            self.w = event.width    
        if(self.canvas.winfo_height() % 5 == 0 or self.canvas.winfo_width() % 5 == 0):
            self.initialise = True
            self.activate(self.turtle)

    # This method is responsible for drawing the koch snowflake in the python UI.
    # This method takes 3 parameters to work, the instance of the draw_canvas created by the
    # main method, the lineLength variable created by the activate() method and the 
    # complexity scalear value given from the activate method from the slider gui 
    # component. For each recursive method call the complecity variable decreases and unlit the 
    # integer value of complexity is reduced to zero. 

    # If a complexity of 1 is entered into this method the forward method is executed in 
    # tandem with the rotate 120degrees staement from the activate method producing a triangle. 
    def drawFlake(self, lineLength, complexity): 
        if complexity == 1: 
            self.turtle.forward(lineLength) 
            return
        if complexity > 1:
            lineLength /= 3.0
            self.drawFlake(lineLength, complexity-1) 
            self.turtle.right(60) 
            self.drawFlake(lineLength, complexity-1) 
            self.turtle.left(120) 
            self.drawFlake(lineLength, complexity-1) 
            self.turtle.right(60) 
            self.drawFlake(lineLength, complexity-1) 

    # This main method creates the instances of all the major components of the UI.
    # including the UI canvas, the koch Snowflake drawing Canvas, the UI components 
    # and the properties which are needed to resize each window with the master windows scale. 
    def __init__(self, master):
        self.master = master
        self.master.title("Koch Snowflake UI")
        self.guiCanvas = tk.Canvas(master)
        self.guiCanvas.pack(fill = BOTH, side= BOTTOM)
        self.guiCanvas.configure(height = 20)
        self.guiCanvas.button = Button(self.master, command = lambda:self.activate(self.turtle), text = "Draw", width = 5,
        height = 1, bg = "grey", fg = "black")
        self.guiCanvas.complexityLabel = ttk.Label(self.master, text='Snowflake Complexity:')
        self.guiCanvas.slider = Scale(from_= 1, to = 12, orient='horizontal')
        self.guiCanvas.button.pack(side=tk.TOP, fill = BOTH)
        self.guiCanvas.complexityLabel.pack(side=tk.TOP, fill = BOTH)
        self.guiCanvas.slider.pack(side=tk.TOP, fill = BOTH)
        self.canvas = tk.Canvas(master)
        self.turtle = None
        self.canvas.pack(fill = BOTH, expand = YES, side= BOTTOM)
        self.canvas.bind("<Configure>", self.resize)

if __name__ == "__main__": 
    root = tk.Tk()
    app = App(root)
    root.resizable(1,1)
    root.mainloop()


    