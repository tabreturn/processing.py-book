# This sketch makes use of:
# The Arnolfini Portrait, Jan van Eyck, oil on oak, 1434. National Gallery, London 
# Jan van Eyck [Public domain], via Wikimedia Commons

# a function without arguments

wait = 0#5000

def printAnswer():
    print(' ------------------- ')
    print('| The answer is 42! |')
    print('| ------------------ ')
    print('|/')

print('What do you get if you multiply six by seven?')
delay(wait)
printAnswer()

delay(wait/2)
print('2. How many US gallons are there in a barrel of oil?')
delay(wait)
printAnswer()

# a function with arguments

size(561, 768)
art = loadImage('561px-Van_Eyck_-_Arnolfini_Portrait.jpg')
image(art, 0, 0, width, height)

def speechBubble(x, y, txt='Hello', type='speech'):
    noStroke()
    pushMatrix()
    translate(x, y)
    
    # tail
    if type == 'speech':
        fill('#FFFFFF')
        beginShape()
        vertex(0, 0) # tip
        vertex(15, -40)
        vertex(35, -40)
        endShape(CLOSE)
    
    elif type == 'thought': 
        fill('#FFFFFF')
        circle(0, 0, 8)
        circle(10, -20, 20)
        
    # bubble
    textSize(15)
    by = -85
    bw = textWidth(txt)
    pad = 20
    rect(0, by, bw+pad*2, 45, 10)
    fill('#000000')
    textAlign(LEFT, CENTER)
    text(txt, pad, by+pad)
    
    popMatrix()

def shout(txt):
    return txt.upper() + '!!!'

speechBubble(190, 150, shout('Check out my hat'))
speechBubble(315, 650, 'Woof')         # positional arguments
speechBubble(txt='Woof', x=315, y=650) # keyword arguments
speechBubble(445, 125, 'Meh', 'thought')
