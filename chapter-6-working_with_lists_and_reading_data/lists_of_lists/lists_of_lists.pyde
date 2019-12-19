size(500, 380)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

h = 50
translate(100, 40)

bands = 6
rect(0, 0, 40, h*bands)

# 1-dimensional

bands1 = [
  '#FF0000',
  '#FF9900',
  '#FFFF00',
  '#00FF00',
  '#0099FF',
  '#6633FF'
]

for band in bands1:
    fill(band)
    rect(0, 0, 40, h)
    translate(0, h)
    
# 2-dimensional

bands2 = [
  [100, 0, 0, 'red'],
  [100, 60, 0, 'orange'],
  [100, 100, 0, 'yellow'],
  [0, 100, 0, 'green'],
  [0, 60, 100, 'blue'],
  [40, 20, 100, 'violet']
]

print( bands2[1][1] ) # 60

colorMode(RGB, 100)
resetMatrix()
translate(100, 40)

for band in bands2:
    r = band[0]
    g = band[1]
    b = band[2]
    
    #sum = r + g + b
    #avg = sum / 3
    #fill(avg, avg, avg)
    #rect(0, 0, sum, h)
    
    fill('#FF0000')
    rect(0, 0, r, h)
    fill('#00FF00')
    rect(r, 0, g, h)
    fill('#0099FF')
    rect(r+g, 0, b, h)
    fill('#FFFFFF')
    
    textAlign(RIGHT)
    text(band[3], -20,30)
    translate(0, h)
