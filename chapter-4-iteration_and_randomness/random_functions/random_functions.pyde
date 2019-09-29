randomSeed(213)

size(600, 250)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(9)

# random functions
print( random(5) )
print( random(5,10) )
print( int(random(5,10)) )

for i in range(10):
    point(random(width), random(height))
