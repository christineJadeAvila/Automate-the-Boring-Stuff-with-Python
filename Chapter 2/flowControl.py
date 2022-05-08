# A program that decides for you when you should go out 
# when it is raining and checks if you have umbrella. 

print('Is it raining? ')
rainCheck = input()

if rainCheck == 'Yes' or rainCheck == 'yes' or rainCheck == 'YES':
    print('Do you have an umbrella? Yes or No?')
    haveUmbrella = input()
    #if not or if have an umbrella
    if haveUmbrella == 'Yes':
        print('Go outside!')
    elif haveUmbrella == 'No':
        print('wait a while')
        print()
        print('Please answer this question after 7 seconds.')
        print('Is it still raining?')
        stillRaining = input()
        if stillRaining == 'Yes':
            print('You got to wait again! and only go outside if the rain stops.')
        else: 
            print('Go outside!')
    else: 
        print('What are you talking about?')
else:
    print('Go outside!')