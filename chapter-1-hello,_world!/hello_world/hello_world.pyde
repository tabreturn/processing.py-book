# dimensions of the display window measured in pixels
size(500, 500)
background('#004477')
print('Hello, World!')  # writes hello world to the console area
'''
This is a multi-line comment.
Any code between the opening and closing triple-quotes is ignored.
'''
print('How are you?')

stroke('#FFFFFF')
strokeWeight(3)

# large red rectangle
fill('#FF0000')
rect(100, 150, 200, 300)

# small red rectangle
rect(10, 15, 20, 30)

# orange square
fill('#FF9900')
rect(50, 100, 150, 150)

# fill-less square
noFill()
square(250, 100, 150)
