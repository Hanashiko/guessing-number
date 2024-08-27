from random import randint

min_numbers_range: int = 1
max_number_range: int = 9
secret_number: int = randint(min_numbers_range, max_number_range)

times: int = 0

while 1:
    guess_number: int = int(input(f"Write number ({min_numbers_range} to {max_number_range}): "))
    times += 1
    
    if guess_number == secret_number:
        print("You win!!!")
        print(f"You did it in {times} tried")
        break
    elif guess_number < secret_number:
        print("Try a higher number")
    else:
        print("Try a lower number")
    

    