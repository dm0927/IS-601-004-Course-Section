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


# def test_topping_step(machine):
#   machine.reset()
#   machine.handle_bun("no bun")
#   #skip handle_patty
#   try:
#     machine.handle_topping("lettuce")
#   except:
#     assert True
#     return
#   assert False

def test_case_one(machine):
    try:
        machine.reset()
        machine.handle_patty("veggie")
        assert False
    except InvalidStageException:
        print("Invalid Stage")
        assert True

def test_case_two(machine):
    try:
        machine.reset()
        machine.handle_patty("veggie")
        assert False
    except InvalidStageException:
        print("Invalid Stage")
        assert True

def test_case_two(machine):
    try:
        machine.reset()

        machine.handle_bun("no bun")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        machine.reset()

        machine.handle_bun("no bun")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        machine.reset()

        machine.handle_bun("no bun")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        machine.reset()

        assert True
    except OutOfStockException:
        print("Veggie Not avaiable")
        assert False

def test_case_three(machine):
    try:
        machine.reset()

        machine.handle_bun("no bun")
        machine.handle_patty("veggie")
        machine.handle_patty("next")
        machine.pick_toppings("cheese")
        machine.pick_toppings("cheese")
        machine.pick_toppings("cheese")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        assert True
    except OutOfStockException:
        print("Toppings Not avaiable")
        assert False

def test_case_four(machine):
    try:
        machine.reset()

        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("turkey")
        machine.handle_patty("beef")
        machine.handle_patty("next")
        machine.pick_toppings("cheese")
        machine.pick_toppings("cheese")
        machine.pick_toppings("cheese")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        assert True
    except:
        assert False

def test_case_five(machine):
    try:
        machine.reset()

        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("turkey")
        machine.handle_patty("beef")
        machine.handle_patty("next")
        machine.pick_toppings("bbq")
        machine.pick_toppings("mustard")
        machine.pick_toppings("ketchup")
        machine.handle_toppings("done")
        machine.handle_pay(3,"3")

        assert True
    except:
        assert False