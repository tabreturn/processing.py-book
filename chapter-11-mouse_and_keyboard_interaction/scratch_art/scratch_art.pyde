def setup():
    size(800, 400)
    frameRate(1020)
    background('#000000')
    stroke('#FFFFFF')


def draw():
    colorMode(HSB, 360, 100, 100)
    h = mouseX * 360.0 / width
    s = mouseY * 100.0 / height
    b = 100
    stroke(h, s, b)
    strokeWeight(15)

    if mousePressed and mouseButton == LEFT:
        line(mouseX, mouseY, pmouseX, pmouseY)
