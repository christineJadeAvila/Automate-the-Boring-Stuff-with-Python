# Blocks

# credentials
name = 'Mary'
password = 'swordfish'
# Flow Control = if else
# condition
if name == 'Mary':
    print('Hello, Mary!') #block of code
    # another block of condition
    if password == 'swordfish':
        print('Access granted!') #block of code
    else: 
        print('Wrong password!... try again.') #block of code


# else if
name = 'Carol'
age = 3000

if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo!')
elif age > 2000:
    print('You are a vampire.. hmmp!')
elif age > 100:
    print('You are not Alice, grandma')

# while loop
print('')
#spam = 0
#if spam < 5:
#    print('Hello, world')
#    spam += 1

spam = 0
while spam < 5:
    print('Hello, world')
    spam = spam + 1 # or spam += 1

# An annoying while loop
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you!')