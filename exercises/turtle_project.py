"""Three trees and a blue sky."""

__author__ = "730384323"


from turtle import Turtle, colormode, done 
colormode(255)


def draw_sky(width: int, height: int) -> None:
    """Draw a blue rectangle to represent the sky."""
    sky: Turtle = Turtle()
    sky.speed(200)

    # position sky
    sky.penup()
    sky.goto(-360, -90)
    sky.pendown()

    # color the sky blue
    sky.pencolor(173, 233, 254)
    sky.fillcolor(173, 233, 254)
    sky.begin_fill()
    
    # make the sky
    i: int = 0
    while (i < 2):
        sky.forward(width)
        sky.left(90)
        sky.forward(height)
        sky.left(90)
        i += 1
    
    sky.end_fill()
    sky.hideturtle()


def draw_grass(width: int, height: int) -> None:
    """Draw green rectangle to represent grass."""
    grass: Turtle = Turtle()
    grass.speed(200)

    # position grass
    grass.penup()
    grass.goto(-360, -340)
    grass.pendown()

    # color the grass green
    grass.pencolor(105, 191, 86)
    grass.fillcolor(105, 191, 86)
    grass.begin_fill()
    
    # make the grass
    i: int = 0
    while (i < 2):
        grass.forward(width)
        grass.left(90)
        grass.forward(height)
        grass.left(90)
        i += 1
    
    grass.end_fill()
    grass.hideturtle()


def draw_trunk(x: int, y: int, width: int, height: int) -> None:
    """Draw rectangles to represent tree trunks."""
    trunk: Turtle = Turtle()
    trunk.speed(200)

    # position trunk
    trunk.penup()
    trunk.goto(x, y)
    trunk.pendown()

    # color the trunks brown
    trunk.pencolor(140, 57, 57)
    trunk.fillcolor(140, 57, 57)
    trunk.begin_fill()

    # make trunk
    i: int = 0
    while (i < 2):
        trunk.forward(width)
        trunk.left(90)
        trunk.forward(height)
        trunk.left(90)
        i += 1
    
    trunk.end_fill()
    trunk.hideturtle()


def draw_leaves(leaves: Turtle, x: int, y: int, radius: int, num_circles: int) -> None:
    """Draw green circles to represent leaves."""
    leaves.speed(200)

    # position leaves
    leaves.penup()
    leaves.goto(x, y)
    leaves.pendown()

    # color leaves green
    leaves.pencolor(6, 104, 63)
    
    # recursion code for printing concentric circles 
    if num_circles == 0:
        return None
    else:
        # draw a circle with a given radius
        leaves.circle(radius)

        # recursive call with larger radius
        draw_leaves(leaves, x, y, radius + 2, num_circles - 1)
    
    leaves.hideturtle()


leaves1: Turtle = Turtle()
leaves2: Turtle = Turtle()
leaves3: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    draw_sky(710, 450)

    draw_grass(710, 250)

    draw_trunk(-25, -200, 60, 360)
    draw_trunk(-250, -150, 30, 250)
    draw_trunk(230, -125, 20, 200)

    draw_leaves(leaves1, 240, 50, 2, 50)
    draw_leaves(leaves2, -235, 50, 2, 75)
    draw_leaves(leaves3, 5, 100, 2, 100)


main()
done()

# if __name__ == "__main__":