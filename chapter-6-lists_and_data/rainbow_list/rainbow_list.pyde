rainbow = ['blue', 'orange', 'yellow']

print(rainbow)      # ['blue', 'orange', 'yellow']
print(rainbow[0])   # displays: blue
print(rainbow[1])   # displays: orange
print(rainbow[2])   # displays: yellow
print(rainbow[-1])  # displays: yellow
print(rainbow[-2])  # displays: orange
print(rainbow[0:2]) # displays: ['blue', 'orange']

rainbow[0] = 'red'
print(rainbow)      # ['red', 'orange', 'yellow']

rainbow.append('blue')
print(rainbow)      # red, orange, yellow, blue

colors = ['indigo', 'violet']
rainbow.extend(colors)
print(rainbow)      # red, orange, yellow, blue, indigo, violet

yellowindex = rainbow.index('yellow')
print(yellowindex)  # 2

rainbow.insert(3, 'green')
print(rainbow)      # red, orange, yellow, green, blue, indigo, violet

i = rainbow.pop(5)  # removes indigo and assigns it to i
print(i)            # indigo
print(rainbow)      # red, orange, yellow, green, blue, violet

i = rainbow.pop()   # removes violet
print(rainbow)      # red, orange, yellow, green, blue

rainbow.extend(colors)
print(rainbow)      # red, orange, yellow, green, blue, indigo, violet
rainbow.remove('indigo')
print(rainbow)      # red, orange, yellow, green, blue, violet

size(500, 500)
noStroke()
background('#004477')

bands = [
  '#FF0000', # red
  '#FF9900', # orange
  '#FFFF00', # yellow
  '#00FF00', # green
  '#0099FF', # blue
  '#6633FF'  # violet
]

translate(0, 100)
#fill(bands[0])
#rect(0, 0, width, 50)

'''
for i in range(len(bands)):
    fill(bands[i])
    rect(0, 50*i, width, 50)
'''

#for band in bands:
for i, band in enumerate(bands):
    fill(band)
    rect(0, 0, width, 50)
    fill('#FFFFFF')
    textSize(25)
    text(i, 20,35)
    translate(0, 50)

    
    
    
