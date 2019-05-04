# dimension of the display window in units of pixels
size(500, 500)
background('#004477')
print('Hello, World!') # writes hello world to the console area
'''
This is a multi-line comment.
Any code between the opening and closing triple-quotes is ignored.
'''
print('How are you?')

stroke('#FFFFFF')
strokeWeight(3)

# red rectangles
fill('#FF0000')
rect(100, 150, 200, 300)
rect(10, 15, 20, 30)

# orange square
fill('#FF9900')
rect(50, 100, 150, 150)

# fill-less square
noFill()
rect(250, 100, 150, 150)
fill('#FF0000')
