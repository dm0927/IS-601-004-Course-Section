from MyCalc import MyCalc
import pytest

calc = MyCalc()

def test_add():
    check = calc.add(2,2)
    assert check == 4

def test_ans_add():
    check = calc.add("ans",2)
    assert check == 6

def number_sub_number():
    check = calc.sub(6,4)
    assert check == 2

def ans_sum_number():
    check = calc.sub("ans",4)
    assert check == -2

def number_mult_number():
    check = calc.mul(5,5)
    assert check == 25

def ans_mult_number():
    check = calc.mul("ans",4)
    assert check == 100

def number_div_number():
    check = calc.div(5,5)
    assert check == 1

def ans_div_number():
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