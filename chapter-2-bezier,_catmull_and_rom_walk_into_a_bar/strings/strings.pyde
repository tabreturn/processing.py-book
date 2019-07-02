# creating a string
greeting = 'Hello, World!'
print(greeting)
whatsup = "What's up?"
question = 'Is your name really "World"?'
print(whatsup)
print(question)

# concatenation
all = greeting + ' ' + whatsup + ' ' + question
print(all)

# string formatting
all = '{} {} {}'.format(greeting, whatsup, question)
print(all)

# length
print( len(greeting) )  # displays total number of characters (13)

# slice notation
print( greeting[0] )    # displays the first character (H)
print( greeting[1] )    # displays character at index 1 (e)
print( greeting[1:4] )  # displays: ell
print( greeting[4:] )   # displays: o, World!
# everything from the fourth last character to the end of the string
print( greeting[-4:] )  # rld!
# everything from index 0 up until the fourth last character
print( greeting[:-4] )  # Hello, Wo
# everything from index 4 up until the fourth last character
print( greeting[4:-4] ) # o, Wo

# sting methods
print( greeting.upper() )       # HELLO, WORLD!
print( greeting.count('o') )    # 2
print( greeting.count('or') )   # 1
print( greeting.find('World') ) # 7
print( greeting.find('lemon') ) # -1
print( greeting.find('o',6) )   # 8
