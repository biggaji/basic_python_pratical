import random
# my basic bio
firstname = "Tobiloba"
lastname = "Ajibade"
username = "bigg_aji"
languages = ["javascript", "typescript", "python", "rust", "solidity"]

#Unpack each language from the list
_lang1, _lang2, _lang3, _lang4, _lang5 = languages
print("Hello world, my name is " + firstname + " " + lastname + ", but most people calls me " + username,)
print("I code in these languages " + _lang1 + ", " + _lang2 + ", " + _lang3 + ", " + _lang4 + " and " + _lang5)
print(type(firstname))

def me():
    legend = "Super engineer 10X"
    print("I am a " + legend + "!")

me()

def genRandomNum(num1, num2):
    ranVal = random.randrange(num1, num2)
    print(ranVal)

genRandomNum(1,100000)

#python data types
#int, str, e.t.c

whoIsHe = """
Am a legend in what i do, super engineer of the super world of programming, first forbes riches dude on earth
to enter the list as a trillionaire in dollars, CEO of the greatest company the world has ever seen,
A guy who would revolutionize the fintech industry. I am bigg_aji. I am Tobi Ajibade. I am a legend!
"""

print(whoIsHe)

#They say strings are array!
name = 'Tobi Heritage Ajibade'
initials1, initials2 = name[0], name[5]

# print(initials1 + " " + initials2)

name = 'Mary'

#loop through name

for k in name:
    print(k)

# Get length of a string
print('The length of the string is ' + str(len(name)))

txt = 'The best thing in the world is free'
print("best" in txt) #returns true

if 'free' in txt:
    print('Yeah, free is present')

print('best' not in txt)

if 'expensive' not in txt:
    print('expensive is not present')

# slicing strings
#you can return a range of characters by suing the slice syntax
#tobiloba
print(firstname[:4])

b = "Hello, World!"
print(b[:5])

print(b[-5:-2])


def getSlicedPart(string,stPos,endPos):
    print(string[stPos:endPos])

getSlicedPart('Anderson',0,5)

#Modify strings
#using python built in methods

#upper case

print(name.upper());

#lowercase
print(name.upper().lower());

#remove whitesame from text
unstripedtext = '   Asynchoronous   '
print(unstripedtext.strip())
print(unstripedtext)

#replace string
print(name.replace('ry','bi'))

#split string
Fruits = 'Orange, Olive'
print(Fruits.split(','))

#concatenate Strings
#To concatenate, or combine two or more strings , you use the + operator
c = "One"
d = 'trillion'
e = c + " " + d
print(e)

#Format string
#the format() method takes it arguments, formats them and inserts them in the string in there respective
#placeholders

r = 'My name is Tobi Ajibade, and i am a {} {}. I gradated college in the year {}..'
print(r.format('Software', 'Engineer', '2016'))

#formatting based on index
curr = 'pounds'
w = 'I have {2} {0} {1} in my account!'
print(w.format(d,curr,c))


#Escape characters
#\' - Single quotes
#\\ - backslash
#\n - new line
#\r - carriage return
#\b - backspace
#\t - tab
#\f - form field


_l = "We are the so-called \nvikings from the north."
print(_l)
