size(500, 500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# manual approach
'''
circle(width/2, height/2, 30)
circle(width/2, height/2, 60)
circle(width/2, height/2, 90)
'''

# loop approach
i = 0

while i < 24:
    print(i)
    circle(width/2, height/2, 30*i)
    i = i + 1
