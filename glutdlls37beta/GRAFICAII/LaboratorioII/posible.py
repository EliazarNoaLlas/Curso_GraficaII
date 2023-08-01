import turtle

# Define the variables.
variables = ["A", "B"]
constants = []
axiom = "A"
rules = {
"A": "ABA",
"B": "BBB"
}

# Initialize the turtle.
turtle.speed(0)
turtle.left(90)

# Draw the tree.
def draw_tree(string):
    if string in variables:
        turtle.forward(10)
        turtle.pendown()
        turtle.right(45)
        draw_tree(rules[string])
        turtle.left(90)
        turtle.penup()
        turtle.forward(10)
        turtle.right(45)
        draw_tree(rules[string])
        turtle.left(90)
        turtle.pendown()
    else:
        turtle.forward(10)
        turtle.pendown()

# Draw the tree.
draw_tree(axiom)

# Wait for the user to close the window.
turtle.done()
