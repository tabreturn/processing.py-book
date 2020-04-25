size(600, 600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

col = 0
row = 0

for i in range(1, 145):
    strokeWeight(7)
    r = int(random(4))
    
    if r == 0:
        arc(col, row, 50, 50, 0, PI/2)
        arc(col+50, row+50, 50, 50, PI, PI*1.5)
        
    elif r == 1:
        arc(col+50, row, 50, 50, PI/2, PI)
        arc(col, row+50, 50, 50, PI*1.5, 2*PI)
        
    elif r == 2:
        line(col+25, row, col+25, row+50)
        line(col, row+25, col+50, row+25)
        
    elif r == 3:
        line(col+25, row, col+25, row+5)
        line(col+25, row+45, col+25, row+50)
        circle(col+25, row+25, 40)
        line(col, row+25, col+5, row+25)
        line(col+45, row+25, col+50, row+25)

    col += 50

    if i % 12 == 0:
        row += 50
        col = 0
