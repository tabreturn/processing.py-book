size(600, 600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()

'''
# arc examples
arc(width/2,height/2, 200,200, 0,2)
arc(width/2,height/2, 300,300, 0,PI)   # half-circle
arc(width/2,height/2, 400,400, 0,PI*2) # full-circle
arc(width/2,height/2, 350,350, 3.4,(PI*2)-(PI/2), PIE)
'''

ringwidth = 70
r2 = ringwidth * 2

x = width/2
y = height/2
p214 = PI*2/14

# vacation
fill('#00FF00')
arc(x, y, r2*4, r2*4, p214*11, p214*12, PIE)

# metal
fill('#FF99FF')
arc(x, y, r2*3, r2*3, PI, p214*9, PIE)

# rap
fill('#FF99FF')
arc(x, y, r2*3, r2*3, p214*9, p214*11, PIE)

# photos
fill('#0099FF')
arc(x, y, r2*3, r2*3, p214*11, p214*13, PIE)

# work
fill('#0099FF')
arc(x, y, r2*3, r2*3, p214*13, PI*2, PIE)

# video
fill('#FF0000')
arc(x, y, r2*2, r2*2, 0, PI, PIE)

# music
fill('#FF3399')
arc(x, y, r2*2, r2*2, PI, p214*11, PIE)

# docs
fill('#6633FF')
arc(x, y, r2*2, r2*2, p214*11, PI*2, PIE)

# center
fill('#004477')
circle(x, y, r2)
