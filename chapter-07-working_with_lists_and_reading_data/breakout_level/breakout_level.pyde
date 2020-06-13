size(600, 600)
noStroke()
background('#000000')

# ball and paddle
fill('#FFFFFF')
circle(350, 440, 18)
rect(300, 520, 190, 40)

r = '#FF0000'  # red
o = '#FF9900'  # orange
y = '#FFFF00'  # yellow
g = '#00FF00'  # green
b = '#0099FF'  # blue
p = '#6633FF'  # violet

bricks = [
  # col 0  col 1  col 2  col 3
  [ [r,1], [o,1], [y,1], [g,1] ],  # row 0
  [ [o,1], [y,1], [g,1], [b,1] ],  # row 1
  [ [y,1], [g,1], [b,1], [p,1] ],  # row 2
  [ [g,1], [b,2], [p,2], [b,1] ],  # row 3
  [ [b,1], [p,2], [   ], [g,1] ],  # row 4
  [ [p,1], [   ], [   ], [y,1] ],  # row 5
  [ [   ], [   ], [   ], [o,1] ],  # row 6
  [ [g,1], [   ], [   ], [   ] ]   # row 7
]

print(bricks[0])        # displays row 0 items
print(bricks[0][0])     # displays the very first brick
print(bricks[0][0][0])  # displays #FF0000

bw = width / 4
bh = height / 15
translate(0, bh)

for row in bricks:

    for col, brick in enumerate(row):
        
        if len(brick):
            x = col * bw
            fill(brick[0])
            rect(x, 0, bw, bh)
    
            if brick[1] == 2:
                stroke('#FFFFFF')
                strokeWeight(3)
                line(x+5, 5, x+bw-7, 5)
                line(x+5, 5, x+5, bh-7)
                noStroke()

    translate(0, bh)
