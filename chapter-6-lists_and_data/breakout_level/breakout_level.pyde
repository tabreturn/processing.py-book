size(600,600)
noStroke()
background('#000000')

# ball and paddle
fill('#FFFFFF')
ellipse(350,440, 18,18)
rect(300,520, 190,40)

r = '#FF0000' # red
o = '#FF9900' # orange
y = '#FFFF00' # yellow
g = '#00FF00' # green
b = '#0099FF' # blue
p = '#6633FF' # violet

bricks = [
  [ [0,r,1], [1,o,1], [2,y,1], [3,g,1] ], # row 0
  [ [0,o,1], [1,y,1], [2,g,1], [3,b,1] ], # row 1
  [ [0,y,1], [1,g,1], [2,b,1], [3,p,1] ], # row 2
  [ [0,g,1], [1,b,2], [2,p,2], [3,b,1] ], # row 3
  [ [0,b,1], [1,p,2],          [3,g,1] ], # row 4
  [ [0,p,1],                   [3,y,1] ], # row 5
  [                            [3,o,1] ], # row 6
  [ [0,g,1]                            ]  # row 7
]

print(bricks[0])       # displays row 0 items
print(bricks[0][0])    # displays the very first brick
print(bricks[0][0][1]) # displays #FF0000

bw = width/4
bh = height/15
translate(0, bh)

for row, bricks in enumerate(bricks):

    for brick in bricks:
        x = brick[0] * bw
        fill(brick[1])
        rect(x, 0, bw, bh)

        if brick[2] == 2:
            stroke('#FFFFFF')
            strokeWeight(3)
            line(x+5, 5, x+bw-7, 5)
            line(x+5, 5, x+5, bh-7)
            noStroke()
            
    translate(0, bh)
