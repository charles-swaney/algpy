import sys
import yaml
from pathlib import Path
from utils import dict_utils
from cayley_tables import cayley

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

with open('../config/valid_tables.yml', 'r') as f:
    valid_tables = yaml.safe_load(f)

cayley_d4 = cayley.CayleyTable(valid_tables['cayley_d4'])
cayley_mod3 = cayley.CayleyTable(valid_tables['cayley_mod3'])
cayley_mod4 = cayley.CayleyTable(valid_tables['cayley_mod4'])
cayley_klein4 = cayley.CayleyTable(valid_tables['cayley_klein4'])
cayley_s3 = cayley.CayleyTable(valid_tables['cayley_s3'])


def test_restricted_empty():
    assert (dict_utils.restricted([], cayley_d4) == {})


def test_restricted_whole_dict():
    assert (dict_utils.restricted([0, 1, 2, 3], cayley_mod4.table) == cayley_mod4.table)


def test_restricted_subset_d4():
    assert (dict_utils.restricted(['e', 'r', 's'], cayley_d4.table)
            == {'e': {'e': 'e', 'r': 'r', 's': 's'},
                'r': {'e': 'r', 'r': 'r^2', 's': 'sr^3'},
                's': {'e': 's', 'r': 'sr', 's': 'e'}})


def test_restricted_subgroup_d4():
    d4_subgroup = dict_utils.restricted(['e', 'r', 'r^2', 'r^3'], cayley_d4.table)
    assert (d4_subgroup
            == {'e': {'e': 'e', 'r': 'r', 'r^2': 'r^2', 'r^3': 'r^3'},
                'r': {'e': 'r', 'r': 'r^2', 'r^2': 'r^3', 'r^3': 'e'},
                'r^2': {'e': 'r^2', 'r': 'r^3', 'r^2': 'e', 'r^3': 'r'},
                'r^3': {'e': 'r^3', 'r': 'e', 'r^2': 'r', 'r^3': 'r^2'}})
    assert (cayley.CayleyTable(d4_subgroup).is_group() is True)
