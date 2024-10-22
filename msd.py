import numpy as np

def MSD_3D(r, num_particles, num_frames):
    displacements = np.zeros((num_particles, num_frames))
    for i in range(num_frames):
        squared_displacement = np.sum((r[:, :, i:num_frames] - r[:, :, 0:num_frames-i])**2, axis=0)
        displacements[:, i] = np.mean(squared_displacement, axis=1)
    MSD = np.mean(displacements, axis=0)
    return MSD