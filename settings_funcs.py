from SMCFlashcards import *
#----------------------------------------------------------------------------------------------------#
    
def change_settings():
    setting_change = input("""
        What would you like to do?
        1) Change the question weightings
        2) Change the question settings
        3) Restore default settings (all settings)
        4) View 
        3) None (go back)
    """)
    if setting_change == 1:
        change_weightings()
    elif setting_change == 2:
        change_q_settings()
    else:
        setup()

#----------------------------------------------------------------------------------------------------#

global py
py = pythag_triples_test(pythag_triples, enable_multipliers, multipliers)
global sq
sq = squares_test(squares)
global cu
cu = cubes_test(cubes)
global pr
pr = prime_fact_test(prime_fact)
global div
div = divis_test(divisibility_test_nums)

global eq
eq = -1 #equal

def change_weightings():
    print('Each question type has a weighting - the higher the weighting, the more likely it is to come up as a question in your practise. The weightings must add to 100. Set a weighting to 0 if you don\'t want to be asked that type of question, or set it to \'eq\' if you want it to have the same weighting as any other question type with eq. eq will be automatically calculated based on the other weightings, and if using eq, the weightings you\'ve manually given numbers don\'t have to add to 100.')


    chance_weighting = [[py, eq], [sq, eq], [cu,eq], [pr, 0], [div, eq]]

    sum = 0
    eq_freq = 0
    for test in chance_weighting:
        weight = test[1]
        if weight == -1:
            eq_freq += 1
        else:
            sum += weight

    eq = (100 - sum) / eq_freq
    
#----------------------------------------------------------------------------------------------------#

def change_q_settings():

    options = [py_settings(), sq_settings(), cu_settings(), pr_settings(), div_settings(), change_settings()]

    print("""
        Select the question type you would like to change the settings for:
        1) Pythagorean triples
        2) Square numbers
        3) Cubed numbers
        4) Prime factors of a given number
        5) Divisible by certain numbers
        6) None (go back)
    """)

    valid_num = False
    while not valid_num:
        valid_num = True
        choice = valid_int()
        if choice < 1 or choice > 6:
            valid_num = False
            print('Please enter a number from the list above: ', end = '')
        
    options[choice - 1]

#----------------------------------------------------------------------------------------------------#

def py_settings():
    None

def sq_settings():
    None

def cu_settings():
    None

def pr_settings():
    None

def div_settings():
    None
#----------------------------------------------------------------------------------------------------#
