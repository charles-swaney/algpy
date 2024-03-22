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

cayley_d3 = cayley.CayleyTable(valid_tables['cayley_d3'])
cayley_mod3 = cayley.CayleyTable(valid_tables['cayley_mod3'])
cayley_mod4 = cayley.CayleyTable(valid_tables['cayley_mod4'])
cayley_klein4 = cayley.CayleyTable(valid_tables['cayley_klein4'])
cayley_s3 = cayley.CayleyTable(valid_tables['cayley_s3'])

cayley_nonunique_inverse = cayley.CayleyTable(invalid_tables['cayley_nonunique_inverse'])
cayley_noninvertible = cayley.CayleyTable(invalid_tables['cayley_noninvertible'])
cayley_no_inverse = cayley.CayleyTable(invalid_tables['cayley_no_inverse'])


def test_is_group_d3():
    assert (cayley_d3.is_group() is True)
    

def test_is_group_klein4():
    assert (cayley_klein4.is_group() is True)


def test_is_group_mod3():
    assert (cayley_mod3.is_group() is True)


def test_is_group_mod4():
    assert (cayley_mod4.is_group() is True)


def test_is_group_s3():
    assert (cayley_s3.is_group() is True)


def test_inverse_d3():
    assert (cayley_d3.get_inverse('r^2') == 'r')
    assert (cayley_d3.get_inverse('r^2s') == 'r^2s')
    assert (cayley_d3.get_inverse('s') == 's')


def test_inverse_mod3():
    assert (cayley_mod3.get_inverse(0) == 0)
    assert (cayley_mod3.get_inverse(1) == 2)
    assert (cayley_mod3.get_inverse(2) == 1)


def test_identity_klein4():
    assert (cayley_klein4.get_identity() == 'e')


def test_identity_s3():
    assert (cayley_s3.get_identity() == 'e')


def test_noninvertible():
    assert (cayley_noninvertible.get_identity() == 0)
    assert (cayley_noninvertible.get_inverse(2) is None)
    assert (cayley_noninvertible.is_group() is False)


def test_nonunique_inverse():
    assert (cayley_nonunique_inverse.get_identity() == 0)
    with pytest.raises(ValueError) as e:
        cayley_nonunique_inverse.get_inverse(1)
    str(e.value) == 'An element more than one inverse, please check Cayley table.'
    assert (cayley_noninvertible.is_group() is False)
