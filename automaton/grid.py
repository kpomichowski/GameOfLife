
import numpy as np
import numpy.typing as npt
from automaton.states import CellState
from automaton.neighborhood.moore import MooreNeighborhood

class Grid:

    _cell_state = CellState
    _neighborhood = MooreNeighborhood

    def __init__(self, m: int, seed: int) -> None:
        self.width = m
        self.height = m
        self.seed = seed
        self.grid = None

    def initialize_grid(self) -> npt.NDArray[np.int8]:
        if self.grid is None:
            self.grid = np.random.choice([
                self._cell_state.ALIVE,
                self._cell_state.DEAD
            ], size=(self.width, self.height))

            return self.grid
        
        raise ValueError('Grid has been already initialized.')    

    def get_cell_state(self, x: int, y: int) -> int:
        return self.grid[x, y]

    def set_cell_state(self, x: int, y: int, state: int) -> None: 
        self.grid[x, y] = state

    def count_state_of_neighbors(self, x: int, y: int, state: int) -> int:

        neighbors = self._neighborhood.get_neighborhood(x, y)
        state_count = 0

        for dx, dy in neighbors:
            if 0 <= dx < self.grid.shape[0] and 0 <= dy < self.grid.shape[1]:
                if self.grid[dx, dy] == state:
                    state_count += 1

        return state_count

    @property
    def grid_states(self) -> npt.NDArray[np.int8]:
        return self.grid

    @grid_states.setter
    def grid_states(self, grid) -> None:
        self.grid = grid