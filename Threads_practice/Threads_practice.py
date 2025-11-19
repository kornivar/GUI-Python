import threading
import random

rnd = random.Random()
my_drinks = ["coffee", "tea", "juice", "water", "soda", "fanta", "chocolate"]
taken_drinks = []
my_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"]

threads = []

def take_a_drink(name, drink, in_or_out):
    if in_or_out == 0:
        print(f"{name} entered the cafe.")

        if drink not in taken_drinks:
            taken_drinks.append(drink)
            print(f"{name} took a {drink} drink.")
        else:
            print(f"Sorry {name}, the {drink} drink is already taken.")

        print(f"{name} leaved the cafe.")
    else:
        print(f"{name} entered the cafe.")

        if drink not in taken_drinks:
            taken_drinks.append(drink)
            print(f"{name} took a {drink} drink.")
        else:
            print(f"Sorry {name}, the {drink} drink is already taken.")

        print(f"{name} stayed to have a good time")

for i in range(7):
    name = my_names[i]
    tmpTread = threading.Thread(target=take_a_drink, args=[name, rnd.choice(my_drinks), rnd.randint(0,1)])
    tmpTread.start()
    threads.append(tmpTread)


for i in range(7):
    threads[i].join()
