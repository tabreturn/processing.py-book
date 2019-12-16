size(800,800)
background('#004477')
tsv = loadStrings('list_of_best-selling_video_games.tsv')
noStroke()

entry1 = tsv[1].split('\t') # Minecraft entry
sales1 = entry1[2]          # 180000000
print( int(sales1) + 1 )    # 180000001

rainbow = [
  '#FF0000',
  '#FF9900',
  '#FFFF00',
  '#00FF00',
  '#0099FF',
  '#6633FF'
]

# u represts the width of the display divided by the #1 ranked sales figure
topsales = float(tsv[1].split('\t')[2])
u = width / topsales
bh = float(height) / (len(tsv)-1)

for entry in tsv[1:]:
    fields = entry.split('\t')
    bw = u * int(fields[2])
    bx = 0
    by = bh * (int(fields[0])-1)
    fill( rainbow[(int(fields[0])-1) % len(rainbow)] )
    rect(bx, 0, bw, bh)
    fill(0)
    text( fields[1], bx+5, bh-3 )
    translate(0, bh)
