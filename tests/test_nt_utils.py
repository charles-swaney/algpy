import sys
import pytest
from pathlib import Path
from utils import nt

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

# Test is_prime

def test_is_prime_large_prime():
    assert (nt.is_prime(10000139) is True)


def test_is_prime_large_composite():
    assert (nt.is_prime(17 ** 9) is False)


def test_is_prime_negative():
    with pytest.raises(ValueError) as e:
        nt.is_prime(-17)
    assert str(e.value) == 'n must be a positive integer.'


def test_is_prime_float():
    with pytest.raises(ValueError) as e:
        nt.is_prime(6.17)
    assert str(e.value) == 'n must be a positive integer.'
