size(800, 300)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

for i in range(12):
    print(i)
    line(55, 120+i*13, 210, 50+i*13)

distance = 10;
for i in range(1,9):
    line(325, 60+distance, 480, 60+distance)
    distance *= 1.5

for i in range(13):
    if i%2 > 0:
        line( 667, 70+(13*i), 742, 70+(13*i) )
    else:
        line( 590, 70+(13*i), 665, 70+(13*i) )
    
