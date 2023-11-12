import turtle  # import turtle module

class Hexagons:  # define a class called Hexagons
    # initialize the class with hex colors, width, height and title
    def __init__(self, hex_colors, width=600, height=800, title="Hexagons"):
        self.hex_colors = hex_colors  # set the hex colors
        self.width = width  # set the width
        self.height = height  # set the height
        self.title = title  # set the title
        self.x_start = -100  # set the starting x coordinate
        self.y_start = 100  # set the starting y coordinate
        self.hex_turtle = turtle.Turtle()  # create a turtle object
        self.hex_turtle.speed(0)  # set the speed of the turtle to maximum

    # define a method called draw_hexagon that takes in a color and length as arguments
    def draw_hexagon(self, color, length):
        self.hex_turtle.color(color)  # set the color of the turtle to the given color
        self.hex_turtle.begin_fill()  # start filling the hexagon with color
        for i in range(8):  # repeat 8 times
            self.hex_turtle.forward(length)  # move forward by length units
            self.hex_turtle.right(45)  # turn right by 45 degrees

    def draw_hexagons(self):  # define a method called draw_hexagons
        for i in range(2):  # repeat twice
            x = self.x_start  # set x to starting x coordinate
            y = 100 + i * 50  # calculate y coordinate based on row number
            self.hex_turtle.penup()  # lift up pen to move without drawing
            self.hex_turtle.goto(x, y)  # move turtle to (x,y)
            self.hex_turtle.pendown()  # put pen down to start drawing
            self.draw_hexagon(self.hex_colors[i], 50)  # draw a hexagon with given color and length

        for i in range(3):  # repeat three times
            x = self.x_start  # set x to starting x coordinate
            y = 250 + i * 25   # calculate y coordinate based on row number
            self.hex_turtle.penup()   # lift up pen to move without drawing
            self.hex_turtle.goto(x, y)   # move turtle to (x,y)
            self.hex_turtle.pendown()   # put pen down to start drawing
            self.draw_hexagon(self.hex_colors[i+3], 50)   # draw a hexagon with given color and length

    def draw_circles(self):   # define a method called draw_circles
        self.hex_turtle.penup()   # lift up pen to move without drawing
        self.hex_turtle.goto(-100, 210)   # move turtle to (-100,210)
        self.hex_turtle.color(self.hex_colors[0])   # set color of turtle to first hex color
        self.hex_turtle.begin_fill()   # start filling circle with color
        r = 5.5   # set radius of circle to be drawn
        self.hex_turtle.circle(r)   # draw circle with given radius using turtle module
        self.hex_turtle.end_fill()   # stop filling circle with color

        self.hex_turtle.penup()   # lift up pen to move without drawing
        self.hex_turtle.goto(-100, 210.52)   # move turtle to (-100,210.52)
        self.hex_turtle.color(self.hex_colors[2])   # set color of turtle to third hex color
        self.hex_turtle.begin_fill()   # start filling circle with color
        r = 4.5   # set radius of circle to be drawn
        self.hex_turtle.circle(r)   # draw circle with given radius using turtle module
        self.hex_turtle.end_fill()   # stop filling circle with color

        self.hex_turtle.penup()   # lift up pen to move without drawing
        self.hex_turtle.goto(-50, 210)   # move turtle to (-50,210)
        self.hex_turtle.color(self.hex_colors[0])   # set color of turtle to third hex color
        self.hex_turtle.begin_fill()   # start filling circle with color
        r = 5.5   # set radius of circle to be drawn
        self.hex_turtle.circle(r)   # draw circle with given radius using turtle module
        self.hex_turtle.end_fill()   # stop filling circle with color

        self.hex_turtle.penup()   # lift up pen to move without drawing
        self.hex_turtle.goto(-50, 210.52)   # move turtle to (-100,210.52)
        self.hex_turtle.color(self.hex_colors[2])   # set color of turtle to third hex color
        self.hex_turtle.begin_fill()   # start filling circle with color
        r = 4.5   # set radius of circle to be drawn
        self.hex_turtle.circle(r)   # draw circle with given radius using turtle module
        self.hex_turtle.end_fill()   # stop filling circle with color

    def draw(self):  # Defining a method called draw takes in no arguments
        # Creating an instance of the Screen class
        # from the turtle module and assigning it to a local variable screen
        screen = turtle.Screen()
        # Setting up the screen with a width and height specified by
        # the instance variables width and height respectively
        screen.setup(width=self.width,
                     height=self.height)
        # Setting the title of the screen to the value of the instance variable title
        screen.title(self.title)
        # Calling a method called draw_hexagons that is not defined in
        # this code snippet but is assumed to be defined elsewhere in this class
        self.draw_hexagons()
        # Calling a method called draw_circles that is not defined in
        # this code snippet but is assumed to be defined elsewhere in this class
        self.draw_circles()
        # Hide the turtle and keep the window open
        self.hex_turtle.hideturtle()  # Hiding the turtle so it doesn't show up on screen
        turtle.done()

# Define the colors for the hexagons
hex_colors = ['orange', 'green', 'black', 'red', 'blue', 'brown']

# Create an instance of the Hexagons class and call the draw method to draw the hexagons
hexagons = Hexagons(hex_colors)
hexagons.draw()

