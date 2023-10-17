import numpy as np
import numpy.typing as npt

from automaton.rules import Rules
from automaton.grid import Grid

from itertools import product


class GameOfLifeCA:
    def __init__(self, m: int, seed: int, generations=10000) -> None:
        self.__grid = Grid(m, seed)
        self.__grid.initialize_grid()
        self.generations = generations
        self.__rules = Rules

    def run(self) -> None:

        for _ in range(self.generations):
            catersian_prod_coordinates = product(range(self.__grid.width), range(self.__grid.height))
            future_state_grid = np.copy(self.__grid.grid_states)
            yield future_state_grid
            for x, y in catersian_prod_coordinates:
                current_cell_state = self.__grid.get_cell_state(x, y)
                living_cells_count = self.__grid.count_state_of_neighbors(x, y, state=self.__grid._cell_state.ALIVE)
                future_state_cell = self.__rules.apply_rule(living_cells_count, state=current_cell_state)
                future_state_grid[x, y] = future_state_cell
            self.__grid.grid_states = future_state_grid

                