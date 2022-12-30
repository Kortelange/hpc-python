import numpy as np
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'


def evolve(u, u_previous, a, dt, dx, dy):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    # TODO: determine the new temperature field based on previous values
    # and the numerical Laplacian according the explicit time evolution method
    lapx = -2*u_previous[1:-1, 1: -1].copy()
    lapx += u_previous[:-2, 1: -1]
    lapx += u_previous[2:, 1: -1]
    lapx /= dx**2
    lapy = -2*u_previous[1:-1, 1: -1].copy()
    lapy += u_previous[1: -1, : -2]
    lapy += u_previous[1: -1, 2:]
    lapy /= dy**2
    u[1: -1, 1: -1] = u_previous[1: -1, 1: -1] + a*dt*(lapx + lapy)
    u_previous[:] = u.copy()


def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""
    # TODO: Implement the main iteration loop and write the figure
    # (to a new) file after each 'image_interval' iteration
    dt = (1 / 2 / a) * (dx * dy) ** 2 / (dx ** 2 + dy ** 2)
    for step in range(timesteps + 1):
        if step % image_interval == 0:
            write_field(field, step)
        evolve(field, field0, a, dt, dx, dy)


def init_fields(filename):
# TODO: Read the initial temperature field from file
# Create also a copy of the field for the previous time step
    field = np.loadtxt(filename)
    field0 = field.copy()
    return field, field0


def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))
