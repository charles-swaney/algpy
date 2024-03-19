import numpy
from typing import List, Dict, Callable, Any


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
        operation (callable): the binary operation
        cayley_table (Dict[Dict[Any]]): a nested dictionary corresponding to the Cayley table
        corresponding to G. The value of cayley_table[element1][element2] is
        element1 * element 2.
    """
    def __init__(self, elements: List[Any],
                 operate: Callable,
                 cayley_table: Dict[Dict[Any]]) -> None:
        self.elements = elements
        self.operate = operate
        self.cayley_table = cayley_table

    def get_elements(self) -> List[Any]:
        return self.elements
    
    def get_identity(self) -> Any:
        pass
