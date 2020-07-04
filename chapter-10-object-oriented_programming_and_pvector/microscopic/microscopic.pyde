from amoeba import Amoeba

amoebas = []

for i in range(8):
    diameter = random(50, 200)
    speed = 1000 / (diameter * 50)
    amoebas.append(Amoeba(random(800), random(500), diameter, speed, speed))

current = PVector(0.1, -0.2)


def setup():
    size(800, 400)
    frameRate(120)


def draw():
    background('#004477')
    pointer = PVector(mouseX, mouseY)

    for a in amoebas:
        difference = pointer - a.location
        a.propulsion += difference.limit(a.maxpropulsion/100)
        a.location += a.propulsion.limit(a.maxpropulsion)
        a.location += current
        a.display()

        # wraparound

        r = a.d / 2

        if a.location.x - r > width:
            a.location.x = 0 - r
        if a.location.x + r < 0:
            a.location.x = width + r
        if a.location.y - r > height:
            a.location.y = 0 - r
        if a.location.y + r < 0:
            a.location.y = height + r

        # collision

        for b in amoebas:

            if a is b:
                continue

            distance = a.location - b.location
            sumradii = a.d/2 + b.d/2

            if distance.mag() < sumradii:
                a.propulsion += distance.limit(0.05)
                b.propulsion -= distance.limit(0.05)

                # draw a line between the centers of colliding amoeba
                line(a.location.x, a.location.y, b.location.x, b.location.y)
