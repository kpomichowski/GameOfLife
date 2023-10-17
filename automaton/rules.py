from automaton.states import CellState

class Rules:

    @staticmethod
    def apply_rule(number_of_neighbors: int, state: int) -> int:
        if state == CellState.ALIVE:
            if number_of_neighbors < 2 or number_of_neighbors > 3: # Underpopulation & Overpopulation
                return CellState.DEAD
            else:
                return CellState.ALIVE
        else:
            if number_of_neighbors == 3:
                return CellState.ALIVE # Survives
            else:
                return CellState.DEAD   