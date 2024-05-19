import math
import random
import matplotlib.pyplot as plt

class ProximitySensor:
    def __init__(self, angle, range_percent):
        self.angle = angle  # Angle relative to robot's heading
        self.range = range_percent  # Range as a percentage of square length

    def detect_obstacle(self, robot_position, robot_heading, walls):
        # Calculate sensor's position relative to robot's position and heading
        # Adjust angle based on robot's heading
        adjusted_angle = self.angle + robot_heading
        sensor_x = robot_position[0] + math.cos(math.radians(adjusted_angle))
        sensor_y = robot_position[1] + math.sin(math.radians(adjusted_angle))

        # Check for obstacles within sensor's range
        for wall in walls:
            if self.is_within_range(robot_position, (sensor_x, sensor_y), wall):
                distance = self.calculate_distance(robot_position, (sensor_x, sensor_y), wall)
                return 1 - (distance / self.range)

        return 0  # No obstacle detected within range

    def is_within_range(self, robot_position, sensor_position, wall):
        # Check if the sensor's beam intersects with the wall
        # This could be done using ray tracing or other methods
        # For simplicity, we'll use a simple distance check
        distance_to_wall = math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
        return distance_to_wall <= self.range

    def calculate_distance(self, robot_position, sensor_position, wall):
        # Calculate the distance between the sensor and the wall
        return math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)


class RobotController:
    def __init__(self, sensors):
        self.sensors = sensors
        self.path = []  # to store the robot's path

    def navigate(self, robot_position, robot_heading, walls):
        # Read sensor values
        sensor_values = [sensor.detect_obstacle(robot_position, robot_heading, walls) for sensor in self.sensors]

        # Rule-based navigation
        if sensor_values[0] > 0.5:  # Obstacle detected on the left
            robot_heading -= 45  # Turn left
        elif sensor_values[2] > 0.5:  # Obstacle detected on the right
            robot_heading += 45  # Turn right

        # Move the robot forward
        robot_position = self.move_forward(robot_position, robot_heading)
        self.path.append(robot_position)  # add the new position to the path

        return robot_position, robot_heading

    def move_forward(self, position, heading):
        # Move the robot one step forward based on its current heading
        new_x = position[0] + math.cos(math.radians(heading))
        new_y = position[1] + math.sin(math.radians(heading))
        return new_x, new_y


def plot_environment(walls, path):
    fig, ax = plt.subplots()

    # Plot walls
    for wall in walls:
        ax.plot([wall[0], wall[2]], [wall[1], wall[3]], color='black')

    # Plot robot's path
    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]
    ax.plot(path_x, path_y, color='blue', marker='o')

    ax.set_aspect('equal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Robot Navigation')
    plt.grid(True)
    plt.show()  # Show the plot


# Define walls as (x1, y1, x2, y2) coordinates
walls = [(0, 0, 5, 0), (5, 0, 5, 5), (5, 5, 0, 5), (0, 5, 0, 0), (2, 2, 3, 2), (3, 3, 3, 2)]
robot_heading_list = [0, 1, 2, 3]

# Initialize robot position and heading
robot_position = (1, 1)
robot_heading = 0

# Initialize proximity sensors
sensor_left = ProximitySensor(angle=-45, range_percent=0.15)
sensor_front = ProximitySensor(angle=0, range_percent=0.15)
sensor_right = ProximitySensor(angle=45, range_percent=0.15)

sensors = [sensor_left, sensor_front, sensor_right]

# Initialize robot controller
controller = RobotController(sensors)

# Test navigation
for _ in range(20):  # Increased the number of iterations for more steps
    robot_position, robot_heading = controller.navigate(robot_position, robot_heading, walls)

for _ in range(10):

    print("Robot Position:", robot_position)
    print("Robot Heading:", random.choice(robot_heading_list))

    robot_position, robot_heading = controller.navigate(robot_position, robot_heading, walls)


# Plot the environment
plot_environment(walls, controller.path)
