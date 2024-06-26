import numpy as np
class HeatTransfer:
    """
    Simulates heat transfer representing a beer can.
    """

    def __init__(self, beer_initial_temperature, room_temperature,
                 grid_directory, dt, final_time, beer_density, 
                 save_path=None, save_interval=None):
        """
        Initializes the simulation parameters and loads the grid data.

        """

        self.beer_initial_temperature = beer_initial_temperature
        self.room_temperature = room_temperature
        self.dt = dt
        self.final_time = final_time
        self.beer_density = beer_density
        self.n_steps = int(final_time / dt)

        self.load_grid(grid_directory)
        self.initialize_temperature()
        
        self.save_path = save_path
        self.save_interval = save_interval

    def load_grid(self, grid_directory):
        """
        Loads the X and Y coordinates of the grid points from separate files.
        
        """

        self.X = np.loadtxt(f"{grid_directory}/grid_X.dat")
        self.Y = np.loadtxt(f"{grid_directory}/grid_Y.dat")

    def initialize_temperature(self):
        """
        Initializes the temperature array with the initial temperature inside
        and room temperature on the boundaries.
        """

        self.T = np.ones_like(self.X) * self.beer_initial_temperature
        self.T[:, 0] = self.T[:, -1] = self.room_temperature
        self.T[0, :] = self.T[-1, :] = self.room_temperature

    def run_simulation(self):
        """
        Runs the heat transfer simulation.
        """
        
        for step in range(self.n_steps):
           
            current_time = (step + 1) * self.dt

            for i in range(1, self.T.shape[0] - 1):
                for j in range(1, self.T.shape[1] - 1):
                    self.T[i, j] = self.update_temperature(i, j)
            
            # Save results if save_path and save_interval are defined
            if self.save_path and self.save_interval:
                if current_time % self.save_interval == 0:
                    self.save_results(current_time, self.T)

    def update_temperature(self, i, j):
        """
        Calculates the new temperature at a specific grid point based on the
        diffusion of the temperature in X and Y directions.

        """

        dx = self.X[i, j] - self.X[i, j - 1]
        dy = self.Y[i, j] - self.Y[i - 1, j]

        F2x = (self.T[i, j + 1] - self.T[i, j] + self.T[i, j - 1]) / (dx * dx)
        F2y = (self.T[i + 1, j] - self.T[i, j] + self.T[i - 1, j]) / (dy * dy)

        alpha = self.thermal_conductivity(self.T[i, j]) / (
            self.specific_heat_capacity(self.T[i, j]) * self.beer_density
        )

        return self.T[i, j] + self.dt * alpha * (F2x + F2y)
    
    def save_results(self, current_time, temperature_data):

        step_string = f"{int(current_time):04d}"  # Format step as 4-digit string
        filename = f"temperature_{step_string}.dat"
        filepath = f"{self.save_path}/{filename}"
        np.savetxt(filepath, temperature_data, delimiter=" ", fmt="%.6e")

    def specific_heat_capacity(self, temperature):

        return (2e-5 * temperature**2) - (2e-3 * temperature) + 4.118

    def thermal_conductivity(self, temperature):

        return (-8.116e-6 * temperature**2) + (1.9e-3 * temperature) + 0.54611