# Buiding a guessing game in Python

secret_word = "manchester"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess!= secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE! TRY AGAIN...")

else:
    print("Good Job, YOU WIN!!!")
