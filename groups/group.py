import numpy
from typing import List, Dict, Any
from utils import cayley_utils


class Group():
    """
    Represents a mathematical group. A group (G, *) consists of a set G along with a
    binary operation *, satisfying the following properties:
    - closure under *
    - there is an identity element
    - * is associative
    - existence of inverses

    Attributes:
        elements (List[Any]): the elements in G
        cayley_table (Dict[Dict[Any]]): a nested dictionary corresponding to the Cayley table
        corresponding to G. The value of cayley_table[element1][element2] is
        element1 * element 2.
    """
    def __init__(self, elements: List[Any],
                 cayley_table: Dict[Any, Dict[Any, Any]]) -> None:
        self.elements = elements
        self.cayley_table = cayley_table

    def get_elements(self) -> List[Any]:
        return self.elements
    
    def get_identity(self) -> Any:
        return cayley_utils.get_identity(self.cayley_table)
    
    def get_order(self) -> int:
        return len(self.elements)
