import random
print("***************** NUMGUESS STARTS ****************")
print("Hi welcome to the Number guessing game..!")
print ("You got 7 chances to guess the number. Let's start the game")
number = random.randrange(100)
chances = 7
counter = 0
while counter < chances:

    counter += 1
    my_guess = int(input('Enter your Guess : '))

    if my_guess == number:
        print(f'The number is {number} and you found it right !! in the {counter} attempt')
        break

    elif counter >= chances and my_guess != number:
        print(f'Sorry, The number is {number} better luck next time')

    elif my_guess > number:
        print('Your guess is high ')

    elif my_guess < number:
        print('Your guess is less')

print("***************** NUMGUESS ENDS ****************")
