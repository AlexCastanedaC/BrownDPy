import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def plot_3d_tr(r, num_particles):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    for i in range(num_particles):
        ax.plot(r[0,i,:], r[1,i,:], r[2,i,:], label=f'Particle {i+1}')
    
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')
    ax.set_title('3D Trajectories of Particles')
    ax.legend()
    plt.savefig('3d_trajectories.png')

def plot_2d_tr(r, num_particles):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    
    # Plot the xy plane trajectories 
    for i in range(num_particles):
        ax.plot(r[0, i, :], r[1, i, :], label=f'Particle {i+1}')
        # Set labels and title
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title(f'2D Trajectories of {num_particles} particle(s) (XY Plane)')
    ax.legend()
    plt.savefig('2d_trajectories.png')

def plot_msd(MSD, num_frames, delta_t):
    time = np.arange(num_frames) * delta_t
    popt, pcov = curve_fit(power_law, time[1:], MSD[1:])  # Skip the first point to avoid fitting issues
    A, n = popt
    # Plotting the result
    plt.figure(figsize=(10, 6))
    plt.loglog(time, MSD, label='MSD (simulation)')
    plt.loglog(time, power_law(time, A, n), '--', label=f'Fit: $At^n$, A={A:.3e}, n={n:.3f}')
    plt.xlabel('Lag Time')
    plt.ylabel('Mean Squared Displacement (MSD)')
    plt.title('MSD for Brownian Motion')
    plt.legend()
    plt.savefig('msd.png')
    print(f'Fitted parameters: A = {A}, n = {n}')

# Function to fit
def power_law(t, A, n):
    return A * t**n