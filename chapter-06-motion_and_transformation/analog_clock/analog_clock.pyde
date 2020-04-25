def setup():
    size(600, 600)
    frameRate(1)
    noFill()
    stroke('#FFFFFF')


def draw():
    background('#004477')
    h = hour()
    m = minute()
    s = second()
    print('{}:{}:{}'.format(h, m, s))

    translate(width/2, height/2)
    strokeWeight(3)
    circle(0, 0, 350)

    rotate(-HALF_PI)

    # hour hand
    pushMatrix()
    rotate(TAU / 12 * h)
    strokeWeight(10)
    line(0, 0, 100, 0)
    popMatrix()

    # minute hand
    pushMatrix()
    rotate(TAU / 60 * m)
    strokeWeight(5)
    line(0, 0, 130, 0)
    popMatrix()

    # second hand
    pushMatrix()
    rotate(TAU / 60 * s)
    strokeWeight(2.5)
    line(0, 0, 140, 0)
    popMatrix()
