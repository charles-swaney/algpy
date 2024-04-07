from typing import Dict, Any, Union, List
from utils import dict_utils


class CayleyTable():
    """
    A Cayley table corresponding to a finite group (G,*) with n elements is an n by n table
    whose entry (i,j) is the value i * j. Nearly every property of a group can be understood
    through its Cayley table representation hence most useful group-theoretic computations
    are implemented here.

    This has an additional benefit of being easily extended to the theory of finite rings
    and fields, because (R,+) is an abelian group for any ring R, and (F,*) is an abelian
    group for any field F.

    Arguments:
        - table (Dict[Any, Dict[Any, Any]]): Cayley table representing the group operation

    Outputs:
        - Cayley table corresponding to the input dictionary
    
    Methods:
        - is_group
        - get_identity
    """
    def __init__(self, table: Dict[Any, Dict[Any, Any]]) -> None:
        
        self.elements = list(table.keys())
        self.table = table
        self.order = len(self.elements)

        if any(element == "" or element is None for element in self.elements):
            raise TypeError('Group elements cannot be the empty string or None.')
        
        # Prevent initialization of any Cayley Table that does not correspond to a valid group.
        if not self.is_group():
            raise ValueError('Input table does not correspond to a valid group.')

    def order(self) -> int:
        return self.order
    
    def elements(self) -> List[any]:
        return self.elements
    
    def table(self) -> Dict[Any, Dict[Any, Any]]:
        return self.table

    def is_group(self) -> bool:
        """
        Check the four group axioms to determine if the input table corresponds to a group:
            - closure under the operation
            - existence of identity element
            - existence of inverses
            - associativity of binary operation
        """
        return (self._is_closed()
                and self.get_identity() is not None
                and self._has_inverses()
                and self._is_associative())

    def _is_closed(self) -> bool:
        # G must be closed under the binary operation *.

        for element in self.elements:
            if not all(self.table[element][x] in self.elements for x in self.elements):
                return False
        return True
    
    def _has_inverses(self) -> bool:
        # Every element must have a unique inverse.
        return (all(self.get_inverse(element) is not None for element in self.elements)
                and all(not isinstance(self.get_inverse(element), list)
                        for element in self.elements))
    
    def _is_associative(self) -> bool:
        """
        The group operation must be associative, i.e. (a * b) * c = a * (b * c) for all a, b, c.
        Note that there is no algorithm which in general is better than O(n^3) because it is
        possible for a group to be associative except for a single triple (a, b, c).
        """

        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    ab = self.table[a][b]
                    bc = self.table[b][c]
                    if self.table[ab][c] != self.table[a][bc]:
                        return False
        return True
    
    def get_identity(self) -> Any:
        """
        Given a table containing the combination under a binary operation of every pair of elements,
        return the identity element, if there is one. Works for any finite algebraic structure.

        For groups, rings, and fields, it suffices to check if an element is the left identity,
        since such elements must also be right identities. For unital magmas, the identity element
        is defined to be two-sided.

        Arguments:
            - table: Cayley table representing the group operation
        Outputs:
            - The identity element
        """
        identities = []
        for element in self.table:
            if all(self.table[element][x] == x for x in self.table):
                identities.append(element)
        if len(identities) == 1:
            return identities.pop()
        elif len(identities) > 1:
            raise ValueError("Identity element is not unique.")
        return None

    def get_inverse(self, element: Any) -> Any:
        """
        Note: Can still find the 'inverse' provided there is an identity, even if the input table
        does not represent a group.
        Arguments:
            - table: Cayley table representing the group operation
            - element: the element to find the inverse of
        Outputs:
            - The inverse of element
        """
        if element not in self.elements:
            raise KeyError(f'{element} is not an element of the group.')
        inverses = []
        identity = self.get_identity()
        for x in self.elements:
            if self.table[element][x] == identity and self.table[x][element] == identity:
                inverses.append(x)
        if len(inverses) == 1:
            return inverses.pop()
        else:
            return None
        
    def is_abelian(self) -> bool:
        # Returns true if the table represents an abelian group, and false otherwise.
        for i in range(len(self.elements)):
            for j in range(i + 1, len(self.elements)):
                x, y = self.elements[i], self.elements[j]
                if self.table[x][y] != self.table[y][x]:
                    return False
        return True

    def get_order_of_element(self, element: Any) -> Union[int, float]:
        '''
        Return the order of element. This is defined to be the least integer m such that
        element^m = e, and infinity otherwise. By Lagrange's Theorem, the order of any element
        is at most the size of the group.
        '''
        if element not in self.elements:
            raise ValueError('Invalid input: element not in group.')
        if element == self.get_identity():
            return 1
        
        count = 1
        current_power = element
        while count < self.order + 1:
            count += 1
            current_power = self.table[current_power][element]
            if current_power == self.get_identity():
                return count
        return float('inf')
    
    def get_elements_of_order(self, order: int) -> List[Any]:
        # Return a list containing all elements of order order.
        return set([element for element in self.elements
                    if self.get_order_of_element(element) == order])
    
    def is_subgroup(self, subset: List[Any]) -> bool:
        """
        Returns True if the subgroup formed from the elements of subset is a group, else False.
        """
        potential_subgroup = CayleyTable(dict_utils.restricted(subset, self.table))
        return potential_subgroup.is_group()
