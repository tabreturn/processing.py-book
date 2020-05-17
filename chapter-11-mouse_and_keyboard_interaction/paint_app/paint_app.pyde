def setup():
    size(600, 600)
    background('#004477')
    ernest = createFont('Ernest.ttf', 20)
    textFont(ernest)
    noLoop()
    cursor(CROSS)


swatches = ['#FF0000', '#FF9900', '#FFFF00', '#00FF00', '#0099FF', '#6633FF']
brushcolor = swatches[2]
brushshape = ROUND
brushsize = 3
painting = False
paintmode = 'free'
palette = 60


def draw():
    print(frameCount)
    global painting, paintmode

    if mouseX < palette:
        paintmode = 'select'

    if paintmode == 'free':

        if painting:
            stroke(brushcolor)
            strokeCap(brushshape)
            strokeWeight(brushsize)
            line(mouseX, mouseY, pmouseX, pmouseY)

        elif frameCount > 1:
            painting = True

    # black panel
    noStroke()
    fill('#000000'); rect(0, 0, palette, height)
    # color swatches
    p, p2 = palette, palette/2
    fill(swatches[0]); square(0, 0, p2)
    fill(swatches[1]); square(p2, 0, p2)
    fill(swatches[2]); square(0, p2, p2)
    fill(swatches[3]); square(p2, p2, p2)
    fill(swatches[4]); square(0, p, p2)
    fill(swatches[5]); square(p2, p, p2)
    # brush preview
    fill(brushcolor)
    if brushshape == ROUND:
        circle(30, 123, brushsize)
    paintmode = 'free'
    # clear button
    fill('#FFFFFF')
    text('CLEAR', 10, height-12)


def mousePressed():
    # start painting
    if mouseButton == LEFT:
        loop()
    # swatch select
    if mouseButton == LEFT and mouseX < palette and mouseY < 90:
        global brushcolor
        brushcolor = get(mouseX, mouseY)


def mouseReleased():
    # stop painting
    if mouseButton == LEFT:
        global painting
        painting = False
        noLoop()


def mouseWheel(e):
    # resize the brush
    global brushsize, paintmode
    paintmode = 'select'
    brushsize += e.count
    if brushsize < 3:
        brushsize = 3
    if brushsize > 45:
        brushsize = 45
    redraw()


def keyPressed():
    global brushcolor, paintmode
    paintmode = 'select'
    # color swatch shortcuts
    if key.isdigit():
        k = int(key) - 1
        if k < len(swatches):
            brushcolor = swatches[k]
            redraw()


def mouseClicked():
    # clear canvas
    if mouseButton == LEFT and mouseX < 60 and mouseY > height-30:
        fill('#004477')
        rect(palette, 0, width, height)
