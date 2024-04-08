from typing import Any, Dict, List
from group import Group
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from cayley_tables import cayley

class DihedralGroup(Group):
    """
    The Dihedral group of D_n of order n (sometimes also D_{2n}) is the group of symmetries of 
    the regular n-gon, and is a group of order 2n. There are n rotational symmetries and n
    reflection symmetries. If n is odd, then we reflect across the line from each vertex to
    the midpoint of the opposite side. If n is even, then we reflect across the axes of 
    symmetry connecting opposite vertices, or sides.

    Attributes:
        - n_vertices (int): the number of vertices
        - cayley_table (Dict[Any, Dict[Any, Any]]): 
            a nested dictionary representing the Cayley table of the elements of C_n. Does not
            need to be passed in as a parameter.

    Parameters:
        - n_vertices (int): the number of vertices, a positive integer

    Methods:
        - _generate_cayley_table: 
            generates the Cayley table for the cyclic group with n elements.
    """
    def __init__(self, n_vertices: int) -> None:
        if not isinstance(n_vertices, int):
            raise TypeError('n_elements must be an integer.')
        if n_vertices <= 0:
            raise ValueError('n_elements must be a positive integer.')

        self.n_vertices = n_vertices
        cayley_table = self._generate_cayley_table(n_vertices)
        super().__init__(input_table=cayley_table)

    def _generate_cayley_table(self, n_vertices: int) -> Dict[Any, Dict[Any, Any]]:
        # Generates an input table for the Cayley table of a dihedral group on n vertices.
        rotations, reflections, table = [], ['s^1'], {}
        for i in range(1, n_vertices):
            rotations.append(f'r^{i}')
            reflections.append(f'sr^{i}')
        elements = ['e'] + rotations + reflections
        # First fill in the table values when the first operation is a rotation
        table['e'] = {}
        for element in elements:
            table['e'][element] = element

        for rotation in rotations:
            table[rotation] = {}
            for element in elements:
                if element == 'e':
                    table[rotation][element] = rotation
                elif element in rotations:
                    exponent = (int(rotation[-1]) + int(element[-1])) % n_vertices
                    table[rotation][element] = 'r^' + str(exponent)
                elif element in reflections:
                    exponent = n_vertices - 1 - int(rotation[-1])
                    if exponent == 0:
                        table[rotation][element] = 's'
                    else:
                        table[rotation][element] = 'rs^' + str(exponent)


        for reflection in reflections:
            table[reflection] = {}
            for element in elements:
                if element == 'e':
                    table[reflection][element] = reflection
                elif element in rotations:
                    pass
                elif element in reflections:
                    pass
