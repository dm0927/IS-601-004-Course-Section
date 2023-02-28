from MyCalc import MyCalc

calc = MyCalc()

def test_add():

    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether addition is perfect between two numbers
    '''

    check = calc.add(2,2)
    assert check == 4

def test_ans_add():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether addition is perfect between ans and numbers
    '''
    check = calc.add("ans",2)
    assert check == 6

def number_sub_number():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether subtraction is perfect between two numbers
    '''
    check = calc.sub(6,4)
    assert check == 2

def ans_sum_number():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether subtraction is perfect between ans and numbers
    '''
    check = calc.sub("ans",4)
    assert check == -2

def number_mult_number():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether multiplication is perfect between two numbers
    '''
    check = calc.mul(5,5)
    assert check == 25

def ans_mult_number():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether multiplication is perfect between ans and numbers
    '''
    check = calc.mul("ans",4)
    assert check == 100

def number_div_number():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether division is perfect between two numbers
    '''
    check = calc.div(5,5)
    assert check == 1

def ans_div_number():
    '''
    # UCID - dm767
    # Date - Feb 27
    # Explanation - To check whether division is perfect between ans and numbers
    '''
    check = calc.div("ans",4)
    assert check == 0.25

test_add()
test_ans_add()
number_sub_number()
ans_sum_number()
number_mult_number()
ans_mult_number()
number_div_number()
ans_div_number()