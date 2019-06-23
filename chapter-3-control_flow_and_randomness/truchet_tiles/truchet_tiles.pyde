size(600, 600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

col = 0
row = 0

for i in range(1, 145):
    
    if int(random(2)):
        arc(col,row, 50,50, 0,PI/2)
        arc(col+50,row+50, 50,50, PI,PI*1.5)
    else:
        arc(col+50,row, 50,50, PI/2,PI)
        arc(col,row+50, 50,50, PI*1.5,2*PI)

    col += 50
    
    if i%12 == 0:
        row += 50
        col = 0
