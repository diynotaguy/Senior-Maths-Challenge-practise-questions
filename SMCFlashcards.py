import random
import math
import json

#----------------------------------------------------------------------------------------------------#

questions = 0
global score
score = 0

#----------------------------------------------------------------------------------------------------#

def valid_int():
    """ Asks for user input until it is a valid integer. Returns input when valid"""
    inpt = input()
    valid = False
    while valid == False:
        valid = True
        try:
            assert str(int(inpt)) == inpt
        except:
            valid = False
            inpt = input(print('Please enter a valid integer: '))

    return inpt

#----------------------------------------------------------------------------------------------------#
        
def pythag_triples_test(pythag_triples, enable_multipliers, multipliers):
    set = random.randint(0,len(pythag_triples)-1)
    sides = [0,1,2]
    removed_side = random.randint(0, 2)
    sides.remove(removed_side)

    multiplier = 1
    if enable_multipliers:
        multiplier = multipliers[random.randint(0, len(multipliers)-1)]

    given_side_1 = pythag_triples[set][sides[0]]*multiplier
    given_side_2 = pythag_triples[set][sides[1]]*multiplier
    ans = pythag_triples[set][removed_side] * multiplier
    reward = True

    user_ans = int(input(f'Complete the pythagorean triple:\n{given_side_1}, {given_side_2}, '))
    while user_ans != ans:
        print('Incorrect, try again.\n')
        if multiplier != 1:
            print('HINT: It\'s a pythagorean triple that\'s been multiplied by a constant')
        user_ans = int(input(f'Complete the pythagorean triple:\n{given_side_1}, {given_side_2}, '))
        reward = False

    print('Correct!\n\n')
    if reward:
        global score
        score += 1

#----------------------------------------------------------------------------------------------------#

squares = []
for i in range (squares_start, squares_end + 1, 1):
    squares.append([i, 0])
    squares[i-squares_start][1] = (i**2)

def squares_test(squares):
    type = random.randint(0,1)
    square = random.randint(0,len(squares)-1)

    print(squares)
    print(f'squares[{square}][{type}]')

    if type == 0:
        user_ans = int(input(f'What is {squares[square][type]} squared?\n'))
    else:
        user_ans = int(input(f'What is the square root of {squares[square][type]}?\n'))

    attempts = 1
    while user_ans != squares[square][1-type]:
        print('Incorrect. Try again')
        if type == 0:
                user_ans = int(input(print(f'What is {squares[square][type]} squared?\n')))
        else:
            user_ans = int(input(f'What is the square root of {squares[square][type]}?\n'))
        attempts += 1
    print('Correct!\n\n')
    if attempts == 1:
        global score
        score += 1

#----------------------------------------------------------------------------------------------------#    

cubes = []
for i in range (cubes_start, cubes_end + 1, 1):
    cubes.append([i, 0])
    cubes[i-cubes_start][1] = i**3

def cubes_test(cubes):
    type = random.randint(0, 1)
    cube = random.randint(0, len(cubes)-1)

    print(f'cubes[{cube}][{type}]')

    x = cubes[cube][type]
    if type == 0:
        type1_input = input(f'What is {x} cubed?\n')
        user_ans = int(type1_input)
    else:
        type2_input = input(f'What is the cube root of {x}?\n')
        user_ans = int(type2_input)
        #user_ans = int(input(f'What is the cube root of {cubes[cube][type]}?\n'))

    attempts = 1
    while user_ans != cubes[cube][1-type]:
        print('Incorrect. Try again')
        if type == 0:
                user_ans = int(input(print(f'What is {cubes[cube][type]} cubed?\n')))
        else:
            user_ans = int(input(f'What is the cube root of {cubes[cube][type]}?\n'))
        attempts += 1
    print('Correct!\n\n')
    if attempts == 1:
        global score
        score += 1

#----------------------------------------------------------------------------------------------------#

def prime_fact_test(prime_fact):
    incorrect = True
    attempt = 1
    while incorrect:
        check_list = prime_fact[1:]
        print(f'check_list:\n{check_list}')

        user_ans = check_list[0]
        while user_ans in check_list:
            check_list.remove(user_ans)
            user_ans = int(input(f'Enter prime factors of {prime_fact[0]}. Enter 0 when finished.\n'))

        if len(check_list) == 0 and user_ans == 0:
            print('Well done, you answered perfectly!\n\n')
            if attempt == 1:
                global score
                score += 1
            incorrect = False
        elif len(check_list) == 0 and user_ans != 0:
            print('You have already listed all of the prime factors.')
            incorrect = False
        elif user_ans != 0:
            print(f'{user_ans} is not a factor or {prime_fact[0]}. Please try again.')
            attempt += 1
        else:
            print(f'There are still more factors of {prime_fact[0]} to list. Please try again.')
            attempt += 1
    
#----------------------------------------------------------------------------------------------------#

def divis_test(divisibility_test_nums):
    rand_num = random.randint(1, 5000)
    for num in divisibility_test_nums:
        ans = rand_num/num
        user_ans = input(f'Is {rand_num} divisible by {num}? y/n\n')
        if (user_ans == 'y' and ans == int(ans)) or (user_ans == 'n' and ans != int(ans)):
            print('Correct!\n')
        elif user_ans == 'y' and ans != int(ans):
            if ans - math.floor(ans) > math.ceil(ans) - ans:
                closest_multiple = math.ceil(ans)
            else:
                closest_multiple = math.floor(ans)

            print(f'Incorrect. The closest number to {rand_num} divisible by {num} is {closest_multiple}.')
        else:
            print(f'{rand_num} / {num} = {ans}')
    print()

#----------------------------------------------------------------------------------------------------#

def setup():
    print('Welcome to the Senior Maths Challenge (SMC) memorisation programme! You will be asked short answer maths questions to help you remember things that will be useful to know during the SMC or similar challenges. Have fun! :D')
    print('\n-----------------------------------------------------------------------------------------------\n')

    print("""What would you like to do?
    1) Start questions
    
    """)
    
    if (input('Would you like to change the settings? (y/n)')).lower() == 'y':
        change_settings()

#----------------------------------------------------------------------------------------------------#

from settings_funcs import *
setup()
from settings import *
running = True
while running:

    test_select = random.randint(0, 100)

    lower_bound = 0
    upper_bound = 0
    for test in chance_weighting:
        weight = test[1]
        upper_bound += weight
        if test_select <= weight and test_select > lower_bound:
            test[0]
        lower_bound = upper_bound

    questions += 1

    print('NEW TEST')

    if input('Would you like to do another test? y/n') == 'n':
        running = False

print(f'Your score was {score/questions}')