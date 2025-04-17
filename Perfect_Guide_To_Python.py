#types of data
bool, str, list, tuple, set, dict, range, None, bin, int, float, complex, bytes
print(bin(5))           #output: 0b101
print(int(0b101))       #output: 5


#checking type of data
print(type(2-4))                #output: <class 'int'>
print(type(2/4))                #output: <class 'float'>
print('Hello'+' World'+'!')     #output: Hello World!   #string concatenation
print(type(int(str(100))))                #output: <class 'int'>


#order in math symbols
1. ()                   #nawiasy
2. (**)                 #potęgowanie                    Exponentiation
3. * and /              #mnożenie i dzielenie           Multiplication and Division
4. + and -              #dodawanie i odejmowanie     	Addition and Subtraction
print((20-3)+2**2)      #output: 21


#other operators
%                       #Modulo
//                      #Floor divison
=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=                   #assignment operators
== ('equal'), != ('not equal'), > ('greater than'), < ('less than'),    #comparison operators
>= ('greater than or equal to'), <= ('less than or equal to')           #comparison operators
and ('returns True if both are true')   #if x and y:                            #logical operators
or ('returns True if either is true')   #if x or y:                             #logical operators
not ('reverse the result, returns False if result is True')  #if not(x and y):  #logical operators
is ('returns True if both are the same object')  #if x is y:                    #identity operators
is not ('returns True if both are not the same object')  #if x is not y:        #identity operators
in ('returns True if a sequence with the specified value is present in the object') #if x in y:         #membership operators
not in ('returns True if a sequence with specified value is not present in the object') #if x not in y  #membership operators
#bitwise operators (to compare binary numbers)
& ('AND - sets each bit to 1 if both are 1')                            | ('OR - sets each bit to 1 if one of two bits is 1')
^ ('XOR - sets each bit to 1 if ONLY one of two bits is 1')             ~ ('NOT - inverts all the bits')
<< ('Zero fill left shift - shift left by pushing zeros in from the right and the the leftmost bits fall off')
>> ('Signed right shift - shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off')


#augumented assignment operator
someValue=5
someValue+=2
print(someValue)        #output: 7
someValue-=3
print(someValue)        #output: 4


#multiline
longString = '''        #output: WOW
WOW                     #output: 0 0
0 0                     #output: ---
---
'''
print(longString)


#escape sequence with "\"
var = "It\\s \"kind of\" sunny."
var2 = "\n\t It\'s \"kind of\" sunny. \n hope you have...\na good day!"
print(var, var2)
#output:
#It\s "kind of" sunny. 
#         It's "kind of" sunny.
# hope you have...
#a good day!


#text formatting
txt="Hello World"
print(txt[2:5])              #to get characters from index 2 to 4      #output: llo
txt2=" Hello World "
print(txt2.strip())          #to return the string without any whitespace at the begining or the end     #output: Hello World
print(txt.replace('H', 'J')) #to swap first char with second           #output: Jello World



#formatted strings
name = 'Johnny'
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old')
print(f'hi {name}. You are {age} years old')
print('hi {}. You are {} years old'.format('Johnny', '55'))
print('hi {1}. You are {0} years old'.format(name, age))
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))
#output:
#hi Johnny. You are 55 years old
#hi Johnny. You are 55 years old
#hi Johnny. You are 55 years old
#hi 55. You are Johnny years old
#hi sally. You are 100 years old


#inputs
birth_year = input('What year were you born? ')
age = 2023 - int(birth_year)
print(f'Your age is: {age}.')
#output:
#What year were you born? 2000
#Your age is: 23.
username=input('What is your username? ')
password=input('What is your password? ')
passwordLength=len(password)
hiddenPassword= '*' * passwordLength
print(f'{username}, your password, {hiddenPassword}, is {passwordLength} letters long.')
#output:
#What is your username? Ezio
#What is your password? 999999
#Ezio, your password, ******, is 6 letters long.


#List slicing
amazonCart = [             #listName[0:6:3]     x[start:stop:step]
    'notebooks',            #zaczyna od 0, kończy na 6, wybiera co trzeci wyraz listy
    'sunglasses',          #newListName2 = listName1
    'toys',                 #jakiekolwiek zmiany w newListName2 zmienią i nadpiszą listName1
    'grapes'               #newListName2 = listName1[:]
]                           #jakiekolwiek zmiany w newListName2 NIE zmienią pierwotnej listy listName1
amazonCart[0] = 'laptop'
newCart = amazonCart[:]
newCart[0] = 'gum'
print(newCart)
print(amazonCart)
#output:
#['gum', 'sunglasses', 'toys', 'grapes']
#['laptop', 'sunglasses', 'toys', 'grapes']


#matrix (listy w listach)
listName = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
listName2 = [
    [[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]]
]
print(listName[0][1]) #index po amerykańsku od 0 są, tedy piersza wartość ma index 0
#output: 2       #bierzemy z zewnętrznej listy index 0 i z wewnętrznej index 1
print(listName2[1][1][0][1])
#output 14


#adding in terms of lists
basket = [1,2,3,4,5]
newList = basket.insert(3, 100)         #insert wstawia w wybrane miejsce wpisaną wartość
print(basket)                           #output: [1, 2, 3, 100, 4, 5]
print(newList)                          #output: None           #doesn't return any value
newList2 = basket.append(200)           #append dodaje na koniec listy wpisaną jedną wartość
print(basket)                           #output: [1, 2, 3, 100, 4, 5, 200]
newList3 = basket.append([300, 400])
print(basket)                           #output: [1, 2, 3, 100, 4, 5, 200, [300, 400]]
print(newList2)                         #output: None           #doesn't return any value
print(newList3)                         #output: None           #doesn't return any value
newList4 = basket.extend([500, 600])    #extend dodaje na koniec listy wiele elementów
print(basket)                           #output: [1, 2, 3, 100, 4, 5, 200, [300, 400], 500, 600]
print(newList4)                         #output: None           #doesn't return any value
newList5 = basket + [700]
print(basket)                           #output: [1, 2, 3, 100, 4, 5, 200, [300, 400], 500, 600]
print(newList5)                         #output: [1, 2, 3, 100, 4, 5, 200, [300, 400], 500, 600, 700]


#deleting in terms of lists
cart = [10, 1, 1, [1, 1], 2, 2, [2, 2], 3, 3, [3,3], 4, 4, [4, 4], 5, 5, [5, 5]]
newList6 = cart.pop()                #usuwa wybrany index, [domyślnie "()" usuwa ostatni index z listy]
print(cart)                          #output: [10, 1, 1, [1, 1], 2, 2, [2, 2], 3, 3, [3, 3], 4, 4, [4, 4], 5, 5]
print(newList6)                      #output: [5, 5]         #zwraca usuniętą wartość
newList7 = cart.pop(10)              #na 10 idexie, jest cyfra 4 
print(cart)                          #output: [1, 1, [1, 1], 2, 2, [2, 2], 3, 3, [3, 3], 4, 4, [4, 4], 5, 5] 
print(newList7)                      #output: 4              #zwraca usuniętą wartość
newList8 = cart.remove(1)            #usuwa podaną wartość, NIE po indexie, [jeżeli jest kilka to usunie tylko najwcześniejszą]
print(cart)                          #output: [10, 1, [1, 1], 2, 2, [2, 2], 3, 3, [3, 3], 4, [4, 4], 5, 5]
print(newList8)                      #output: None           #doesn't return any value
newList9 = cart.clear()              #usuwa całą zawartość
print(cart)                          #output: []
print(newList9)                      #output: None           #doesn't return any value


#various operations on lists
storage = ['a', 'e', 'b', 'c', 'd', 'b']
print('x' in storage)                #output: False
print('d' in storage)                #output: True
print(storage.count('d'))            #output: 1         #to count how many times the things occurs
print(sorted(storage))               #output: ['a', 'b', 'b', 'c', 'd', 'e']    #posortowane
print(storage)                       #output: ['a', 'e', 'b', 'c', 'd', 'b']
storage.sort()
print(storage)                       #output: ['a', 'b', 'b', 'c', 'd', 'e']    #posortowane
newStorage2 = storage.copy()
print(newStorage2)                   #output: ['a', 'b', 'b', 'c', 'd', 'e']
newStorage2.reverse()
print(newStorage2)                   #output: ['e', 'd', 'c', 'b', 'b', 'a']    #reversed
print(newStorage2[::-1])             #output: ['a', 'b', 'b', 'c', 'd', 'e']    #reversed once more
sentence = '!'
newSentence = sentence.join(['Hi', 'my', 'name', 'is', 'Jojo.'])
print(newSentence)                   #output: Hi!my!name!is!Jojo.
newSentence = ' '.join(['Hi', 'my', 'name', 'is', 'Jojo.'])
print(newSentence)                   #output: Hi my name is Jojo.

print(list(range(20)))               #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a, b, c, other, d)             #output: 1 2 3 [4, 5, 6, 7, 8] 9


#Dictionary
dictionary = {                      #key= 'a':
    'a': [1,2,3],                   #value= '[1,2,3]
    'b': 'hello',
    'c': True
}
myListInDictionary = [
{
    'a': [1,2,3],
    'b': 'hello',
    'c': True
},
{
    'a': [4,5,6],
    'b': 'hello',
    'c': True
}]
print(dictionary['a'])                      #output: [1,2,3]    #print values from key='a' z dict
print(dictionary['a'][1])                   #output: 2          #print index '1' z from key='a'
print(myListInDictionary[1]['a'][2])        #output: 6
print(dictionary.get('d', 55))              #output: 55         #if 'd' doesn't exist in the dictionary, use value=55 as default
print(dictionary.get('b', 'bye'))           #output: hello
dictionary['c'] = False     #to change value of key
dictionary['d'] = 69        #to the key/value pair to the dictionary


#Tuple
myTuple = (1,2,3,4,5)    #tuples are like lists, but unlike lists we cannot modify them
#myTuple[1] = 'z'        #output: TypeError
print(myTuple.count(3))  #output: 1         #number 3 occurs 1 time
print(myTuple.index(4))  #output: 3         #value=4 has index number 3


#Set
myList = [99,98,98,99]
print(set(myList))                      #output: {98, 99}           #so transforming to list to set, removes duplicates
mySet = {1,2,3,4,5,5}                   #sets are unordered collections of UNIQUE objects
print(mySet)                            #output: {1, 2, 3, 4, 5}    #nie ważne jak zdefiniujemy set, powtórzenia wartości znikną
mySet.add(100)
mySet.add(2)
print(mySet)                            #output: {1, 2, 3, 4, 5, 100}
YourSet = {4,5,6,7,8,9,10}
print(mySet.difference(YourSet))        #output: {1, 2, 3, 100}     #pokazuje wartości pierwszego seta, których nie ma w drugim 
print(mySet)                            #output: {1, 2, 3, 4, 5, 100}       #nie nadpisuje seta .difference()
print(mySet.intersection(YourSet))      #output: {4,5}              #wypisuje wspólne wartości
mySet.discard(5)
print(mySet)                            #output: {1, 2, 3, 4, 100}  #usunięta 5 po discard(5)
mySet.difference_update(YourSet)        #permamentnie usuwa wartość w pierwszym, które występują też w drugim
print(mySet)                            #output: {1, 2, 3, 100}
print(mySet.isdisjoint(YourSet))        #output: True               #sprawdza czy "nienachodzą" na siebie (True jeśli nienachodzą)
mySet.update(YourSet)                   #.update zmienia set na zawsze, pozostawiając różnice przy porównywaniu
print(mySet)                            #output: {1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10}   #update'uje set o iterable object
print(mySet.issubset(YourSet))          #output: False
print(mySet.issuperset(YourSet))        #output: True               #True, ponieważ YourSet zawiera się w MySet
print(mySet)
print(YourSet)

ThirdSet = {1,12,13,14,14}
print(ThirdSet.union(mySet, YourSet))   #returns a set that contains all items from the original set, and all items from the specified set(s)
#                                       #output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 100}


#Truthy and Falsy - all values are considered "truthy" except for the following, which are "falsy":
None, False,
30, 0.0, 0j, decimal.Decimal(0), fraction.Fraction(0, 1),    #numbers that numerically equals to zero
[], {}, (), set(),                                           #empty list, dict, tuple, set
'', b'', bytearray(b''), memoryview(b''),                    #empty str, bytes, bytearray, memoryview
range(0)                                                     #empty range
obj.__bool__()          #object for which returns false 
obj.__len__()           #object for which returns 0, given that obj.__bool__ is undefined


#Short Circuiting
print('a' > 'A')            #output: True
print(not(1 == 1))          #output: False
print(True == 1)            #output: True
print('' == 1)              #output: False
print([] == 1)              #output: False
print(10 == 10.0)           #output: True
print([] == [])             #output: True
print(True is 1)            #output: False
print('1' is 1)             #output: False
print([] is 1)              #output: False
print(10 is 10.0)           #output: False
print([1,2,3] is [1,2,3])   #output: False
print(True is True)         #output: True
print('1' is '1')           #output: True
print([] is [])             #output: False
print(10 is 10)             #output: True
a, b = [1,2,3], [1,2,3]
print(a is b)               #output: False     


#for looping
for item in 'Byee':         for item in (1,2,3,4):              for item in (1,2):
    print(item)                 print(item)                         for x in ['a', 'b']:   
#output: B                  #output: 1                                  print(item, x)
#output: y                  #output: 2                          #output: 1 a
#output: e                  #output: 3                          #output: 1 b
#output: e                  #output: 4                          #output: 2 a
user = {                                                        #output: 2 b
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in user:           for item in user.items():               for item in user.values():          for item in user.keys():
    print(item)                 print(item)                             print(item)                         print(item)
#output: name               #output: ('name', 'Golem')              #output: Golem                      #output: name
#output: age                #output: ('age', '5006')                #output: 5006                       #output: age
#output: can_swim           #output: ('can_swim', 'False')          #output: False                      #output: can_swim
for item in user.items():
    key, value = item;                      for key, value in user.items():
    print(key, value)                           print(key,value)
#output: name Golem                         #output: name Golem
#output: age 5006                           #output: age 5006
#output: can_swim False                     #output: can_swim False
myNewList, counter = [[1,2,3,4,5,6,7,8,9,10], 0]
for i in myNewList:
    counter = counter + i
print(counter)
#output: 55
someList,duplicates=[['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'],[]]
for value in someList:  #loops exercise - check for duplicates
    if someList.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


#range()
for number in range (0, 4):         for _ in range(0, 4, 2):        for _ in range(2,0,-1):             for _ in range(2):
    print(number)                       print(_)                        print(_)                            print(list(range(5)))
#output: 0                          #output: 0                      #output: 2                          #output: [0,1,2,3,4]
#output: 1                          #output: 2                      #output: 1                          #output: [0,1,2,3,4]
#output: 2                                                          #output: 0
#output: 3                          od 0 do 10 co 2                 od 2 do 0 co 1 w dół                dwie rzeczy po 5 reczy


#enumerate()
for i,char in enumerate('Helo'):            for i,char in enumerate((1,2,3)):               for i,char in enumerate(list(range(3))):
    print(i, char)                              print(i,char)                                   print(i,char)
;                                                                                                   if char == 1: print(f'Index of 1 is: {i}')
#output: 0 H                                ############                                    #########################
#output: 1 e                                #output: 0 1                                    #output: 0 0
#output: 2 l                                #output: 1 2                                    #output: Index of 1 is: 1
#output: 3 o                                #output: 2 3                                    #output: 2 2

#while looping
whileint, whilejnt = [0, 0]                 #output: 0
while whileint < 3:                         #output: 1
    print(whileint)                         #output: 2
    whileint+=1                             #output: done with the work
    if whilejnt == 1: break                 #break stop whole function, when condition is met, but here $whilejnt will never meet it
else:
    print('done with the work')
#break, continue, pass - applies also to other loops
while True:                                                         #output:
    respone = input('say: ')                                        #say: 2
    if (respone == 'hi'):                                           #2
        continue   #skip whats below and continue with function     #say: hi
        print('not hi for you')                                     #say: welcome
    if (respone == 'bye'):                                          #welcome
        break      #breaks, stops the function completely           #say: bye
    if (respone == 'welcome'):
        pass       #placeholder for the future
    print(respone)


#functions
myForList = [                   #functions should:
    [0,0,0,1,0,0,0],                #do one thing really well
    [0,0,1,1,1,0,0],                #return something
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def snowTree():                                                         #output:
    for row in myForList:                                               #   *
        for pixel in row:                                               #  ***
            if (pixel): #if (pixel) - means if it is true  true=1       # *****
                print('*', end='')                                      #*******
            else:                                                       #   *
                print(' ', end='')                                      #   *
        print('')
snowTree()      #always need to call out the function to use it
def highestEven(li):
    #docstring ''' '''
    ''' 
    Info: this functions is to find out the highest even number from provided numbers.
    ''' 
    #so you can see this describtion when you will try writing calling-out-instruction
    #or when using instruction "help(highestEven)" or "print(highestEven.__doc__"
    evenNumbers=[]
    for get_EvenNumber in li:
        if get_EvenNumber % 2 == 0:
            evenNumbers.append(get_EvenNumber)
    return max(evenNumbers)
print(highestEven([10,2,3,4,5,6,11]))      #output: 10


#parameters
def summing(num1,num2):
    def anotherFunc(num1,NUMBER2):
        return num1 + NUMBER2
    return anotherFunc(num1,num2)
def sayHello(name,emoji):
    print(f'Hello, {name} {emoji}')
#arguments
print(summing(10,5))                            #output: 15 
sayHello('Grzegorz', ':)')                      #output: Hello, Grzegorz :)
#default parameters
def sayGoodbye(name="Cecil",emoji=";("):        #if we don't provide arguments when calling out, defaults will be used
    print(f'Goodbye, {name} {emoji}')
#no arguments
sayGoodbye()                                    #output: Goodbye, Cecil ;(
#keyword arguments
sayGoodbye(emoji='O.O',name='DefinitlyNotName') #output: Goodbye, DefinitlyNotName O.O


#if, elif, else
def checkDriverAge():
    age=input('What\'s your age?: ')
    if int(age) < 18:
        print('Sorry, you are too young.')
    elif int(age)>18:
        print('Enjoy ride.')
    else:
        print('Your first year of driving')     #output: What's your age?: 19
checkDriverAge()                                #output: Enjoy ride.


# *args     (unknown amount of arguments) 
# **kwargs  (unknown amount of keyarguments)
# putting '*' means the function can accept any number of positional arguments
#Rule: parameters, *args, default parameters, **kwargs
def superFunc(*args):
    print(*args)
    #using print(args) will give #output: (1, 2, 3, 4, 5)
    return sum(args)
superFunc(1,2,3,4,5)         #output: 1 2 3 4 5
print(superFunc(1,2,3,4,5))  #output: 1 2 3 5 5   #and in new line: 15
def SuperiorFunc(*xxx,**kwargs):
    print(kwargs)
    return sum(xxx)                             #output: {'num1': 5, 'num2': 10}
print(SuperiorFunc(1,2,3,4,5, num1=5,num2=10))  #output: 15
def combinedFunc(*args,**kwargs):
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args) + total
print(combinedFunc(1,2,3,4,5, num1=5,num2=10))  #output: 30


#walrus operator
# ":=" assigns values to variables as part of a larger expression
a = 'hello'
if ((n := len(a))>4):
    print(f"too long {n} elements")         #output: too long 5 elements
while (n := len(a) >1):                     #output: 4x True        #z racji is do 'n' przypisuje instrukcje porównania
    print(n)
    a=a[:-1]
while ((n := len(a)) >1):                   #output: 5
    print(n)                                #output: 4
    a=a[:-1]                                #output: 3
print(a)                                    #output: 2
#                                           #output: h


#scope - what variables do I have access to?
# #1 - local
# #2 - parent local?
# #3 - global
# #4 - built-in python functions    (nonlocal too(?))
a=1
def confusion():
    a =5
    return a
print(confusion())          #output: 5      ponieważ w funkcji confusion() zmieniamy a z 1 na 5
print(a)                    #output: 1      ponieważ a=5 obowiązuje wewnątrz fuckji confusion()
def Anotherconfusion():
    global a                #so we can use a outside of the function too
    a = 10
    return a
print(Anotherconfusion())   #output: 10
print(a)                    #output: 10


#shorthand syntax
print("Yes") if 5>2 else print('No')                        #output: Yes
print('toReverseString'[::-1])                              #output: gnirtSesreveRot
reduce((lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n))) #Sieve of Eratosthenes
print([(x, y) for x in range(3) for y in range(3)])         #output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
x,y,z=[5,10,15], if x < y < z: print(x); print(y); print(z) #output: 5 10 15 #each in newlines
ls = lambda a, b: len(b) if not a else len(a) if not b else min(ls(a[1:], b[1:])+(a[0] != b[0]), ls(a[1:], b)+1, ls(a, b[1:])+1)
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))
#list comprehension
myList1=[char for char in 'hello']
print(myList1)                                          #output: ['h', 'e', 'l', 'l', 'o']
print(list(num**3 for num in range(0,10) if num%2==0))  #output: [0, 8, 64, 216, 512]
#set comprehension      #set can work as function that deletes duplicates
duplicates=['a','b','c','b','d','m','n','n']    #here it shows us chars that were duplicated
print(list(set([x for x in duplicates if duplicates.count(x)>1])))  #output: ['b', 'n']
print(set([x for x in duplicates if duplicates.count(x)>1]))        #output: {'b', 'n'}
#dictionary comprehension
simpleDict={'a':1,'b':2,'c':3,'d':4}
print({key:value**2 for key,value in simpleDict.items() if value %2==0})                #output: {'b': 4,'d': 16}
print({key:value**2 for key,value in {'a':1,'b':2,'c':3,'d':4}.items() if value %2==0}) #output: {'b': 4,'d': 16}
print({num+10:num*2 for num in [1,2,3]})                                                #output: {11: 2, 12: 4, 13: 6}



#classes    #OOP - object oriented programming
'''class object attribute - is static and never changes'''
'''constructors attribute - is dynamic and can change'''
class Person:   #all classes have function __init__(), which is always executed when the class is being initiated
    '''Example Class'''
    membership = True   #class object attribute
    def __init__(self,name,age):    #self - odnosi się do nazwy classy      #self.name - to nazwa obkietu utworzonego classą
        '''Example Setup'''
        self.name = name    #attributes     #to assign values to object properties
        self.age = age
    def printname(self):
        '''Example instance method'''
        '''instance methods - able to access data and properties'''
        print(self.name)
p1 = Person("John", 36)     #object of class Person
print(p1.name)  #output: John   #use the p1 object to print the value of name
print(p1.age)  #output: 36
print(p1)   #output: <__main__.Person object at 0x7f4b26d15fd0>
p1.printname()  #output: John   #encapsulation

'''@staticmethod vs @classmethod:
class method odwołuje się do nazwy classy w pierwszym swoim argumencie (cls, ...), 
bezwzględu na to czy ów cls umieścimy czy nie, on i tak będzie pierszym argumentem'''
class DecoratorExample():
    def __init__(self):
        self.name = 'DecoratorExample'
    def exampleFunction(self):
        print('My name is ' + self.name + '.')
    @classmethod    #can access limited methods in the class, can modify class specific details
    def anotherFunction(cls):
        cls.someOtherFunction()
    @staticmethod   #cannot access anything else in the class, totally self-contained code
    def someOtherFunction():
        print('Hello.')
de = DecoratorExample()
de.exampleFunction()    #output: My name is DecoratorExample.
de.anotherFunction()    #output: Hello.     #classmethod wywołało staticmethod

class Student(Person):  #inheritance    #classes that inherit other class'es properties and methods
    pass
x=Student('Mike', 33)   #to create an object named x from class student
x.printname()   #output: Mike   #to execute the printname() of the object x

'''Encapsulation''' #is the binding of data and functions that manipulate that data. 
#And we encapsulate into one big object, so that we keep everything in this box that users or code or other machines can interact with.
'''Abstraction''' #means hiding of information or abstracting away information and giving access to only what is necessary.
#In other languages we can have Public and Private variables, but in python we do not.
'''Inheritance''' #allows objects to take on properties of existing objects. So you can inherit classes.
'''Polymorphism''' #refers to the way in which object classes can share the same method name. 
#But those method names can act differently based on what object calls them.
class User(): 
    def signIn(self): print('logged in')
class Wizard(User):
    def __init__(self,name,power): self.name, self.power = [name, power]
    def attack(self): print(f'attacking with power of {self.power}')
class Archer(User):
    def __init__(self,name,arrows): self.name, self.arrows = [name,arrows]
    def attack(self): print(f'attacking with arrows: arrows left - {self.arrows}')
class HybridBorg(Archer, Wizard):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
wizard1, archer1, hb1= [Wizard('Merlin', 50), Archer('Robin', 100), HybridBorg('borgie',50,100)]
wizard1.attack()    #output: attacking with power of 50
archer1.attack()    #output: attacking with arrows: arrows left - 100
hb1.attack()        #output: attacking with arrows: arrows left - 100

class Pets():
    animals=[]
    def __init__(self,animals): self.animals=animals
    def walk(self):
        for animal in self.animals: print(animal.walk())
class Cat():
    is_lazy=True
    def __init__(self,name,age): self.name,self.age=[name,age]
    def walk(self): return f'{self.name} is just walking around'
class Simon(Cat):
    def sing(self,sounds): return f'{sounds}'                       #output: Simon is just walking around
class Sally(Cat):                                                   #output: Sally is just walking around
    def sing(self,sounds): return f'{sounds}'                       #output: Suzy is just walking around
class Suzy(Cat):
    def sing(self,sounds): return f'{sounds}'
myCats=[Simon('Simon',4),Sally('Sally',21),Suzy('Suzy',1)]
myPets=Pets(myCats) #instantiate the Pet class with all your cats
myPets.walk()

'''two ways of calling functions from higher classes'''
class UserA(object):
    def __init__(self, email): self.email = email
    def signIn(self): print('logged in')
class MagicMan(UserA):
    def __init__(self, name, power, email):
        UserA.__init__(self, email)
        self.name, self.power=[name,power]
class WarriorMan(UserA):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name, self.power=[name,power]




#dunder functions       #__something__
class Toy():
    def __init__(self,color,age): self.color,self.age=[color,age]
    def __str__(self): return f'{self.color}'
    def __len__(self): return 5
    def __del__(self): return 'deleted'
actionFigure = Toy('red',0)
print(actionFigure.__str__())   #output: red
print(str(actionFigure))        #output: red


#introspection - object introspections shows us what object has access to
wizard1=Wizard('Merlin', 60, 'merlin@gmail.com')
print(dir(wizard1))      #potential output: '__gt__', '__hash__', '__init__'  etc..


#map, filter, zip, reduce
def multiply_by2(item):  #map(function,iter)  #map() function returns a map object(which is an iterator) of the results 
    return item*2                             #after applying the given function to each item of a given iterable (list, tuple etc.)
print(map(multiply_by2,[1,2,3]))              #output: <map object at 0x7fc93c6551f0>
print(list(map(multiply_by2,[1,2,3])))        #output: [2, 4, 6]
def is_smart(score):            #filter(action,data)   #Na podstawie "action" sprawdza każdy fragment z "data" na zasadzie True/False,
    return score > 50                                  #i jeśli jest True, to zwraca dany fragment, a jeżeli False to się go pozbywa.
print(filter(is_smart, [73,20,65,19,76,100,88]))       #output: <filter object at 0x7f281fedbfa0>
print(list(filter(is_smart,[73,20,65,19,76,100,88])))  #output: [73, 65, 76, 100, 88]
myStrings,myNumbers=[['a','b','c','d','e'],[5,4,3,2,1]] #Iterates over each data structure and zips them together. Creates new data, instead of overriding.
print(list(zip(myStrings, sorted(myNumbers))))          #output: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
from functools import reduce                               #reduce(action,data,initialValue)
my_num,my_score=[[3,2,1],[20,80,50]]                       #Apply a function of two arguments cumulatively to the items of a sequence or iterable,
def accumulator(acc,item): return acc+item                 #from left to right, so as to reduce the iterable to a single
print(reduce(accumulator, (sorted(my_num)+my_score)))      #output: 156


#lambda function                           #to create very short, especially one line, functions
# "lambda arguments : expression"          #Lambda expression - is to be used once, it is anonymous function, no need to store them
myTest=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda item: item*2, myTest)))           #output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(list(filter(lambda item: item%2 != 0, myTest)))   #output: [1, 3, 5, 7, 9]
from functools import reduce
print(reduce(lambda acc,item: acc+item, myTest))        #output: 55
print(myTest)                                           #output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TestNr2=[(0,2),(4,3),(10,-1),(9,9)]
TestNr2.sort()                      #sorting with first value
print(TestNr2)     #output: [(0, 2), (4, 3), (9, 9), (10, -1)]
TestNr2.sort(key=lambda x:x[1])     #sorting with second value
print(TestNr2)     #output: [(10, -1), (0, 2), (4, 3), (9, 9)]


#importing
import math as matematyka     #to refer to a module by using different name, using alias       #useful if two modules have same names
from PIL import Image         #to import only a certain things from libraries
print(dir(matematyka))        #to print all variables and function names of the math library
help(matematyka)              #describies module for us
#example:
from random import randint 
import sys
answer=randint(int(sys.argv[1]),int(sys.argv[2]))   #sys.argv to input z konsoli podczas wpisywania egzekucji pliku
while True:                                         #$ file.py argument1 argument2
    try:
        guess= int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}: '))
        if sys.argv[1] < guess <sys.argv[2]:
            if guess == answer:
                print('you are a genius')
                break
    except ValueError:
        print('please enter a number')
        continue 


#idea for decorators
def Hello(function): function() #funkcja Hello() może tak wywołać każdą funkcje
def Greet(): print('Hi!')
Hello(Greet) #output: Hi!
#decorators 
#decorators boosts the functions with additional actions
def myDecorator(function):  #this function is how it looks like most of the time
    def wrapFunc():         #so it can be copied and little adjust to circumstances
        print('*'*10)
        function()
    return wrapFunc
@myDecorator    #actually a decorator
def Hello(): print("Hello.")
def Bye(): print('Goodbye.')
@myDecorator                                        #output: **********
def Silence(): print('"Silence upon leaving."')     #output: Hello.
Hello()                                             #output: Goodbye.
Bye()                                               #output: **********
Silence()                                           #output: "Silence upon leaving."
###
###
user1={'name': 'Sorna', 'valid': 'True'}
def authenticated(function):
    def wrapper(*args, **kwargs):
        '''args is passing a dictionary as an argument, and [0] as a first argument
        in our case user1(dictionary). Then we just check the key 'valid'.'''
        if args[0]['valid']: return function(*args, **kwargs)
    return wrapper
@authenticated
def messageFriends(user): print('message has been sent')
messageFriends(user1)       #output: message has been sent


#Error Handling
while True:                                         #loop till else break
    try:                                            #first try "try" instructions
        age=int(input('What is your age? '))        #If no exception occurs, the except clause is skipped and 
        10/age                                      #execution of the try statement is finished.
        if age > 150:
            raise EOFError('Hey, restart it.')      #raise is throw an exception if a condition occurs.
    except ValueError:
        print('Please, enter a number.')            #If an exception occurs during execution of the try clause,
    except (TypeError, ZeroDivisionError) as err:   #the rest of the clause is skipped
        print('please enter age higher than 0.')    #the except clause is executed
        print(err)     #output: division by zero
    except:
        print('Repeat, please, with a number.')     
    else:                                           #to define a block of code to be executed if no errors were raised
        print('Nothing went wrong.')
        break
    finally:                                        #finally runs regardless of error or correct input
        print('Ok, I am finally done.')
    print('Can you hear me?')                       #this is outside of the try's and exceptions


#generator functions
def generatorFunction(num): 
    for i in range(num): yield i*2    #yield pauses the function and comesback to it when we do something to it
g=generatorFunction(10)               #next() to comeback to a function, take next thing from it
print(next(g))      #output: 0
print(next(g))      #output: 2                  #w przeciwieństwie do list, generatory nie zapisują całych zbiorów w pamięci,
next(g)             #here, not printed '4'      #tylko ostatnio utworzone części
print(next(g))      #output: 6
print(next(g))      #output: 8
print(next(g))      #output: 10
print(next(g))      #output: 12
next(g)             #here, not printed 14
print(next(g))      #output: 16
print(next(g))      #output: 18
#własny generator loop
def specialFor(iterable):
    iterator=iter(iterable)
    while True:
        try: iterator*5
        next(iterator)
    except StopIteration: break
class MyGen:
    current=0
    def __init__(self,first,last): self.first,self.last,MyGen.current=[first,last,self.first]
    #MyGen.current allows use to use the current number as the starting point for the iteration
    def __iter__(self): return self
    def __next__(self):
        if MyGen.current<self.last:
            num=MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
gen=MyGen(1,100)
for i in gen: print(i)


#debugging
#1.debugging    2.linting    3.ide/editor    4.read erros       #output: t = 4*5
import pdb  #library for debugging                              #output:(pdb) a
def add(num1,num2):                                             #output: num1 = 4
    pdb.set_trace()                                             #output: num2 = 5
    t= 4*5                                                      #output:(pdb) num2 = 'sadas'
    return num1+num2                                            #output:(pdb) next
add(4,'sadas')                                                  #output: etc.......


#Regex
import re   #to import RegEx (regular expressions)
string,regPattern,regPat2=['search this inside of this text please!',re.compile('this'),re.compile('search this inside of this text please!')]
regSearch, regPat3=[re.search('this', string), re.compile(r"([a-zA-Z]).([a])")]
print('search' in string)                 #output: True
print(regSearch.span())                   #output: (17, 21)
print(regPattern.search(string).group())  #output: this
print(regPattern.findall(string))         #output: ['this', 'this']
print(regPat2.fullmatch(string))          #output: <re.Match object; span=(0, 39), match='search this inside of this text please!'>
print(regPat2.match(string))              #output: <re.Match object; span=(0, 39), match='search this inside of this text please!'>
print(regPat3.search(string).group())     #output: sea
print(regPat3.findall(string))            #output: [('s', 'a'), ('l', 'a')]
print(regPat3.fullmatch(string))          #output: None
print(regPat3.match(string))              #output: <re.Match object; span=(0, 3), match='sea'>
print(re.compile(r'[A-Za-z0-9$%#@]{8,}').fullmatch('2381dj@js9sAA'))    #<re.Match object; span=(0, 13), match='2381dj@js9sAA'>


#File Handling
firstHosts=open('Desktop\Linux_101.txt')   #to open a file, tho in this way, you will need to close it later
hostFileContents=firstHosts.read(3)        #reads what is in the file, by default it read whole file, here first 3 characters
print(hostFileContents)                    #prints what was read
firstHosts.close()                         #to close opened file
with open('/etc/hosts') as hosts:                   #use 'with' to automatically close the file after finishing or interrupting
    print('File closed? {}'.format(hosts.closed))   #output: File closed? False
    print(hosts.read())                             #output: 127.0.0.1 localhost
print('Finished reading a file.')                   #output: Finished reading a file.
print('File closed? {}'.format(hosts.closed))       #output: File closed? True
with open('file.txt', 'w') as theFile:                      #to open a file to write to it
    print(theFile.mode)       #to check the current mode    #output: w
    theFile.write('This is line one')                       #to write to a file
    theFile.write('This is line two')
    theFile.write('Finally, last line of the file')
with open('file.txt', 'rt') as theFile:    #file mode 'r' - read        #output: This is line one
    for line in theFile:       #to read lines one by one                #output: This is line two
        print(line.rstrip())   #to remove carriage return and newlines  #output: Finally, last line of the file.


#File Modes
'r' #open for reading (by default)
'w' #open for writing, truncating the file first
'x' #create a new file and open it for writing
'a' #open for writing, appending to the end of the file if it exists
'b' #binary mode
't' #text mode (by default)
'+' #open a disk file for updating (reading and writing)


#exercies
if __name__=='__main__':                                    #to print ints from 1 through n as a string without spaces
    n=int(input())                                          #input: 12
    print("".join(list(str(x) for x in range(1, n + 1))))   #output: 123456789101112
###################################################
my_pets=['sisi','bibi','titi','carla']  #to capitalize all of the names and print the list
def capitalize(string): return string.upper()
print(list(map(capitalize, my_pets)))   #output: ['SISI', 'BIBI', 'TITI', 'CARLA']
###################################################
def oddOrEven(number):
    if number % 2 == 0: return 'Even'
    else: return 'odd'
def isOdd(number):
    if number % 2 == 0: return False
    else: return True
###################################################
def getName(): #2
    name=input('What is your name? ') #3
    return name #4
def sayName(name): #6
    print('Your name is {}.'.format(name)) #7
def getAndSayName(): #0
    name = getName() #1
    sayName(name) #5
getAndSayName() #output: Yourname is <inserted name>.


