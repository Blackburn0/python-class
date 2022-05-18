our_fav_number = 10

user_guess = input("Enter your guess: ")
# type_of_user_guess = type(user_guess)

print(type(user_guess))

user_guess = int(user_guess)

if user_guess == our_fav_number:
    print("You got the correct number \U0001F917, congrats: " + str(our_fav_number))

elif user_guess < our_fav_number:
        print("The number you entered is too low, try a number higher")

elif user_guess > our_fav_number:
    print("The number you entered is too high, try a lower number")
