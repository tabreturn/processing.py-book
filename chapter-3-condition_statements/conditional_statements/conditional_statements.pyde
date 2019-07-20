# booleans
ball_is_red = True
ball_is_blue = False
print(ball_is_red)
print(ball_is_blue)
print(ball_is_red + True) # 2

# relational operators
x = 2
print( x > 1 )        # displays: True
print( x < 1 )        # displays: False
print( x == 2 )       # displays: True
name = 'Jo'
print( name == 'Jo' ) # displays: True
print( name != 'Em' ) # displays: True

# if statements
mark = 0

if mark < 0 or mark > 100:
    print('INVALID MARK')
elif mark >= 80:
    print('A')
elif mark >= 65:
    print('B')
elif mark >= 50:
    print('C')
elif mark >= 45 and mark < 50:
    print('RESUBMIT')
else:
    print('FAIL')
    
if not mark:
    print('WARNING: MARK IS ZERO')
