course = "Python course for beginners✅"

is_present = "Python" in course
print(is_present)

#Guess game
secret_number = 20
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:

    guess = input("Guess the number: ")
    guess_count+=1
    if guess == secret_number:
        print("Correct, you won!")
        break
    else: print(f"{guess_limit - guess_count} guesses left!")

else: print("Guess limit reached, Game over!")