import pytest
import sys
from pathlib import Path

from groups import group
from utils import cayley_utils

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

cayley_mod3 = {
    0: {0: 0, 1: 1, 2: 2},
    1: {0: 0, 1: 2, 2: 0},
    2: {0: 2, 1: 0, 2: 1}
}

cayley_d3 = {
    'e': {'e': 'e', 'r': 'r', 'r^2': 'r^2', 's': 's', 'rs': 'rs', 'r^2s': 'r^2s'},
    'r': {'e': 'r', 'r': 'r^2', 'r^2': 'e', 's': 'rs', 'rs': 's', 'r^2s': 'r^2s'},
    'r^2': {'e': 'r^2', 'r': 'e', 'r^2': 'r', 's': 'r^2s', 'rs': 'rs', 'r^2s': 's'},
    's': {'e': 's', 'r': 'r^2s', 'r^2': 'rs', 's': 'e', 'rs': 'r', 'r^2s': 'r^2'},
    'rs': {'e': 'rs', 'r': 's', 'r^2': 'r^2s', 's': 'r^2', 'rs': 'e', 'r^2s': 'r'},
    'r^2s': {'e': 'r^2s', 'r': 'rs', 'r^2': 's', 's': 'r', 'rs': 'r^2', 'r^2s': 'e'},
}

cayley_no_inverse = {
    0: {0: 0, 1: 1, 2: 1},
    1: {0: 1, 1: 2, 2: 0},
    2: {0: 2, 1: 0, 2: 1}
}

cayley_noninvertible = {
    0: {0: 0, 1: 1, 2: 2},
    1: {0: 0, 1: 2, 2: 0},
    2: {0: 2, 1: 1, 2: 1}
}

cayley_nonunique_inverse = {
    0: {0: 0, 1: 1, 2: 2},
    1: {0: 1, 1: 0, 2: 0},
    2: {0: 2, 1: 0, 2: 1}
}


def test_identity_mod3():
    assert cayley_utils.get_identity(cayley_mod3) == 0


def test_identity_d3():
    assert cayley_utils.get_identity(cayley_d3) == 'e'


def test_identity_nongroup():
    assert cayley_utils.get_identity(cayley_no_inverse) is None


def test_inverse_mod3():
    assert cayley_utils.get_inverse(cayley_mod3, 0) == 0
    assert cayley_utils.get_inverse(cayley_mod3, 1) == 2
    assert cayley_utils.get_inverse(cayley_mod3, 2) == 1


def test_inverse_d3():
    assert cayley_utils.get_inverse(cayley_d3, 'r^2') == 'r'
    assert cayley_utils.get_inverse(cayley_d3, 'r^2s') == 'r^2s'
    assert cayley_utils.get_inverse(cayley_d3, 's') == 's'


def test_noninvertible():
    assert cayley_utils.get_inverse(cayley_noninvertible, 2) is None


def test_nonunique_inverse():
    assert len(cayley_utils.get_inverse(cayley_nonunique_inverse, 1)) > 1
