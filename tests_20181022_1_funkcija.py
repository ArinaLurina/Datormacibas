def thing():
    print("Hello")
    print("Fun")

thing()
print("Zip")
thing()
big = max("Hello world")
print(big)

tiny=min("Hello world")
print(tiny)
big=max("Hello world")
print(big)
print(float(99)/100)
i=42
type(i)
f=float(i)
print(f)
type(f)
print(1 + 2 * float(3)/4-5)
sval = "123"
type(sval)

#print(sval+1)

ival=int(sval)
type(ival)
print(ival + 1)

nsv = "Hello bob"
#niv = int(nsv)
def print_lyrics():
    print("I believe, I can fly")
    print("I believe, I can touch the sky")
x = 5
print("Hello")
def print_lyrics():
   print("I believe, I can fly")
   print("I believe, I can touch the sky")
print("Yo")
x = x +2
print(x)

x = 5
print("Hello")

def print_lyrics():
    print("I believe, I can fly")
    print("I believe, I can touch the sky")
print("Yo")
print_lyrics()
x = x +2
print(x)


def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
         print("Chao")
    else:
         print("Hello")

greet("en")
greet("es")
greet("fr")

def greet():
    return "Hello"
print(greet(),"Glenn")
print(greet(),"Sally")



def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
         return "Chao"
    else:
         return "Hello"

print(greet("en"),"Glenn")
print(greet("es"),"Sally")
print(greet("fr"),"Mihael")

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)

hrs = input("Enter hours:")
fhrs = float(hrs)
pay = input("Enter rate:")
fpay = float(pay)
if fhrs > 40:
    ohrs = fhrs - 40
    opay = fpay*1.5
    print(40*10+ohrs*opay)
    
