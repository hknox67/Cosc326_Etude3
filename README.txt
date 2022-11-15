During the initial development stages of this python Program. The user interface was something of an oddity 
as keeping all the interactive components of the UI for the snowflake drawing in one place was difficult.
I had considered a few less effective means of creating a simple UI before deciding to use two different classes
of Python libraries.

1) All the elements including a button and a number input box would be drawn in turtle. 
 - This method though useful and consistent with a single library class used for drawing and 
 user interaction. The redrawing of a snowflake to either increase or decrease its complexity 
 effectively redrew each UI element as well. Redrawing not only the snowflake but the UI as well 
 took many resources of the computer and when resizing the window did not reposition the UI elements
 accurately when the window dimensions changed. 

- A number text box from Tkinter was used instead of the slider UI component. Using this component 
  turned out to be vary tedious and required the wasting of unnecessary time for a simple drawing application.

Problem Occurred: 
A simple python Turtle class would not effectively draw the Koch Snowflake separate from the UI without the
use of another Python drawing class which accepted python turtle as a parameter. By using canvas, I could separate
the UI of drawing components from the Drawing window. However, a new issue occurred. Turtle couldn't draw in a 
Canvas without using the TurtleScreen Class and the RawTurtle Class jointly. This cased much issue in trying to 
pass parameters between python classes correctly. 

Later this issue managed to appear again when trying to determine why the UI wouldn't remain visible when 
resizing the RawTurtle Canvas window. Though the issue was solved it is important to keep in mind the varying 
properties assigned to canvases and which ones are overridden by the creation of another adjacent instance of 
python Canvas. The order of canvas instantiation is relevant as well. The UI canvas must be created and given the 
correct properties before the Drawing Canvas.



Biggest Issue: 
- Resizing the drawing Canvas window & The Drawing the Koch Snowflake without draw button Click.

Though methods of configuring the dimensions of a canvas in python were known. I had to surmise a way for the 
Draw Canvas to call the activate method to redraw the snowflake when screen dimensions had been altered. 

This statement configures the dimensions of the drawing canvas.
        self.canvas.config(height = self.canvas.winfo_height() -4, width = self.canvas.winfo_width() -4)

Solution:

By using the bind method to configure the drawing Canvas to the calls issued to a resize method which accepts
a parameter of the python turtle drawing instance. Each time the UI has its dimensions altered the turtle 
instance redraws its snowflake with its inherent complexity. This will actively recentre the python turtle 
drawing 


Solution: CODE

            self.canvas.bind("<Configure>", self.resize)

    Adding the resize method to be called by the configure statement was the final step to the resizing solution.
    If the height and width of a window is greater or less than 0 (Which it always is to see a snowflake).
    The height and width of the master window is set to the current value of height and width.

            def resize(self, event):
                if(event.height != 0):
                    self.h = event.height 
                if(event.width != 0):
                    self.w = event.width

Underlying Issue:
Despite successfully producing a Koch Snowflake UI which fulfils the criteria of Etude 3. The methods used to
achieve creating a snowflake combined with my resizing method does have its drawbacks being less effective 
than perhaps some other means of creating a UI. This is largely due to the number of systems calls to the 
resize method and the draw method in the activate function. Since the draw method relies on recursion for 
more effective speed in drawing snowflake. All these method calls mount in their use of computer resources.
Though I had considered alternative to this issue as to make resizing quicker. I couldn't execute them in time
due to assessment time constraints and a lack of familiarity with some python functions and classes. Here are
some of the alternatives I considered.

Alternatives: 

1)
- I could employ the use of a coordinate system stored into a list in python. Each recursive call to the activate 
  function could store the various points of each triangle vertex drawn from a side length. When resizing the
  the window and therefore draw canvas. The array list could replot the position of each vertex into the draw canvas
- Result:
  A significant reduction in the number of methods calls in the python IDE stack. Making the executions of other method
  more immediate. The Issue however is that python does not have a class for vectors in their libraries. And establishing
  these coordinates with the movement of turtle drawing are very difficult.

2)
- This might be the most viable solution to my resizing time delays. If I were able to cache an image of an already
  drawn snowflake and then superimpose the image over the python turtle drawing. Resizing an image alone demands
  much less resources from the computer rather than having to recursively redraw a complicated snowflake drawing
  each time the UI window is resized.

- Issue: though imposing an image into a python canvas from a file directory is easy. To capture a screen image
  from a specific python UI component is much trickier. I cannot seem to find any reference to capturing an image 
  of a particular size and screen dimension to make image resizing seamless from the execution of the activate 
  button method. 



Thank you for accepting this submission of etude 3. It did require a lot of revisiting for a language
I had not used in a long time.
