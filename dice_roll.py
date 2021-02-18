# dice rolling library, nigel griffin, febuary 18, 2021, 1:52pm

import random
import time

# d4 simulator
def roll_d4(num_roll): # num_roll is an argument
    rolls = 0
    the_sum = 0

while rolls < num_roll:
    result = random.randint(1, 4)
    print(f"homie u rolled a {result}.\n")
    rolls += 1
    sum += result
print(f"")

roll_d4(4)


