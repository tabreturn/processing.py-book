size(800,800)
noStroke()
grid = loadImage('grid.png')
image(grid, 0, 0)
grido = loadImage('grid-overlay.png')

translate(150, 100)
#rotate(QUARTER_PI)
scale(0.5)

# grid overlay and red square
pushMatrix()
shearY(QUARTER_PI)
image(grido, 0, 0)
fill('#FF0000')
square(0, 0, 100)
popMatrix()

# yellow square
translate(100, 0)
fill('#FFFF00')
square(0, 0, 100)
