import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachine import STAGE
from BurgerMachine import Usable
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("veggie")
    machine.handle_patty("veggie")    
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(3,"3")
    return machine

@pytest.fixture
def second_order(machine, first_order):
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    # machine.handle_pay(3,"3")
    return machine

def test_production_line(second_order):
    assert second_order is not None

def test_case_one(machine):
    if machine.currently_selecting != STAGE.Bun:
        assert False
    else:
        assert True

def test_case_two(machine):
    for f in machine.patties:
        if f.name.lower() == "veggie":
            assert f.in_stock()

def test_case_three(machine):
    for f in machine.toppings:
        if f.name.lower() == "cheese":
            assert f.in_stock()

def test_case_four(machine):
    if machine.remaining_patties <= 0:
        assert False
    else:
        assert True

def test_case_five(machine):
    if machine.remaining_toppings <= 0:
        assert False
    else:
        assert True

def test_case_six(machine):
    machine.inprogress_burger_price = [1, 1, 1, 1, .25, .25]
    cost = machine.calculate_cost()
    assert cost == 4.50

    machine.inprogress_burger_price = [1, 1, .25, .25]
    cost = machine.calculate_cost()
    assert cost == 2.50

    machine.inprogress_burger_price = [0, 1, .25, .25]
    cost = machine.calculate_cost()
    assert cost == 1.50

def test_case_seven(machine):
    machine.currently_selecting = STAGE.Pay
    machine.inprogress_burger_price = [1, 1, 1, 1, .25, .25]
    machine.handle_pay(sum(machine.inprogress_burger_price), '4.5')

    machine.currently_selecting = STAGE.Pay
    machine.inprogress_burger_price = [1, 1, .25, .25]
    machine.handle_pay(sum(machine.inprogress_burger_price), '2.5')

    machine.currently_selecting = STAGE.Pay
    machine.inprogress_burger_price = [0, 1, .25, .25]
    machine.handle_pay(sum(machine.inprogress_burger_price), '1.5')

    assert machine.total_sales == 8.50

def test_case_eight(machine):
    machine.currently_selecting = STAGE.Pay
    machine.inprogress_burger_price = [1, 1, 1, 1, .25, .25]
    machine.handle_pay(sum(machine.inprogress_burger_price), '4.5')

    machine.currently_selecting = STAGE.Pay
    machine.inprogress_burger_price = [1, 1, .25, .25]
    machine.handle_pay(sum(machine.inprogress_burger_price), '2.5')

    machine.currently_selecting = STAGE.Pay
    machine.inprogress_burger_price = [0, 1, .25, .25]
    machine.handle_pay(sum(machine.inprogress_burger_price), '1.5')

    assert machine.total_burgers == 3