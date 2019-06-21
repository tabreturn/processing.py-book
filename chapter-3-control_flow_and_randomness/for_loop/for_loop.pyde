size(500, 500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)
'''
i = 0

for i in range(24):
    print(i)
    ellipse(width/2, height/2, 30*i, 30*i)
'''
#for i in range(24):
#for i in range(10, 13): 
for i in range(0, 13, 3):
    print(i)
    ellipse(width/2, height/2, 30*i, 30*i)
