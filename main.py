import numpy as np
import math
import numpy as np

def main():
    
    num_particles = int(input("Enter the number of particles of your simulation: "))
    num_frames = int(input("Enter the number of frames of your simulation: "))
    delta_t = 1.0e-4

    r = random_walk(num_particles, num_frames, delta_t)

if __name__ == '__main__':
    main()

def random_walk(num_particles, num_frames, delta_t):

    r = np.zeros((3,num_particles, num_frames))
    
    for frame in range(1,num_frames):
        r[:,:,frame] = r[:, :, frame-1] + math.sqrt(2*delta_t)*np.random.normal(0, 1, size = (3, num_particles))

    return r