# booleans
ball_is_red = True
ball_is_spikey = False
print(ball_is_red)
print(ball_is_spikey)
print(ball_is_red + True) # 2
print( bool(1) )          # True
print( bool(0) )          # False

# relational operators
x = 2
print( x > 1 )        # displays: True
print( x < 1 )        # displays: False

name = 'Jo'
print( name == 'Jo' ) # displays: True
print( name != 'Em' ) # displays: True

# if statements
score = 0
print( bool(not score) )

if score < 0 or score > 100:
    print('INVALID SCORE')
elif score >= 80:
    print('A')
elif score >= 65:
    print('B')
elif score >= 50:
    print('C')
elif score >= 45 and score < 50:
    print('RETAKE TEST')
else:
    print('FAIL')

if not score:
    print('WARNING: SCORE IS ZERO')
