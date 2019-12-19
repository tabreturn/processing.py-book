size(800,800)
image(loadImage('grid.png'), 0,0)
noFill()
stroke('#FFFFFF')
strokeWeight(6)

image(loadImage('logo_paths.png'), 0,0)

beginShape()
vertex(262,238)
vertex(262,178)
bezierVertex(262,40, 370,30, 500,30)
bezierVertex(630,30, 730,40, 735,178)
vertex(735,375)
bezierVertex(735,435, 685,488, 625,488)
vertex(375,488)
bezierVertex(295,488, 235,550, 235,630)
vertex(235,735)
vertex(175,735)
bezierVertex(40,735, 30,630, 30,500)
bezierVertex(30,375, 40,268, 175,268)
vertex(500,268)
vertex(500,238)
# eye
beginContour()
x = 368 # center-x 
y = 144 # center-y
r = 43  # radius
h = 25  # handle length
vertex(x,y-r)
bezierVertex(x-h,y-r, x-r,y-h, x-r,y)
bezierVertex(x-r,y+h, x-h,y+r, x,y+r)
bezierVertex(x+h,y+r, x+r,y+h, x+r,y)
bezierVertex(x+r,y-h, x+h,y-r, x,y-r)
endContour()
endShape(CLOSE)
