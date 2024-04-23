import sys
sys.path.append(".\hop_hour_ambipar\heat_transfer") 

from heat_transfer import HeatTransfer  # Import the HeatTransfer class
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Simulation parameters
    beer_initial_temperature = 4
    room_temperature = 22
    grid_directory = "D:\\d-users\\d-Naviersat\\Repositories\\hop_hour_ambipar\\grid"  # Update path if needed
    dt = 0.1
    final_time = 200
    beer_density = 1048

    # Create the simulation object
    simulation = HeatTransfer(
        beer_initial_temperature,
        room_temperature,
        grid_directory,
        dt,
        final_time,
        beer_density,
    )

    # Run the simulation
    simulation.run_simulation()
   
    final_temperature = simulation.T
    X = simulation.X
    Y = simulation.Y

    # Plot temperature 
    plt.contourf(X, Y, final_temperature, cmap="RdGy")  # Adjust colormap as desired
    plt.colorbar(label="Temperature (°C)")
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.title("Final Temperature Distribution in Beer Can")
    plt.axis('equal')
    plt.show()
