# John Conway's Game of Life

The Game of Life, devised by mathematician John Conway, is a cellular automaton that simulates the evolution of simple organisms. It consists of a grid of cells, each of which can be in one of two states: alive or dead. The game progresses in discrete steps, following a set of rules based on the state of neighboring cells. Despite its simple rules, the Game of Life can produce complex and unpredictable patterns, making it a fascinating study in emergent behavior and a popular topic in computer science and mathematics.

Sources:
* [Game Of Life at Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life),
* [Conway's Game Of Life](https://pi.math.cornell.edu/~lipa/mec/lesson6.html).

# Table Of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Dependencies](#dependencies)
* [Examples](#examples)

# Installation

Before installation necessary dependencies to run this project, create Python virtual environment, in the terminal go the directory of the project:

`cd path/to/goe/project`

Then create the Virtual Environment:

`python -m venv [env]`

If you are using Anaconda or Mamba, issue following command:

`conda create -n [env]` or `mamba create -n [env]`

## Windows Case

In the case of using Windows, just activate the Virutal Environment using:

`[env]\Scripts\activate`

## Linux Case

In the case of standalone version of virtual environment using Python, you need to activate created environment:

`. /[env]/bin/activate` or `source [env]/bin/activate`

In the case of `conda` or `mamba`:

`conda activate [env]` or `mamba activate [env]`

`[env]` is the name of your created Virtual Environment.

When you notice that Your environment has been activated, then install necessary libraries and dependencies to run this cellular automata:

`pip install -r requirements.txt`

## Usage

To run this cellular automata, you can check the help of the ArgumentParser in Python:

`python main.py --help` will print below an instruction what arguments are required to run the simulation:

```
usage: main.py [-h] --grid_dim GRID_DIM --seed SEED --generations GENERATIONS

options:
  -h, --help            show this help message and exit
  --grid_dim GRID_DIM   Dimension of the grid
  --seed SEED           Seed for random number generation
  --generations GENERATIONS
                        Number of generations
```

## Dependencies

Project was built upon following libraries:

* matplotlib,
* numpy.

## Examples:

.gif file represents a simulation for following parameters:
* `seed` = 100,
* `# generations` = 5000,
* `grid_size` = 100;

![GameOfLife Example](https://github.com/kpomichowski/GameOfLife/blob/master/example/output.gif)

