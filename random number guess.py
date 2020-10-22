from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

total_guesses = 5
guesses_left = total_guesses
# Start your game!

print("Guessing Game!")
print ()
print ("You get", total_guesses, "guesses")
print ()
print ("GOOD LUCK")
print ()

while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess != int:
        print ()
        print ("That doesn't seem right, try again...")
        print ()
    else:
        if guess == random_number:
            print ()
            print ("You win!")
            print ()
            break
        guesses_left -= 1
        print ()
        print ("Wrong...guess again!")
        print("Guesses left:", guesses_left, "/", total_guesses)
        print ()
        else:
            print ("YOU LOSE")
            print ()