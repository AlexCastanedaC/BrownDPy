import numpy as np
import numpy as np

from msd import random_walk,MSD_3D
from bm_plots import plot_3d_tr, plot_2d_tr, plot_msd

    
num_particles = int(input("Enter the number of particles of your simulation: "))
num_frames = int(input("Enter the number of frames of your simulation: "))
delta_t = 1.0e-4

r = random_walk(num_particles, num_frames, delta_t)
MSD = MSD_3D(r, num_particles, num_frames)
plot_3d_tr(r, 3)
plot_2d_tr(r, 1)
plot_msd(MSD, num_frames, delta_t)


