# A program that says hello and asks for a name

print('Hello, World!')
print('What is your name?') # ask for the name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ') # get the length of the name
print(len(myName))
print('How old are you? ') # ask for the age
myAge = input()
print('Your age next year will be ' + str(int(myAge) + 1))

if int(myAge) > 20:
    print('You are getting old, ' + myName)
else:
    print('Live a happy life!!!')

print(str(2222))
print(str(333))
print(int('333'))
print(str('3'))

