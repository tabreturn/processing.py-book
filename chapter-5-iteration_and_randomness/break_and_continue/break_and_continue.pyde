size(660, 300)
noFill()
background('#004477')

noStroke()
fill('#FF0000')
rect(395, 0, 10, height)
rect(495, 0, 10, height)

# plain loop

for i in range(20, width, 20):
    fill('#0099FF')
    circle(i, 75, 10)

# loop with a break statement

for i in range(20, width, 20):

    if red(get(i, 1)) == 255:
        break

    fill('#FF9900')
    circle(i, 150, 10)

# loop with a continue statement

for i in range(20, width, 20):

    if red(get(i, 1)) == 255:
        continue

    fill('#00FF00')
    circle(i, 225, 10)
