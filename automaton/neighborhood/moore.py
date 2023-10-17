import numpy as np
import numpy.typing as npt

class MooreNeighborhood:

    # North directions
    NORTH_WEST = (-1, -1)
    NORTH = (0, -1)
    NORTH_EAST = (1, -1)

    # West
    WEST = (-1, 0)

    # East direction
    EAST = (1, 0)

    # South directions
    SOUTH_WEST = (-1, 1)
    SOUTH = (0, 1)
    SOUTH_EAST = (1, 1)

    @staticmethod
    def get_neighborhood(center_x: int, center_y: int) -> npt.NDArray[np.int8]:
        directions = [
            MooreNeighborhood.NORTH_WEST, MooreNeighborhood.NORTH, MooreNeighborhood.NORTH_EAST,
            MooreNeighborhood.WEST, MooreNeighborhood.EAST,
            MooreNeighborhood.SOUTH_WEST, MooreNeighborhood.SOUTH, MooreNeighborhood.SOUTH_EAST
        ]

        moore_neighborhood = np.array([(center_x + dx, center_y + dy) for dx, dy in directions])

        return moore_neighborhood


