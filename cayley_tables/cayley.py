from typing import Dict, Any


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
        self.table = table
        self.elements = table.keys()

    def is_group(self) -> bool:
        """
        Check the four group axioms to determine if the input table corresponds to a group:
            - closure under the operation
            - existence of identity element
            - existence of inverses
            - associativity of binary operation
        """
        return (self.is_closed
                and self.get_identity() is not None
                and self.has_inverses()
                and self.is_associative())

    def is_closed(self) -> bool:
        # G must be closed under the binary operation *.

        for element in self.elements:
            if not all(self.table[element][x] in self.elements for x in self.elements):
                return False
        return True
    
    def has_inverses(self) -> bool:
        # Every element must have a unique inverse.
        return (all(self.get_inverse(element) is not None for element in self.elements) and
                all(not isinstance(self.get_inverse(element), list) for element in self.elements))
    
    def is_associative(self) -> bool:
        # The group operation must be associative, i.e. (a * b) * c = a * (b * c) for all a, b, c.
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    ab = self.table[a][b]
                    bc = self.table[b][c]
                    if self.table[ab][c] != self.table[a][bc]:
                        print(f'a = {a}, b={b}, c = {c}, ab={ab}, bc = {bc}, so \n (ab)c = {self.table[ab][c]}, but a(bc) = {self.table[a][bc]}')
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

    def get_inverse(self, element) -> Any:
        """
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
        if identity is None:
            raise ValueError("No identity element found.")
        for x in self.elements:
            if self.table[element][x] == identity and self.table[x][element] == identity:
                inverses.append(x)
        if len(inverses) == 1:
            return inverses.pop()
        elif len(inverses) > 1:
            raise ValueError('An element more than one inverse, please check Cayley table.')
        else:
            return None
