import random
random.seed(1014)

while raw_input("Play a game of guess the number? (yes/no): ") == "yes":
    random_num = random.randrange(0, 100)
    current_guess = 0
    prev_guess = 1000
    while current_guess != random_num:
        current_guess = input("Enter a guess between 0 and 100: ")
        curr_diff = abs(random_num - current_guess)
        prev_diff = abs(random_num - prev_guess)

        if current_guess == random_num:
            print("Congratulations! You guessed correctly.")
            print "The number was", current_guess
        elif curr_diff < prev_diff:
            print("You're getting closer!")
        elif current_guess == prev_guess:
            print("You guessed the same thing last time!")
        else:
            print("That guess was a step in the wrong direction.")
        prev_guess = current_guess
