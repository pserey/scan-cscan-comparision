# generates a file with 1000 different integers

import random

def generate(number_set):
    numbers = set()
    while len(numbers) < number_set:
        numbers.add(random.randint(0, number_set * 10))

    with open("requests.txt", "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")
