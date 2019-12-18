size(800, 800)
background('#004477')

import json
jsondata = open('coffees.json')
coffees = json.load(jsondata) # data is typed -- no int() required

'''
coffees = [
  { 
    'name': 'espresso', 
    'ingredients': [
      ['espresso',    30, '#221100']
    ]
  },
  { 
    'name': 'espresso doppio',
    'ingredients': [
      ['espresso',    60, '#221100']
    ]
  },
    { 
    'name': 'cafe macchiato', 
    'ingredients': [
      ['espresso',    60, '#221100'], 
      ['foamedmilk',  10, '#DDDDCC']
    ]
  },
  { 
    'name': 'cafe cortado',
    'ingredients': [
      ['espresso',    60, '#221100'], 
      ['foamedmilk',  30, '#DDDDCC']
    ]
  },
  { 
    'name': 'capucchino', 
    'ingredients': [
      ['espresso',    40, '#221100'], 
      ['steamedmilk', 40, '#FFFFFF'],
      ['foamedmilk',  40, '#DDDDCC']
    ]
  },
  { 
    'name': 'americano', 
    'ingredients': [
      ['espresso',    50, '#221100'], 
      ['hotwater',    60, '#0099FF']
    ]
  },
  { 
    'name': 'black eye', 
    'ingredients': [
      ['espresso',    50, '#221100'], 
      ['brewedcoffee',50, '#443322']
    ]
  },
  { 
    'name': 'mocha', 
    'ingredients': [
      ['espresso',    50, '#221100'], 
      ['chocolate',   50, '#AA6644'], 
      ['steamedmilk', 20, '#FFFFFF']
    ]
  },
  { 
    'name': 'irish', 
    'ingredients': [
      ['espresso',    60, '#221100'], 
      ['whiskey',     40, '#FFCC77'], 
      ['whippedcream',20, '#FFFFFF']
    ]
  }
]
'''

mug = 120
col = 1
row = 1

for coffee in coffees:
    x = width/4*col
    y = height/4*row
    
    resetMatrix()
    translate(x, y)
    noStroke()
    
    pushMatrix()
    
    for ingredient in coffee['ingredients']:
        print(ingredient)
        ml = ingredient[1]
        fill(ingredient[2])
        rect(-mug/2, mug/2-ml, mug, ml)
        translate(0, -ml)
    
    popMatrix()
    
    # label
    fill('#FFFFFF')
    textSize(16)
    text(coffee['name'], -textWidth(coffee['name'])/2, 90)
    
    # mug
    strokeWeight(5)
    stroke('#FFFFFF')
    noFill()
    arc(mug/2, 0, 40, 40, -HALF_PI, HALF_PI)
    arc(mug/2, 0, 65, 65, -HALF_PI, HALF_PI)
    square(-mug/2, -mug/2, mug)
    
    if col%3 == 0:
        row += 1
        col = 1
    else:
        col += 1
    
