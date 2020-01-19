# booleans
ball_is_red = True
ball_is_spikey = False
print(ball_is_red)         # displays: True
print(ball_is_spikey)      # displays: False
print(ball_is_red + True)  # displays: 2
print(bool(1))            # displays: True
print(bool(0))            # displays: False

# relational operators
x = 2
print(x > 1)  # displays: True
print(x < 1)  # displays: False

name = 'Jo'
print(name == 'Jo')  # displays: True
print(name != 'Em')  # displays: True

# if statements
score = 0

if score < 0 or score > 100:
    print('INVALID SCORE')
elif score >= 80:
    print('A')
elif score >= 65:
    print('B')
elif score >= 50:
    print('C')
else:
    print('FAIL')

if score >= 45 and score < 50:
    print('OFFER RETAKE')

if not score:
    print('WARNING: SCORE IS ZERO')
