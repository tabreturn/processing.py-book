def setup():
    size(500, 500)
    background('#004477')
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    frameRate(25)


def draw():
    background('#004477')
    hide = frameCount % 8

    if hide != 0:
        circle(250, 80,  80)
    if hide != 1:
        circle(370, 130, 80)
    if hide != 2:
        circle(420, 250, 80)
    if hide != 3:
        circle(370, 370, 80)
    if hide != 4:
        circle(250, 420, 80)
    if hide != 5:
        circle(130, 370, 80)
    if hide != 6:
        circle(80, 250,  80)
    if hide != 7:
        circle(130, 130, 80)
