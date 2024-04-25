import sys
sys.path.append(".\hop_hour_ambipar\heat_transfer") 

from heat_transfer import HeatTransfer  # Import the HeatTransfer class
import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
    # Simulation parameters
    with open("hop_hour_ambipar/config/simulation_config.json", "r") as f:
        params = json.load(f)

    beer_initial_temperature = params["beer_initial_temperature"]
    room_temperature = params["room_temperature"]
    grid_directory = params["grid_directory"]
    dt = params["dt"]
    final_time = params["final_time"]
    beer_density = params["beer_density"]
    save_path = params.get("save_path", None) 
    save_interval = params.get("save_interval", None)

    # simulation object
    simulation = HeatTransfer(
        beer_initial_temperature,
        room_temperature,
        grid_directory,
        dt,
        final_time,
        beer_density,
        save_path,
        save_interval
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
