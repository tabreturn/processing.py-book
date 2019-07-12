y = 1

def setup():
    print(y)
    size(500,500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)

def draw():
    global y
    y += 1
    print(y)
    background('#004477')
    circle(height/2,y, 50)
