#Functions example :) 
input = raw_input("Enter Your name: ")

def say_hello(name):
    print 'Hello', name

say_hello(input)

input1 = raw_input("Age: ")
input1 = int(input1)

def test(age):
    print 'Age is: ', age

if input1<18:
    print "Underage"
    test(input1)

elif input1>=18:
    print "Legal Age"
    test(input1)
    
