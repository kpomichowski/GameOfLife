import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_automata(generator, seed, generations) -> None:
    fig = plt.figure(figsize=(15, 10))

    def update(frame):
        plt.clf()
        grid_state = next(generator)
        plt.imshow(grid_state, cmap='binary')
        plt.title(f'generation: {frame + 1}, seed: {seed}, no. generations: {generations}')

    anim = animation.FuncAnimation(fig, update, frames=generations, repeat=False)
    plt.show()