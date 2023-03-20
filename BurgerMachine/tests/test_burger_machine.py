import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(sum(machine.inprogress_burger_price),"1")
    print("Test Case 1 Passed")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    first_order.handle_pay(sum(first_order.inprogress_burger_price),"2.75")

    print("Test Case 2 Passed")
    return first_order

@pytest.fixture
def third_order(second_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    second_order.handle_bun("no bun")
    second_order.handle_patty("turkey")
    second_order.handle_patty("next")
    second_order.handle_toppings("cheese")
    second_order.handle_toppings("done")
    second_order.handle_pay(sum(second_order.inprogress_burger_price),"1.25")
    print("Test Case 3 Passed")
    return second_order

@pytest.fixture
def fourth_order(third_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    third_order.handle_bun("white burger bun")
    third_order.handle_patty("veggie")
    third_order.handle_patty("turkey")
    third_order.handle_patty("beef")
    third_order.handle_patty("next")
    third_order.handle_toppings("cheese")
    third_order.handle_toppings("done")
    third_order.handle_pay(sum(third_order.inprogress_burger_price),"4.25")
    print("Test Case 4 Passed")
    return third_order

@pytest.fixture
def fifth_order(fourth_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    fourth_order.handle_bun("lettuce wrap")
    fourth_order.handle_patty("turkey")
    fourth_order.handle_patty("next")
    fourth_order.handle_toppings("bbq")
    fourth_order.handle_toppings("cheese")
    fourth_order.handle_toppings("mayo")
    fourth_order.handle_toppings("done")
    fourth_order.handle_pay(sum(fourth_order.inprogress_burger_price),"3.25")
    print("Test Case 5 Passed")
    return fourth_order

@pytest.fixture
def sixth_order(fifth_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    fifth_order.handle_bun("lettuce wrap")
    fifth_order.handle_patty("turkey")
    fifth_order.handle_patty("next")
    fifth_order.handle_toppings("cheese")
    fifth_order.handle_toppings("cheese")
    fifth_order.handle_toppings("done")
    fifth_order.handle_pay(sum(fifth_order.inprogress_burger_price),"3.0")
    print("Test Case 6 Passed")
    return fifth_order

@pytest.fixture
def seventh_order(sixth_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    sixth_order.handle_bun("lettuce wrap")
    sixth_order.handle_patty("turkey")
    sixth_order.handle_patty("next")
    sixth_order.handle_toppings("cheese")
    sixth_order.handle_toppings("cheese")
    sixth_order.handle_toppings("done")
    sixth_order.handle_pay(sum(sixth_order.inprogress_burger_price),"3.0")
    print("Test Case 7 Passed")
    return sixth_order

@pytest.fixture
def eight_order(seventh_order):
    '''
        UCID - dm767
        Date - March 20, 2023
    '''
    seventh_order.handle_bun("lettuce wrap")
    seventh_order.handle_patty("turkey")
    seventh_order.handle_patty("next")
    seventh_order.handle_toppings("cheese")
    seventh_order.handle_toppings("cheese")
    seventh_order.handle_toppings("done")
    return seventh_order

def test_production_line(eight_order):
    eight_order.handle_pay(sum(eight_order.inprogress_burger_price),"3.0")
    print("Test Case 8 Passed")