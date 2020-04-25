size(500, 500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# while loop version
'''
i = 0

for i in range(24):
    print(i)
    circle(width/2, height/2, 30*i)
'''

# for loop version
for i in range(24):
    print(i)
    circle(width/2, height/2, 30*i)

# to experiment with the range function, try out:
# range(10, 13)
# range(3, 13, 3)
