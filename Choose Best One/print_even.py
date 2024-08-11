#Runs 100 iterations 
def print_even_numbers_100():
    number = 2
    while number <= 100:
        if number % 2 == 0:
            print(number)
        number += 1

print_even_numbers_100()


#The Below one is better than above  takes  only 50 iterations by incrementing the number by 2 each time.
def print_even_numbers_50():
    number = 2
    while number <= 100:
        print(number)
        number += 2

print_even_numbers_50()
