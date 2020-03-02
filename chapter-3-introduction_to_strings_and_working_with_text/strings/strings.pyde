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
firstname = 'World'
o2 = 21
hi = "Hi! I'm " + firstname + ". My atmosphere is " + str(o2) + "% oxygen."
print(hi)
hi = "Hi! I'm {}. My atmosphere is {}% oxygen.".format(firstname, o2)
print(hi)

# length
print(len(greeting))  # displays total number of characters (13)

# slice notation
url = 'http://www.nostarch.com'
print(url[0])      # displays: h
print(url[1])      # displays: t
print(url[0:7])    # displays: http://
print(url[:7])     # displays: http://
print(url[7:])     # displays: www.nostarch.com
print(url[-3:])    # displays: com
print(url[11:-4])  # displays: nostarch

# sting methods
print(url.upper())       # HTTP://WWW.NOSTARCH.COM
print(url.count('w'))    # 3
print(url.count('www'))  # 1
css = url.find('://')    # 4
protocol = url[:css]     # http
dot1 = url.find('.')          # 10
subdomain = url[css+3:dot1]   # www
dot2 = url.find('.', dot1+1)  # 19
tld = url[dot2 + 1:]          # com
domain = url[dot1+1:dot2]     # nostarch
