secret_number = 7
guess_count= 0
while guess_count < 3:
    guess = int(input("guess the number"))

    if secret_number == guess :
       print(f"i'm win at {guess_count+1} guess")
       break
    elif secret_number > guess:
        print("secreat number is greater than guess")
    elif secret_number < guess:
        print("secreat number is lesser than guess")

    guess_count += 1
    print("number of remaining guessess",3-guess_count)
else:
    print("I'm fail")


