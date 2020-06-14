def lissajousPoint(t, A, B, a, b):
    x = cos(t * a) * A
    y = sin(t * b) * B
    return [x, y]


def setup():
    size(800, 600)
    frameRate(30)
    background('#004477')
    fill('#FFFFFF')
    noStroke()


theta = 0
period = 10


def draw():
    global theta
    theta += TAU / (frameRate * period)
    # flip the y-axis and reposition the origin
    scale(1, -1)
    translate(width/2, height/2-height)

    # test curve

    x, y = lissajousPoint(theta, 200, 100, 1, 2)
    circle(x, y, 15)

    # screensaver

    for i in range(10):
        # curves
        t = theta + i / 15.0
        x1, y1 = lissajousPoint(t, 300, 150, 3, 1)
        x2, y2 = lissajousPoint(t, 250, 220, 1, 3)
        # background color
        fill(0x55000000)
        noStroke()
        rect(-width/2, -height/2, width, height)
        # line
        colorMode(HSB, 360, 100, 100)
        h = (frameCount + i * 15) % 360
        strokeWeight(7)
        stroke(h, 100, 100)
        line(x1, y1, x2, y2)
