# Example for float and integer operations
# Addition
a = 5
b = 2.5
c = a + b  # float + integer = float
d = b + a  # integer + float = float
print(c)  # Output: 7.5
print(d)  # Output: 7.5

# Subtraction
e = 7.5
f = 3
g = e - f  # float - integer = float
h = f - e  # integer - float = float
print(g)  # Output: 4.5
print(h)  # Output: -4.5

# Multiplication
i = 2
j = 3.5
k = i * j  # integer * float = float
l = j * i  # float * integer = float
print(k)  # Output: 7.0
print(l)  # Output: 7.0

# Division
m = 10
n = 3
o = m / n  # integer / integer = float
p = n / m  # integer / integer = float
q = m / j  # integer / float = float
r = j / m  # float / integer = float
print(o)  # Output: 3.3333333333333335
print(p)  # Output: 0.3
print(q)  # Output: 2.857142857142857
print(r)  # Output: 0.35

############################################################

# Example code for string operations
# Concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + s2  # concatenation using + operator
print(s3)  # Output: HelloWorld

# Repetition
s4 = "Ha"
s5 = s4 * 5  # repetition using * operator
print(s5)  # Output: HaHaHaHaHa

# Slicing
s6 = "Hello World"
s7 = s6[0:5]  # slicing from index 0 to 4
s8 = s6[6:]  # slicing from index 6 to end
print(s7)  # Output: Hello
print(s8)  # Output: World

# Length
s9 = "Python"
length = len(s9)  # length of string using len() function
print(length)  # Output: 6

# Upper and Lower case
s10 = "Hello World"
s11 = s10.upper()  # convert to upper case
s12 = s10.lower()  # convert to lower case
print(s11)  # Output: HELLO WORLD
print(s12)  # Output: hello world

# Example code for anagrams
# Anagrams are words or phrases formed by rearranging the letters of a different word or phrase
# Here is an example code to check if two strings are anagrams of each other

def is_anagram(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Check if the length of both strings are equal
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare them
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Test the function
print(is_anagram("Listen", "Silent"))  # Output: True
print(is_anagram("Eleven plus two", "Twelve plus one"))  # Output: True
print(is_anagram("Hello", "World"))  # Output: False