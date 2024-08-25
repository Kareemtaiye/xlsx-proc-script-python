import modules, random
from modules import unique

numbers = [5,2, 5, 2, 2]
numbers_max = [3, 5, 6, 100, 3, 2, 9, 2]
dupl_list = [1, 2, 4, 3, 2, 5, 5, 1, 4]

for number in numbers:
    print("x" * number)

maximum_number = modules.find_max(numbers_max)
unique_list = modules.unique(dupl_list)
print(maximum_number, unique_list)

def dice_roll():
    first_die = random.randint(1, 6)
    sec_die = random.randint(1, 6)
    print((first_die, sec_die))

dice_roll()

from pathlib import  Path
path = Path()
for file in path.glob("*"):
    print(file)