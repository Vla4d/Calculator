import sys
print ("Hello! This is my first serious program, not strictly)")
print ("Enter the first number: ")
a = (int(sys.stdin.readline()))
print ("Enter another number: ")
b = (int(sys.stdin.readline()))
Action = input ("Enter the action you want to perform: ")
if Action == "+" :
    print (int(a + b))
if Action == "-" :
    print (int(a - b))
if Action == "*" :
    print (a * b)
if Action == "/" :
    print (a / b )