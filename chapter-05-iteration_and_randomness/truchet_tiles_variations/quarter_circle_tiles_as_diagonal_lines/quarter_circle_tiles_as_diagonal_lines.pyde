size(600, 600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

col = 0
row = 0

for i in range(1, 145):
    stroke('#FFFFFF')
    strokeWeight(5)
    
    if int(random(2)):
        line(col, row+25, col+25, row)
        line(col+25, row+50, col+50, row+25)
    else:
        line(col+25, row, col+50, row+25)
        line(col, row+25, col+25, row+50)

    col += 50

    if i % 12 == 0:
        row += 50
        col = 0
