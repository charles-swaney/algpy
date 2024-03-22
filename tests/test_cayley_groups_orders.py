import yaml
import sys
import pytest
from pathlib import Path
from cayley_tables import cayley

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))


with open('../config/valid_tables.yml', 'r') as f:
    valid_tables = yaml.safe_load(f)

with open('../config/invalid_tables.yml', 'r') as f:
    invalid_tables = yaml.safe_load(f)

cayley_d4 = cayley.CayleyTable(valid_tables['cayley_d4'])
cayley_mod3 = cayley.CayleyTable(valid_tables['cayley_mod3'])
cayley_mod4 = cayley.CayleyTable(valid_tables['cayley_mod4'])
cayley_klein4 = cayley.CayleyTable(valid_tables['cayley_klein4'])
cayley_s3 = cayley.CayleyTable(valid_tables['cayley_s3'])

# Testing group order


def test_group_order_d4():
    assert (cayley_d4.order == 8)


def test_group_order_s3():
    assert (cayley_s3.order == 6)

# Testing is_abelian (move to another testing script later)


def test_is_abelian_mod4():
    assert (cayley_mod4.is_abelian() is True)

    
def test_is_abelian_s3():
    assert (cayley_s3.is_abelian() is False)


def test_is_abelian_d4():
    assert (cayley_d4.is_abelian() is False)


def test_is_abelian_klein4():
    assert (cayley_klein4.is_abelian() is True)

# Testing orders of elements
    

def test_order_e_d4():
    assert (cayley_d4.order_of_element('e') == 1)


def test_order_sr2_d4():
    assert (cayley_d4.order_of_element('sr^2') == 2)


def test_order_rotations_d4():
    assert (cayley_d4.order_of_element('r^3') == 4)
    assert (cayley_d4.order_of_element('r^3') == cayley_d4.order_of_element('r'))
    assert (cayley_d4.order_of_element('r^2') == 2)


def test_order_1_mod4():
    assert (cayley_mod4.order_of_element(1) == 4)


def test_order_q_s3():
    assert (cayley_s3.order_of_element('q') == 3)

# Testing get_elements_of_order
    

def test_elts_order_1_d4():
    assert (cayley_d4.get_elements_of_order(1) == {'e'})


def test_elts_order_2_d4():
    assert (cayley_d4.get_elements_of_order(2) == {'r^2', 's', 'sr', 'sr^2', 'sr^3'})


def test_elts_order_4_mod4():
    assert (cayley_mod4.get_elements_of_order(4) == {1, 3})


def test_elts_order_2_klein4():
    assert (cayley_klein4.get_elements_of_order(2) == {'a', 'b', 'c'})
