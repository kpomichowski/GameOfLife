import argparse

from automaton import goe
from visualize.anim import animate_automata


def main(seed: int, generations:int, grid_dim: int) -> None:
    print(f'Seed: {seed}, Generations: {generations}, Grid dimensions: {grid_dim}')
    goe_instance = goe.GameOfLifeCA(m=grid_dim, seed=seed, generations=generations)
    animate_automata(generator=goe_instance.run(), generations=generations, seed=seed)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--grid_dim", type=int, help="Dimension of the grid", required=True)
    parser.add_argument("--seed", type=int, help="Seed for random number generation", required=True)
    parser.add_argument("--generations", type=int, help="Number of generations", required=True)
    
    args = parser.parse_args()

    main(args.seed, args.generations, args.grid_dim)
