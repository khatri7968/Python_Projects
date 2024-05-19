import numpy as np
import matplotlib.pyplot as plt

class BraitenbergSimulator:
    def __init__(self, width, height, light_source_position, light_intensity_decay_rate):
        self.width = width
        self.height = height
        self.light_source_position = light_source_position
        self.light_intensity_decay_rate = light_intensity_decay_rate

    def calculate_light_intensity(self, position):
        distance_to_light = np.linalg.norm(np.array(position) - np.array(self.light_source_position))
        light_intensity = max(0, 1 - self.light_intensity_decay_rate * distance_to_light)
        return light_intensity

    def update_robot_position(self, position, heading, speed, delta_heading, max_distance):
        # Update heading
        new_heading = (heading + delta_heading) % (2 * np.pi)

        # Update position
        new_position = [position[0] + speed * np.cos(new_heading),
                        position[1] + speed * np.sin(new_heading)]

        # Wrap around if out of bounds
        new_position[0] = new_position[0] % self.width
        new_position[1] = new_position[1] % self.height

        return new_position, new_heading

    def plot_light_intensity_field(self):
        x = np.linspace(0, self.width, 100)
        y = np.linspace(0, self.height, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)

        for i in range(len(x)):
            for j in range(len(y)):
                Z[i, j] = self.calculate_light_intensity([x[i], y[j]])

        plt.contourf(X, Y, Z, cmap='plasma')
        plt.colorbar(label='Light Intensity')
        plt.title('Light Intensity Field')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

# Test the implementation
simulator = BraitenbergSimulator(width=50, height=50, light_source_position=[25, 25], light_intensity_decay_rate=0.02)
simulator.plot_light_intensity_field()

