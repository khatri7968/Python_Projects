import numpy as np
import matplotlib.pyplot as plt

class Simulator:
    def __init__(self, square_size, wall_thickness):
        self.square_size = square_size
        self.wall_thickness = wall_thickness
        self.robot_size = 1  # Size of the robot (assumed to be a point)

    def detect_obstacle(self, position):
        # Check if position is within the bounds of the square
        if position[0] < self.wall_thickness or position[0] > self.square_size - self.wall_thickness \
                or position[1] < self.wall_thickness or position[1] > self.square_size - self.wall_thickness:
            return True  # Wall detected

        # Check if position is within inner walls
        if position[0] > self.square_size / 3 and position[0] < 2 * self.square_size / 3 \
                and position[1] > self.square_size / 3 and position[1] < 2 * self.square_size / 3:
            return True  # Inner wall detected

        return False

    def update_position(self, position, heading, speed):
        # Update position based on heading and speed
        dx = speed * np.cos(heading)
        dy = speed * np.sin(heading)
        new_position = position + np.array([dx, dy])

        # Ensure the robot doesn't pass through walls
        if not self.detect_obstacle(new_position):
            return new_position
        else:
            return position


class ProximitySensors:
    def __init__(self, simulator, robot_position, robot_heading, sensor_range):
        self.simulator = simulator
        self.robot_position = np.array(robot_position)
        self.robot_heading = robot_heading
        self.sensor_range = sensor_range

    def detect(self):
        # Calculate positions of sensors
        sensor_offsets = [np.array([np.cos(self.robot_heading + np.pi / 4),
                                    np.sin(self.robot_heading + np.pi / 4)]),  # Front-left sensor
                          np.array([np.cos(self.robot_heading),
                                    np.sin(self.robot_heading)]),  # Front sensor
                          np.array([np.cos(self.robot_heading - np.pi / 4),
                                    np.sin(self.robot_heading - np.pi / 4)])]  # Front-right sensor

        sensor_positions = [self.robot_position + offset * self.sensor_range for offset in sensor_offsets]

        # Detect obstacles
        obstacles_detected = [self.simulator.detect_obstacle(position) for position in sensor_positions]

        # Calculate sensor readings
        sensor_readings = [1 - np.linalg.norm(sensor_positions[i] - self.robot_position) / self.sensor_range
                           if obstacles_detected[i] else 0 for i in range(3)]

        return sensor_readings


class SimpleController:
    def __init__(self, proximity_sensors):
        self.proximity_sensors = proximity_sensors

    def control(self):
        # Read sensor data
        sensor_readings = self.proximity_sensors.detect()

        # Define control rules
        if sensor_readings[0] > 0.5:  # If obstacle detected by front-left sensor
            new_heading = self.proximity_sensors.robot_heading + np.pi / 4  # Turn right
        elif sensor_readings[1] > 0.5:  # If obstacle detected by front sensor
            new_heading = self.proximity_sensors.robot_heading - np.pi / 4  # Turn left
        elif sensor_readings[2] > 0.5:  # If obstacle detected by front-right sensor
            new_heading = self.proximity_sensors.robot_heading + np.pi / 4  # Turn right
        else:
            new_heading = self.proximity_sensors.robot_heading  # Continue straight

        return new_heading

# Test the implementation
simulator = Simulator(square_size=20, wall_thickness=2)
sensor_range = 3

# Function to generate a random initial position not inside obstacles
def generate_initial_position(simulator):
    while True:
        initial_position = np.array([np.random.uniform(simulator.wall_thickness, simulator.square_size - simulator.wall_thickness),
                                     np.random.uniform(simulator.wall_thickness, simulator.square_size - simulator.wall_thickness)])
        if not simulator.detect_obstacle(initial_position):
            return initial_position

initial_position = generate_initial_position(simulator)
initial_heading = np.pi / 4

print("Initial Position:", initial_position)
print("Sensor Range:", sensor_range)

proximity_sensors = ProximitySensors(simulator, initial_position, initial_heading, sensor_range)
controller = SimpleController(proximity_sensors)

trajectory = [initial_position.copy()]
heading = initial_heading

for _ in range(100):
    sensor_readings = proximity_sensors.detect()
    print("Sensor Readings:", sensor_readings)
    heading = controller.control()
    print("Heading:", heading)
    new_position = simulator.update_position(trajectory[-1], heading, 0.1)  # Use the last position from trajectory
    trajectory.append(new_position)

# Plot trajectory
trajectory = np.array(trajectory)
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectory of Robot with Proximity Sensors')
plt.show()
