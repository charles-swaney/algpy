import numpy
from typing import List, Dict, Any, Union

import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from cayley_tables import cayley


class Group():
    """
    Represents a mathematical group. A group (G, *) consists of a set G along with a
    binary operation *, satisfying the following properties:
    - closure under *
    - there is an identity element
    - * is associative
    - existence of inverses

    Attributes:
        - input_table (Dict[Dict[Any]]): a nested dictionary corresponding to the Cayley table
        corresponding to G. The value of cayley_table[element1][element2] is
        element1 * element 2.
    """
    def __init__(self, input_table: Dict[Any, Dict[Any, Any]]=None, check_axioms=True) -> None:
        self.check_axioms = check_axioms
        self.cayley_table = cayley.CayleyTable(input_table, check_axioms=self.check_axioms)
        self.elements = self.cayley_table.elements

    def op(self, element_1: Any, element_2: Any) -> Any:
        if element_1 not in self.elements or element_2 not in self.elements:
            raise KeyError('Can only operate on elements of the group.')
        return self.cayley_table.table[element_1][element_2]

    def elements(self) -> List[Any]:
        return self.elements
    
    def order(self) -> int:
        return len(self.elements)
    
    def is_abelian(self) -> bool:
        return self.cayley_table.is_abelian()
    
    def get_identity(self) -> Any:
        return self.cayley_table.get_identity()
    
    def get_inverse(self, element: Any) -> Any:
        return self.cayley_table.get_inverse(element)
    
    def get_order_of_element(self, element: Any) -> Union[int, float]:
        return self.cayley_table.get_order_of_element(element)
    
    def get_elements_of_order(self, order: int) -> List[Any]:
        return self.cayley_table.get_elements_of_order(order)
