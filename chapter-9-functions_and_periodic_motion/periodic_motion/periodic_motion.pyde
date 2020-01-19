def circlePoint(t, r):
    x = cos(t) * r
    y = sin(t) * r
    return [x, y]


def ellipsePoint(t, hr, vr):
    x = cos(t) * hr
    y = sin(t) * vr
    return [x, y]


def setup():
    size(800, 600)


radius = 200
theta = 0
period = 2.1


def draw():
    global theta, radius
    theta += TAU / (frameRate * period)

    background('#004477')
    noFill()
    strokeWeight(3)
    stroke('#0099FF')
    line(width/2, height, width/2, 0)
    line(0, height/2, width, height/2)
    # flip the y-axis
    scale(1, -1)
    translate(0, -height)
    # reposition the origin
    translate(width/2, height/2)
    circle(0, 0, radius*2)

    noStroke()
    fill('#FFFFFF')

    # circular motion
    x, y = circlePoint(theta, radius)
    circle(x, y, 15)

    # spiral motion
    x, y = circlePoint(theta, frameCount)
    circle(x, y, 15)

    # elliptical motion
    x, y = ellipsePoint(theta, radius*1.5, radius)
    circle(x, y, 15)

    # single dot wave
    amplitude = radius
    y = sin(theta) * amplitude
    circle(0, y, 15)

    # multi dot wave
    for i in range(51):
        x = -400 + i * 16
        t = theta + i * 0.25
        y = sin(t) * amplitude
        circle(x, y, 15)

    # weight hanging from a spring
    noFill()
    stroke('#FFFFFF')
    strokeJoin(ROUND)
    bends = 35
    beginShape()
    for i in range(bends):
        vx = 30 + 60 * (i % 2 - 1)
        vy = 300 - (300 - y) / (bends - 1) * i
        vertex(vx, vy)
    endShape()
    rect(-100, y-80, 200, 80)

    # reducing the amplitude or radius
    if radius > 0:
        radius -= 0.1
