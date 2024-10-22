import numpy as np
import math

def MSD_3D(r, num_particles, num_frames):
    displacements = np.zeros((num_particles, num_frames))
    for i in range(num_frames):
        squared_displacement = np.sum((r[:, :, i:num_frames] - r[:, :, 0:num_frames-i])**2, axis=0)
        displacements[:, i] = np.mean(squared_displacement, axis=1)
    MSD = np.mean(displacements, axis=0)
    return MSD

def random_walk(num_particles, num_frames, delta_t):

    r = np.zeros((3,num_particles, num_frames))
    
    for frame in range(1,num_frames):
        r[:,:,frame] = r[:, :, frame-1] + math.sqrt(2*delta_t)*np.random.normal(0, 1, size = (3, num_particles))

    return r