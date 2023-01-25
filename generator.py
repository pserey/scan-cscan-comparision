# generates a file with 10000 different integers

import random

numbers = set()
while len(numbers) < 10000:
    numbers.add(random.randint(0, 1000000))

with open("requests.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")
