size(800, 300)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# left pattern
for i in range(12):
    print(i)
    line(55, 100+i*13, 210, 50+i*13)

# middle pattern
distance = 10
for i in range(1, 9):
    line(325, 35+distance, 480, 85+distance)
    distance *= 1.5

# right pattern
for i in range(13):
    if i % 2 > 0:
        line(665, 60+13*i, 740, 85+13*i)
    else:
        line(590, 85+13*i, 665, 60+13*i)
