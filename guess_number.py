import random

number_to_guess = random.randint(1 ,100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100:"))
        if guess < number_to_guess:
            print('Too LOw!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print("congragulations YOu have made it")
            break
    except ValueError:
        print('please enter a valid number')
    























