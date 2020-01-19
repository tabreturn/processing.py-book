y = 100
yspeed = 2
x = 100
xspeed = 2


def setup():
    size(800, 600)
    fill('#0099FF')
    textSize(50)


def draw():
    global y, yspeed, x, xspeed
    background('#000000')
    y += yspeed
    x += xspeed
    text('DVD', x, y)

    if y < 0+50 or y > height:
        yspeed *= -1

    if x < 0 or x > width - textWidth('DVD'):
        xspeed *= -1
