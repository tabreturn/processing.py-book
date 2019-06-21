size(500, 500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# manual approach
'''
ellipse(width/2, height/2, 30, 30)
ellipse(width/2, height/2, 60, 60)
ellipse(width/2, height/2, 90, 90)
'''

# loop approach
i = 0

while i < 24:
    print(i)
    ellipse(width/2, height/2, 30*i, 30*i)
    i = i + 1
