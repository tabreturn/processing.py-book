size(500, 320)
background('#004477')
fill('#FFFFFF')
stroke('#0099FF')
strokeWeight(3)

pangram = 'Quartz jock vends BMW glyph fix'

text(pangram, 0,50)

textSize(20)
text(pangram, 0,100)

line(
  textWidth(pangram), 0,
  textWidth(pangram), height
)

print( PFont.list() )
seriffont = createFont('Times-Roman', 20)
textFont(seriffont)
text(pangram, 0,150)

textLeading(10)
text(pangram, 0,200, 250, 100)

textAlign(RIGHT)
text(pangram, 0,250, 250, 100)
