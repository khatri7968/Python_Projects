
 '''TASK __ 2'''
# import math
#
#
# class ProximitySensor:
#     def __init__(self, angle, range_percent):
#         self.angle = angle  # Angle relative to robot's heading
#         self.range = range_percent  # Range as a percentage of square length
#
#     def detect_obstacle(self, robot_position, robot_heading, walls):
#         # Calculate sensor's position relative to robot's position and heading
#         sensor_x = robot_position[0] + math.cos(math.radians(robot_heading + self.angle))
#         sensor_y = robot_position[1] + math.sin(math.radians(robot_heading + self.angle))
#
#         # Check for obstacles within sensor's range
#         for wall in walls:
#             if self.is_within_range(robot_position, (sensor_x, sensor_y), wall):
#                 distance = self.calculate_distance(robot_position, (sensor_x, sensor_y), wall)
#                 return 1 - (distance / self.range)
#
#         return 0  # No obstacle detected within range
#
#     def is_within_range(self, robot_position, sensor_position, wall):
#         # Check if the sensor's beam intersects with the wall
#         # This could be done using ray tracing or other methods
#         # For simplicity, we'll use a simple distance check
#         distance_to_wall = math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#         return distance_to_wall <= self.range
#
#     def calculate_distance(self, robot_position, sensor_position, wall):
#         # Calculate the distance between the sensor and the wall
#         return math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#
#
# class RobotController:
#     def __init__(self, sensors):
#         self.sensors = sensors
#
#     def navigate(self, robot_position, robot_heading, walls):
#         # Read sensor values
#         sensor_values = [sensor.detect_obstacle(robot_position, robot_heading, walls) for sensor in self.sensors]
#
#         # Rule-based navigation
#         if sensor_values[0] > 0.5:  # Obstacle detected on the left
#             robot_heading += 45  # Turn right
#         elif sensor_values[2] > 0.5:  # Obstacle detected on the right
#             robot_heading -= 45  # Turn left
#         elif sensor_values[1] > 0.5:  # Obstacle detected straight ahead
#             robot_heading += 180  # Turn around
#
#         # Move the robot forward
#         robot_position = self.move_forward(robot_position, robot_heading)
#
#         return robot_position, robot_heading
#
#     def move_forward(self, position, heading):
#         # Move the robot one step forward based on its current heading
#         new_x = position[0] + math.cos(math.radians(heading))
#         new_y = position[1] + math.sin(math.radians(heading))
#         return new_x, new_y
#
#
# # Define walls as (x, y) coordinates
# walls = [(0, 0), (5, 0), (5, 5), (0, 5), (2, 2), (3, 3)]
#
# # Initialize robot position and heading
# robot_position = (1, 1)
# robot_heading = 0  # Facing east
#
# # Initialize proximity sensors
# sensor_left = ProximitySensor(angle=-45, range_percent=0.15)
# sensor_front = ProximitySensor(angle=0, range_percent=0.15)
# sensor_right = ProximitySensor(angle=45, range_percent=0.15)
#
# sensors = [sensor_left, sensor_front, sensor_right]
#
# # Initialize robot controller
# controller = RobotController(sensors)
#
# # Test navigation
# for _ in range(10):
#     print("Robot Position:", robot_position)
#     print("Robot Heading:", robot_heading)
#     robot_position, robot_heading = controller.navigate(robot_position, robot_heading, walls)


# import math
#
# class ProximitySensor:
#     def __init__(self, angle, range_percent):
#         self.angle = angle  # Angle relative to robot's heading
#         self.range = range_percent  # Range as a percentage of square length
#
#     def detect_obstacle(self, robot_position, robot_heading, walls):
#         # Calculate sensor's position relative to robot's position and heading
#         # Adjust angle based on robot's heading
#         adjusted_angle = self.angle + robot_heading
#         sensor_x = robot_position[0] + math.cos(math.radians(adjusted_angle))
#         sensor_y = robot_position[1] + math.sin(math.radians(adjusted_angle))
#
#         # Check for obstacles within sensor's range
#         for wall in walls:
#             if self.is_within_range(robot_position, (sensor_x, sensor_y), wall):
#                 distance = self.calculate_distance(robot_position, (sensor_x, sensor_y), wall)
#                 return 1 - (distance / self.range)
#
#         return 0  # No obstacle detected within range
#
#     def is_within_range(self, robot_position, sensor_position, wall):
#         # Check if the sensor's beam intersects with the wall
#         # This could be done using ray tracing or other methods
#         # For simplicity, we'll use a simple distance check
#         distance_to_wall = math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#         return distance_to_wall <= self.range
#
#     def calculate_distance(self, robot_position, sensor_position, wall):
#         # Calculate the distance between the sensor and the wall
#         return math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#
#
# class RobotController:
#     def __init__(self, sensors):
#         self.sensors = sensors
#
#     def navigate(self, robot_position, robot_heading, walls):
#         # Read sensor values
#         sensor_values = [sensor.detect_obstacle(robot_position, robot_heading, walls) for sensor in self.sensors]
#
#         # Rule-based navigation
#         if sensor_values[0] > 0.5:  # Obstacle detected on the left
#             robot_heading += 45  # Turn right
#         elif sensor_values[2] > 0.5:  # Obstacle detected on the right
#             robot_heading -= 45  # Turn left
#         elif sensor_values[1] > 0.5:  # Obstacle detected straight ahead
#             robot_heading += 180  # Turn around
#
#         # Move the robot forward
#         robot_position = self.move_forward(robot_position, robot_heading)
#
#         return robot_position, robot_heading
#
#     def move_forward(self, position, heading):
#         # Move the robot one step forward based on its current heading
#         new_x = position[0] + math.cos(math.radians(heading))
#         new_y = position[1] + math.sin(math.radians(heading))
#         return new_x, new_y
#
#
# # Define walls as (x, y) coordinates
# walls = [(0, 0), (5, 0), (5, 5), (0, 5), (2, 2), (3, 3)]
#
# # Initialize robot position and heading
# robot_position = (1, 1)
# robot_heading = 0  # Facing east
#
# # Initialize proximity sensors
# sensor_left = ProximitySensor(angle=-45, range_percent=0.15)
# sensor_front = ProximitySensor(angle=0, range_percent=0.15)
# sensor_right = ProximitySensor(angle=45, range_percent=0.15)
#
# sensors = [sensor_left, sensor_front, sensor_right]
#
# # Initialize robot controller
# controller = RobotController(sensors)
#
# # Test navigation
# for _ in range(10):
#     print("Robot Position:", robot_position)
#     print("Robot Heading:", robot_heading)
#     robot_position, robot_heading = controller.navigate(robot_position, robot_heading, walls)
#

# import math
#
# class ProximitySensor:
#     def __init__(self, angle, range_percent):
#         self.angle = angle  # Angle relative to robot's heading
#         self.range = range_percent  # Range as a percentage of square length
#
#     def detect_obstacle(self, robot_position, robot_heading, walls):
#         # Calculate sensor's position relative to robot's position and heading
#         # Adjust angle based on robot's heading
#         adjusted_angle = self.angle + robot_heading
#         sensor_x = robot_position[0] + math.cos(math.radians(adjusted_angle))
#         sensor_y = robot_position[1] + math.sin(math.radians(adjusted_angle))
#
#         # Check for obstacles within sensor's range
#         for wall in walls:
#             if self.is_within_range(robot_position, (sensor_x, sensor_y), wall):
#                 distance = self.calculate_distance(robot_position, (sensor_x, sensor_y), wall)
#                 return 1 - (distance / self.range)
#
#         return 0  # No obstacle detected within range
#
#     def is_within_range(self, robot_position, sensor_position, wall):
#         # Check if the sensor's beam intersects with the wall
#         # This could be done using ray tracing or other methods
#         # For simplicity, we'll use a simple distance check
#         distance_to_wall = math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#         return distance_to_wall <= self.range
#
#     def calculate_distance(self, robot_position, sensor_position, wall):
#         # Calculate the distance between the sensor and the wall
#         return math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#
#
# class RobotController:
#     def __init__(self, sensors):
#         self.sensors = sensors
#
#     def navigate(self, robot_position, robot_heading, walls):
#         # Read sensor values
#         sensor_values = [sensor.detect_obstacle(robot_position, robot_heading, walls) for sensor in self.sensors]
#
#         # Rule-based navigation
#         if sensor_values[0] > 0.5:  # Obstacle detected on the left
#             robot_heading -= 45  # Turn left
#         elif sensor_values[2] > 0.5:  # Obstacle detected on the right
#             robot_heading += 45  # Turn right
#
#         # Move the robot forward
#         robot_position = self.move_forward(robot_position, robot_heading)
#
#         return robot_position, robot_heading
#
#     def move_forward(self, position, heading):
#         # Move the robot one step forward based on its current heading
#         new_x = position[0] + math.cos(math.radians(heading))
#         new_y = position[1] + math.sin(math.radians(heading))
#         return new_x, new_y
#
#
# # Define walls as (x, y) coordinates
# walls = [(0, 0), (5, 0), (5, 5), (0, 5), (2, 2), (3, 3)]
#
# # Initialize robot position and heading
# robot_position = (1, 1)
# robot_heading = 0  # Facing east
#
# # Initialize proximity sensors
# sensor_left = ProximitySensor(angle=-45, range_percent=0.15)
# sensor_front = ProximitySensor(angle=0, range_percent=0.15)
# sensor_right = ProximitySensor(angle=45, range_percent=0.15)
#
# sensors = [sensor_left, sensor_front, sensor_right]
#
# # Initialize robot controller
# controller = RobotController(sensors)
#
# # Test navigation
# for _ in range(20):  # Increased the number of iterations for more steps
#     print("Robot Position:", robot_position)
#     print("Robot Heading:", robot_heading)
#     robot_position, robot_heading = controller.navigate(robot_position, robot_heading, walls)

# import math
# import matplotlib.pyplot as plt
#
#
# class ProximitySensor:
#     def __init__(self, angle, range_percent):
#         self.angle = angle  # Angle relative to robot's heading
#         self.range = range_percent  # Range as a percentage of square length
#
#     def detect_obstacle(self, robot_position, robot_heading, walls):
#         # Calculate sensor's position relative to robot's position and heading
#         # Adjust angle based on robot's heading
#         adjusted_angle = self.angle + robot_heading
#         sensor_x = robot_position[0] + math.cos(math.radians(adjusted_angle))
#         sensor_y = robot_position[1] + math.sin(math.radians(adjusted_angle))
#
#         # Check for obstacles within sensor's range
#         for wall in walls:
#             if self.is_within_range(robot_position, (sensor_x, sensor_y), wall):
#                 distance = self.calculate_distance(robot_position, (sensor_x, sensor_y), wall)
#                 return 1 - (distance / self.range)
#
#         return 0  # No obstacle detected within range
#
#     def is_within_range(self, robot_position, sensor_position, wall):
#         # Check if the sensor's beam intersects with the wall
#         # This could be done using ray tracing or other methods
#         # For simplicity, we'll use a simple distance check
#         distance_to_wall = math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#         return distance_to_wall <= self.range
#
#     def calculate_distance(self, robot_position, sensor_position, wall):
#         # Calculate the distance between the sensor and the wall
#         return math.sqrt((sensor_position[0] - wall[0]) ** 2 + (sensor_position[1] - wall[1]) ** 2)
#
#
# class RobotController:
#     def __init__(self, sensors):
#         self.sensors = sensors
#         self.path = []  # to store the robot's path
#
#     def navigate(self, robot_position, robot_heading, walls):
#         # Read sensor values
#         sensor_values = [sensor.detect_obstacle(robot_position, robot_heading, walls) for sensor in self.sensors]
#
#         # Rule-based navigation
#         if sensor_values[0] > 0.5:  # Obstacle detected on the left
#             robot_heading -= 45  # Turn left
#         elif sensor_values[2] > 0.5:  # Obstacle detected on the right
#             robot_heading += 45  # Turn right
#
#         # Move the robot forward
#         robot_position = self.move_forward(robot_position, robot_heading)
#         self.path.append(robot_position)  # add the new position to the path
#
#         return robot_position, robot_heading
#
#     def move_forward(self, position, heading):
#         # Move the robot one step forward based on its current heading
#         new_x = position[0] + math.cos(math.radians(heading))
#         new_y = position[1] + math.sin(math.radians(heading))
#         return new_x, new_y
#
#
# def plot_environment(walls, path):
#     fig, ax = plt.subplots()
#
#     # Plot walls
#     for wall in walls:
#         ax.plot([wall[0], wall[1]], [wall[2], wall[3]], color='black')
#
#     # Plot robot's path
#     path_x = [point[0] for point in path]
#     path_y = [point[1] for point in path]
#     ax.plot(path_x, path_y, color='blue', marker='o')
#
#     ax.set_aspect('equal')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Robot Navigation')
#     plt.grid(True)
#     plt.show()
#
#
# # Define walls as (x1, y1, x2, y2) coordinates
# walls = [(0, 0, 5, 0), (5, 0, 5, 5), (5, 5, 0, 5), (0, 5, 0, 0), (2, 2, 3, 2), (3, 3, 3, 2)]
#
# # Initialize robot position and heading
# robot_position = (1, 1)
# robot_heading = 0  # Facing east
#
# # Initialize proximity sensors
# sensor_left = ProximitySensor(angle=-45, range_percent=0.15)
# sensor_front = ProximitySensor(angle=0, range_percent=0.15)
# sensor_right = ProximitySensor(angle=45, range_percent=0.15)
#
# sensors = [sensor_left, sensor_front, sensor_right]
#
# # Initialize robot controller
# controller = RobotController(sensors)
#
# # Test navigation
# for _ in range(20):  # Increased the number of iterations for more steps
#     robot_position, robot_heading = controller.navigate(robot_position, robot_heading, walls)
#
# # Plot the environment
# plot_environment(walls, controller.path)

'''TASK __ 1'''

# import numpy as np
# import matplotlib.pyplot as plt
#
# class Simulator:
#     def __init__(self, width, height, light_source_position, light_intensity_decay_rate):
#         self.width = width
#         self.height = height
#         self.light_source_position = np.array(light_source_position)
#         self.light_intensity_decay_rate = light_intensity_decay_rate
#
#     def calculate_light_intensity(self, position):
#         distance = np.linalg.norm(position - self.light_source_position)
#         return 1 / (1 + self.light_intensity_decay_rate * distance)
#
#     def update_position(self, position, heading, speed, max_distance_per_step, max_angle_per_step):
#         # Limit angle change per time step
#         heading += np.random.uniform(-max_angle_per_step, max_angle_per_step)
#         heading %= 2 * np.pi
#
#         # Limit distance traveled per time step
#         distance = np.random.uniform(0, max_distance_per_step)
#         dx = distance * np.cos(heading)
#         dy = distance * np.sin(heading)
#
#         # Wrap around if going beyond the borders (torus-like space)
#         new_x = (position[0] + dx) % self.width
#         new_y = (position[1] + dy) % self.height
#
#         return np.array([new_x, new_y]), heading
#
#
# class BraitenbergVehicle:
#     def __init__(self, simulator, initial_position, initial_heading, initial_speed):
#         self.simulator = simulator
#         self.position = np.array(initial_position)
#         self.heading = initial_heading
#         self.speed = initial_speed
#
#     def calculate_sensor_positions(self):
#         sensor_distance = 1.0  # Distance between sensors
#         sensor_angle = np.pi / 4  # Angle between heading and sensor direction
#
#         left_sensor_offset = np.array([np.cos(self.heading + sensor_angle),
#                                         np.sin(self.heading + sensor_angle)]) * sensor_distance
#         right_sensor_offset = np.array([np.cos(self.heading - sensor_angle),
#                                          np.sin(self.heading - sensor_angle)]) * sensor_distance
#
#         left_sensor_position = self.position + left_sensor_offset
#         right_sensor_position = self.position + right_sensor_offset
#
#         return left_sensor_position, right_sensor_position
#
#     def read_sensors(self):
#         left_sensor_position, right_sensor_position = self.calculate_sensor_positions()
#         left_sensor_intensity = self.simulator.calculate_light_intensity(left_sensor_position)
#         right_sensor_intensity = self.simulator.calculate_light_intensity(right_sensor_position)
#         return left_sensor_intensity, right_sensor_intensity
#
#     def update_movement(self, aggressor=False):
#         left_sensor_intensity, right_sensor_intensity = self.read_sensors()
#
#         if aggressor:
#             vl = right_sensor_intensity
#             vr = left_sensor_intensity
#         else:
#             vl = left_sensor_intensity
#             vr = right_sensor_intensity
#
#         c = 0.1  # Constant for determining heading change
#         delta_phi = c * (vr - vl)
#         self.heading += delta_phi
#         self.position, self.heading = self.simulator.update_position(self.position, self.heading, self.speed, 0.1, np.pi / 6)
#
#
# # Test the implementation
# simulator = Simulator(width=20, height=20, light_source_position=[10, 10], light_intensity_decay_rate=0.05)
# vehicle1 = BraitenbergVehicle(simulator, initial_position=[5, 5], initial_heading=np.pi/4, initial_speed=0.1)
# vehicle2 = BraitenbergVehicle(simulator, initial_position=[15, 15], initial_heading=np.pi/2, initial_speed=0.1)
#
# trajectory1 = [vehicle1.position.copy()]
# trajectory2 = [vehicle2.position.copy()]
#
# for _ in range(100):
#     vehicle1.update_movement(aggressor=True)
#     vehicle2.update_movement(aggressor=False)
#     trajectory1.append(vehicle1.position.copy())
#     trajectory2.append(vehicle2.position.copy())
#
# # Plot trajectories
# trajectory1 = np.array(trajectory1)
# trajectory2 = np.array(trajectory2)
#
# plt.plot(trajectory1[:, 0], trajectory1[:, 1], label='Aggressor')
# plt.plot(trajectory2[:, 0], trajectory2[:, 1], label='Scaredy-cat')
# plt.scatter(simulator.light_source_position[0], simulator.light_source_position[1], color='yellow', label='Light source')
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Trajectories of Braitenberg Vehicles')
# plt.show()
#
# #
# # import math
# # import matplotlib.pyplot as plt
# #
# # class Simulator:
# #   def __init__(self, width, height, light_source, max_speed, max_turn):
# #     self.width = width
# #     self.height = height
# #     self.light_source = light_source
# #     self.max_speed = max_speed
# #     self.max_turn = max_turn
# #
# #   def get_light_intensity(self, position):
# #     distance = math.sqrt(((position[0] - self.light_source[0])**2) + ((position[1] - self.light_source[1])**2))
# #     return 1.0 - distance / (self.width / 2)  # Linear decrease with distance
# #
# #   def update_robot(self, robot):
# #     # Update position (torus wrap-around)
# #     robot.position[0] = (robot.position[0] + robot.speed * math.cos(robot.heading)) % self.width
# #     robot.position[1] = (robot.position[1] + robot.speed * math.sin(robot.heading)) % self.height
# #
# #     # Update heading based on differential drive
# #     robot.heading += robot.turn_rate
# #
# #     # Limit heading change
# #     robot.heading = robot.heading % (2 * math.pi)
# #
# # class BraitenbergVehicle:
# #   def __init__(self, simulator, sensor_positions, fear=False):
# #     self.simulator = simulator
# #     self.position = [simulator.width / 2, simulator.height / 2]
# #     self.heading = 0.0
# #     self.speed = simulator.max_speed
# #     self.sensor_positions = sensor_positions
# #     self.fear = fear
# #
# #   def get_sensor_readings(self):
# #     sensor_readings = []
# #     for sensor_pos in self.sensor_positions:
# #       sensor_position = [self.position[0] + sensor_pos[0] * math.cos(self.heading) - sensor_pos[1] * math.sin(self.heading),
# #                         self.position[1] + sensor_pos[0] * math.sin(self.heading) + sensor_pos[1] * math.cos(self.heading)]
# #       sensor_readings.append(self.simulator.get_light_intensity(sensor_position))
# #     return sensor_readings
# #
# #   def update(self):
# #     sensor_readings = self.get_sensor_readings()
# #     left_sensor, right_sensor = sensor_readings
# #
# #     # Braitenberg Vehicle control (fear or aggression)
# #     if self.fear:
# #       left_velocity = right_sensor
# #       right_velocity = left_sensor
# #     else:
# #       left_velocity = left_sensor
# #       right_velocity = right_sensor
# #
# #     # Update turn rate based on differential drive
# #     self.turn_rate = self.simulator.max_turn * (right_velocity - left_velocity)
# #
# # # Example usage
# # simulator = Simulator(width=100, height=100, light_source=(50, 50), max_speed=1.0, max_turn=0.5)
# #
# # # Fearful vehicle
# # fearful_vehicle = BraitenbergVehicle(simulator, sensor_positions=[(0.5, 1.0), (-0.5, 1.0)], fear=True)
# #
# # # Aggressive vehicle
# # aggressive_vehicle = BraitenbergVehicle(simulator, sensor_positions=[(0.5, 1.0), (-0.5, 1.0)])
# #
# # # List to store robot positions for visualization
# # fearful_positions = []
# # aggressive_positions = []
# #
# # # Update and record robot movements
# # for _ in range(100):
# #   fearful_vehicle.update()
# #   aggressive_vehicle.update()
# #   fearful_positions.append(fearful_vehicle.position.copy())
# #   aggressive_positions.append(aggressive_vehicle.position.copy())
# #
# # # # Plot robot trajectories
# # # plt.figure(figsize=(8, 8))
# # # fearful_x, fearful_y = zip(*fearful_positions)
# # # aggressive_x, aggressive_y = zip(*aggressive_positions)
# # # plt.plot(fearful_x, fearful_y, label='Fearful')
# # # plt.plot(aggressive_x, aggressive_y, label='Aggressive')
# # # plt.scatter(simulator.light_source[0], simulator.light_source[1], marker='o', color='yellow
# #
# # plt.figure(figsize=(8, 8))
# # fearful_x, fearful_y = zip(*fearful_positions)
# # aggressive_x, aggressive_y = zip(*aggressive_positions)
# # plt.plot(fearful_x, fearful_y, label='Fearful')
# # plt.plot(aggressive_x, aggressive_y, label='Aggressive')
# # plt.scatter(simulator.light_source[0], simulator.light_source[1], marker='o', color='yellow', label='Light Source')
# #
# # # Add labels and title
# # plt.xlabel('X-Position')
# # plt.ylabel('Y-Position')
# # plt.title('Braitenberg Vehicle Trajectories (Fearful vs. Aggressive)')
# #
# # # Add legend
# # plt.legend()
# #
# # # Set axis limits (optional, adjust based on your simulation)
# # plt.xlim(0, simulator.width)
# # plt.ylim(0, simulator.height)
# #
# # # Show the plot
# # plt.grid(True)
# # plt.show()
# # import math
# # import matplotlib.pyplot as plt
# #
# # class Simulator:
# #   def __init__(self, width, height, light_source, max_speed, max_turn):
# #     self.width = width
# #     self.height = height
# #     self.light_source = light_source
# #     self.max_speed = max_speed
# #     self.max_turn = max_turn
# #
# #   def get_light_intensity(self, position):
# #     distance = math.sqrt(((position[0] - self.light_source[0])**2) + ((position[1] - self.light_source[1])**2))
# #     return 1.0 - distance / (self.width / 2)  # Linear decrease with distance
# #
# #   def update_robot(self, robot):
# #     # Update position (torus wrap-around)
# #     robot.position[0] = (robot.position[0] + robot.speed * math.cos(robot.heading)) % self.width
# #     robot.position[1] = (robot.position[1] + robot.speed * math.sin(robot.heading)) % self.height
# #
# #     # Update heading based on differential drive
# #     robot.heading += robot.turn_rate
# #
# #     # Limit heading change
# #     robot.heading = robot.heading % (2 * math.pi)
# #
# # class BraitenbergVehicle:
# #   def __init__(self, simulator, sensor_positions, fear=False):
# #     self.simulator = simulator
# #     self.position = [simulator.width / 2, simulator.height / 2]
# #     self.heading = 0.0
# #     self.speed = simulator.max_speed
# #     self.sensor_positions = sensor_positions
# #     self.fear = fear
# #
# #   def get_sensor_readings(self):
# #     sensor_readings = []
# #     for sensor_pos in self.sensor_positions:
# #       sensor_position = [self.position[0] + sensor_pos[0] * math.cos(self.heading) - sensor_pos[1] * math.sin(self.heading),
# #                         self.position[1] + sensor_pos[0] * math.sin(self.heading) + sensor_pos[1] * math.cos(self.heading)]
# #       sensor_readings.append(self.simulator.get_light_intensity(sensor_position))
# #     return sensor_readings
# #
# #   def update(self):
# #     sensor_readings = self.get_sensor_readings()
# #     left_sensor, right_sensor = sensor_readings
# #
# #     # Braitenberg Vehicle control (fear or aggression)
# #     if self.fear:
# #       left_velocity = right_sensor
# #       right_velocity = left_sensor
# #     else:
# #       left_velocity = left_sensor
# #       right_velocity = right_sensor
# #
# #     # Update turn rate based on differential drive
# #     self.turn_rate = self.simulator.max_turn * (right_velocity - left_velocity)
# #
# # # Example usage
# # simulator = Simulator(width=100, height=100, light_source=(50, 50), max_speed=1.0, max_turn=0.5)
# #
# # # Fearful vehicle
# # fearful_vehicle = BraitenbergVehicle(simulator, sensor_positions=[(0.5, 1.0), (-0.5, 1.0)], fear=True)
# #
# # # Aggressive vehicle
# # aggressive_vehicle = BraitenbergVehicle(simulator, sensor_positions=[(0.5, 1.0), (-0.5, 1.0)])
# #
# # # List to store robot positions for visualization
# # fearful_positions = []
# # aggressive_positions = []
# #
# # # Update and record robot movements
# # for _ in range(100):
# #   fearful_vehicle.update()
# #   aggressive_vehicle.update()
# #   fearful_positions.append(fearful_vehicle.position.copy())
# #   aggressive_positions.append(aggressive_vehicle.position.copy())
# #
# # # Plot robot trajectories
# # plt.figure(figsize=(8, 8))
# # fearful_x, fearful_y = zip(*fearful_positions)
# # aggressive_x, aggressive_y = zip(*aggressive_positions)
# # plt.plot(fearful_x, fearful_y, label='Fearful')
# # plt.plot(aggressive_x, aggressive_y, label='Aggressive')
# # plt.scatter(simulator.light_source[0], simulator.light_source[1], marker='o', color='yellow', label='Light Source')
# #
# # # Add labels and title
# # plt.xlabel('X-Position')
# # plt.ylabel('Y-Position')
# # plt.title('Braitenberg Vehicle Trajectories (Fearful vs. Aggressive)')
# #
# # # Add legend
# # plt.legend()
# #
# # # Set axis limits (optional, adjust based on your simulation)
# # plt.xlim(0, simulator.width)
# # plt.ylim(0, simulator.height)
# #
# # # Show the plot
# # plt.grid(True)
# # plt.show()

#
# import matplotlib.pyplot as plt
# import numpy as np
#
# class Torus:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
#
#   def wrap_position(self, x, y):
#     return (x % self.width, y % self.height)
#
# class Robot:
#   def __init__(self, simulator, x, y, heading, speed, sensor_distance, sensor_angle, is_aggressor):
#     self.simulator = simulator
#     self.x, self.y = simulator.wrap_position(x, y)
#     self.heading = heading
#     self.speed = speed
#     self.sensor_distance = sensor_distance
#     self.sensor_angle = sensor_angle
#     self.is_aggressor = is_aggressor  # Flag for robot type
#
#   def get_sensor_positions(self):
#     left_sensor_x = self.x + self.sensor_distance * np.cos(self.heading + self.sensor_angle)
#     left_sensor_y = self.y + self.sensor_distance * np.sin(self.heading + self.sensor_angle)
#     right_sensor_x = self.x + self.sensor_distance * np.cos(self.heading - self.sensor_angle)
#     right_sensor_y = self.y + self.sensor_distance * np.sin(self.heading - self.sensor_angle)
#     return left_sensor_x, left_sensor_y, right_sensor_x, right_sensor_y
#
#   def get_light_intensity(self, x, y):
#     distance = np.sqrt(((x - self.simulator.light_source[0])**2) + ((y - self.simulator.light_source[1])**2))
#     return max(0, 1 - distance / self.simulator.light_radius)
#
#   def update(self):
#     left_sensor_x, left_sensor_y, right_sensor_x, right_sensor_y = self.get_sensor_positions()
#     left_light_intensity = self.get_light_intensity(left_sensor_x, left_sensor_y)
#     right_light_intensity = self.get_light_intensity(right_sensor_x, right_sensor_y)
#     light_difference = right_light_intensity - left_light_intensity
#
#     # Braitenberg Vehicle control (modify for aggressor/fearful)
#     if self.is_aggressor:
#       left_speed = right_light_intensity
#       right_speed = left_light_intensity
#     else:
#       left_speed = left_light_intensity
#       right_speed = right_light_intensity
#
#     new_heading = self.heading + self.rotation_factor * (right_speed - left_speed)
#     self.heading = np.mod(new_heading, 2*np.pi)
#
#     dx = self.speed * np.cos(self.heading)
#     dy = self.speed * np.sin(self.heading)
#     self.x, self.y = self.simulator.wrap_position(self.x + dx, self.y + dy)
#
# class Simulator:
#   def __init__(self, width, height, light_source, light_radius):
#     self.torus = Torus(width, height)
#     self.light_source = light_source
#     self.light_radius = light_radius
#     self.robots = []
#
#   def add_robot(self, robot):
#     self.robots.append(robot)
#
#   def update(self):
#     for robot in self.robots:
#       robot.update()
#
#   def visualize(self):
#     plt.figure(figsize=(8, 6))
#     light_intensity_field = np.zeros((self.torus.width, self.torus.height))
#     for x in range(self.torus.width):
#       for y in range(self.torus.height):
#         light_intensity_field[x, y] = self.get_light_intensity(x, y)
#     plt.imshow(light_intensity_field, cmap='Greys', extent=(0, self.torus.width, 0, self.torus.height), alpha=0.3)
#     for robot in self.robots:
#       plt.plot(robot.x, robot.y)
#
# # Example Usage
# simulator = Simulator(width=50, height=50, light_source=(25, 25), light_radius=20)
#
# # Aggressor Robot
# robot1 = Robot(simulator, 10, 10, np.pi / 2, 1, 2, np.pi / 6, is_aggressor=True)
# simulator.add_robot(robot1)
#
# # Fearful Robot
# robot2 = Robot(simulator, 40, 40, 3 * np.pi / 2, 1, 2, np.pi / 6, is_aggressor=False)
# simulator.add_robot(robot2)
#
# # Run the simulation for 100 steps
# for _ in range(100):
#   simulator.update()
#
# # Visualize the results
# simulator.visualize()
# plt.show()
#


# import matplotlib.pyplot as plt
# import numpy as np
#
# class Torus:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
#
#   def wrap_position(self, x, y):
#     return (x % self.width, y % self.height)
#
# class Robot:
#   def __init__(self, torus, x, y, heading, speed, sensor_distance, sensor_angle, is_aggressor):
#     self.torus = torus  # Pass the Torus instance
#     self.x, self.y = self.torus.wrap_position(x, y)
#     self.heading = heading
#     self.speed = speed
#     self.sensor_distance = sensor_distance
#     self.sensor_angle = sensor_angle
#     self.is_aggressor = is_aggressor  # Flag for robot type
#
#     # Rest of the Robot class code remains the same
#
# class Simulator:
#   def __init__(self, width, height, light_source, light_radius):
#     self.torus = Torus(width, height)  # Create a Torus instance
#     self.light_source = light_source
#     self.light_radius = light_radius
#     self.robots = []
#
#   # Rest of the Simulator class code remains the same
#
#
#   def add_robot(self, robot):
#     self.robots.append(robot)
#
#   def update(self):
#       left_sensor_x, left_sensor_y, right_sensor_x, right_sensor_y = self.get_sensor_positions()
#       left_light_intensity = self.get_light_intensity(left_sensor_x, left_sensor_y)
#       right_light_intensity = self.get_light_intensity(right_sensor_x, right_sensor_y)
#       light_difference = right_light_intensity - left_light_intensity
#
#       # Braitenberg Vehicle control (modify for aggressor/fearful)
#       if self.is_aggressor:
#           left_speed = right_light_intensity
#           right_speed = left_light_intensity
#       else:
#           left_speed = left_light_intensity
#           right_speed = right_light_intensity
#
#       new_heading = self.heading + self.rotation_factor * (right_speed - left_speed)
#       self.heading = np.mod(new_heading, 2 * np.pi)
#
#       dx = self.speed * np.cos(self.heading)
#       dy = self.speed * np.sin(self.heading)
#       self.x, self.y = self.torus.wrap_position(self.x + dx, self.y + dy)
#
#   def visualize(self):
#     plt.figure(figsize=(8, 6))
#     light_intensity_field = np.zeros((self.torus.width, self.torus.height))
#     for x in range(self.torus.width):
#       for y in range(self.torus.height):
#         light_intensity_field[x, y] = self.get_light_intensity(x, y)
#     plt.imshow(light_intensity_field, cmap='Greys', extent=(0, self.torus.width, 0, self.torus.height), alpha=0.3)
#     for robot in self.robots:
#       plt.plot(robot.x, robot.y)
#
# # Example Usage (modified)
# simulator = Simulator(width=50, height=50, light_source=(25, 25), light_radius=20)
# torus = simulator.torus  # Get the Torus instance from the Simulator
#
# # Aggressor Robot
# robot1 = Robot(torus, 10, 10, np.pi / 2, 1, 2, np.pi / 6, is_aggressor=True)
# simulator.add_robot(robot1)
#
# # Fearful Robot
# robot2 = Robot(torus, 40, 40, 3 * np.pi / 2, 1, 2, np.pi / 6, is_aggressor=False)
# simulator.add_robot(robot2)
#
# # Run the simulation for 100 steps (unchanged)
# # Visualize the results (unchanged)
#
# # Run the simulation for 100 steps
# for _ in range(100):
#   simulator.update()
#
# # Visualize the results
# simulator.visualize()
# plt.show()
#

# import matplotlib.pyplot as plt
# import numpy as np
#
# class Torus:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
#
#   def wrap_position(self, x, y):
#     return (x % self.width, y % self.height)
#
# class Robot:
#   def __init__(self, torus, x, y, heading, speed, sensor_distance, sensor_angle, is_aggressor):
#     self.torus = torus  # Pass the Torus instance
#     self.x, self.y = self.torus.wrap_position(x, y)
#     self.heading = heading
#     self.speed = speed
#     self.sensor_distance = sensor_distance
#     self.sensor_angle = sensor_angle
#     self.is_aggressor = is_aggressor  # Flag for robot type
#
#   def get_sensor_positions(self):
#     left_sensor_x = self.x + self.sensor_distance * np.cos(self.heading + self.sensor_angle)
#     left_sensor_y = self.y + self.sensor_distance * np.sin(self.heading + self.sensor_angle)
#     right_sensor_x = self.x + self.sensor_distance * np.cos(self.heading - self.sensor_angle)
#     right_sensor_y = self.y + self.sensor_distance * np.sin(self.heading - self.sensor_angle)
#     return left_sensor_x, left_sensor_y, right_sensor_x, right_sensor_y
#
#   def get_light_intensity(self, x, y):
#     distance = np.sqrt(((x - self.simulator.light_source[0])**2) + ((y - self.simulator.light_source[1])**2))
#     return max(0, 1 - distance / self.simulator.light_radius)
#
#   def update(self):
#     left_sensor_x, left_sensor_y, right_sensor_x, right_sensor_y = self.get_sensor_positions()
#     left_light_intensity = self.get_light_intensity(left_sensor_x, left_sensor_y)
#     right_light_intensity = self.get_light_intensity(right_sensor_x, right_sensor_y)
#     light_difference = right_light_intensity - left_light_intensity
#
#     # Braitenberg Vehicle control (modify for aggressor/fearful)
#     if self.is_aggressor:
#       left_speed = right_light_intensity
#       right_speed = left_light_intensity
#     else:
#       left_speed = left_light_intensity
#       right_speed = right_light_intensity
#
#     new_heading = self.heading + self.rotation_factor * (right_speed - left_speed)
#     self.heading = np.mod(new_heading, 2*np.pi)
#
#     dx = self.speed * np.cos(self.heading)
#     dy = self.speed * np.sin(self.heading)
#     self.x, self.y = self.torus.wrap_position(self.x + dx, self.y + dy)
#
# class Simulator:
#   def __init__(self, width, height, light_source, light_radius):
#     self.torus = Torus(width, height)  # Create a Torus instance
#     self.light_source = light_source
#     self.light_radius = light_radius
#     self.robots = []
#
#   def add_robot(self, robot):
#     self.robots.append(robot)
#
#   def update(self):
#     for robot in self.robots:
#       robot.update()  # Call the update method of each robot
#
#     def visualize(self):
#         plt.figure(figsize=(8, 6))
#         light_intensity_field = np.zeros((self.torus.width, self.torus.height))
#         for x in range(self.torus.width):
#             for y in range(self.torus.height):
#                 light_intensity_field[x, y] = self.get_light_intensity(x, y)
#             plt.imshow(light_intensity_field, cmap='Greys', extent=(0, self.torus.width, 0, self.torus.height), alpha=0.3)
#         for robot in self.robots:
#             plt.plot(robot.x, robot.y)
#
# # Example Usage (modified)
# simulator = Simulator(width=50, height=50, light_source=(25, 25), light_radius=20)
# torus = simulator.torus  # Get the Torus instance from the Simulator
#
# # Aggressor Robot
# robot1 = Robot(torus, 10, 10, np.pi / 2, 1, 2, np.pi / 6, is_aggressor=True)
# simulator.add_robot(robot1)
#
# # Fearful Robot
# robot2 = Robot(torus, 40, 40, 3 * np.pi / 2, 1, 2, np.pi / 6, is_aggressor=False)
# simulator.add_robot(robot2)
#
# # Run the simulation for 100 steps (unchanged)
# # Visualize the results (unchanged)
#
# # Run the simulation for 100 steps
# for _ in range(100):
#   simulator.update()
#
# # Visualize the results
# simulator.visualize()
# plt.show()

'''TASK -- 1 '''
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # class Simulator:
# #     def __init__(self, square_size, wall_thickness):
# #         self.square_size = square_size
# #         self.wall_thickness = wall_thickness
# #         self.robot_size = 1  # Size of the robot (assumed to be a point)
# #
# #     def detect_obstacle(self, position):
# #         # Check if position is within the bounds of the square
# #         if position[0] < self.wall_thickness or position[0] > self.square_size - self.wall_thickness \
# #                 or position[1] < self.wall_thickness or position[1] > self.square_size - self.wall_thickness:
# #             return True  # Wall detected
# #
# #         # Check if position is within inner walls
# #         if position[0] > self.square_size / 3 and position[0] < 2 * self.square_size / 3 \
# #                 and position[1] > self.square_size / 3 and position[1] < 2 * self.square_size / 3:
# #             return True  # Inner wall detected
# #
# #         return False
# #
# #     def update_position(self, position, heading, speed):
# #         # Update position based on heading and speed
# #         dx = speed * np.cos(heading)
# #         dy = speed * np.sin(heading)
# #         new_position = position + np.array([dx, dy])
# #
# #         # Ensure the robot doesn't pass through walls
# #         if not self.detect_obstacle(new_position):
# #             return new_position
# #         else:
# #             return position
# #
# #
# # class ProximitySensors:
# #     def __init__(self, simulator, robot_position, robot_heading, sensor_range):
# #         self.simulator = simulator
# #         self.robot_position = np.array(robot_position)
# #         self.robot_heading = robot_heading
# #         self.sensor_range = sensor_range
# #
# #     def detect(self):
# #         # Calculate positions of sensors
# #         sensor_offsets = [np.array([np.cos(self.robot_heading + np.pi / 4),
# #                                     np.sin(self.robot_heading + np.pi / 4)]),  # Front-left sensor
# #                           np.array([np.cos(self.robot_heading),
# #                                     np.sin(self.robot_heading)]),  # Front sensor
# #                           np.array([np.cos(self.robot_heading - np.pi / 4),
# #                                     np.sin(self.robot_heading - np.pi / 4)])]  # Front-right sensor
# #
# #         sensor_positions = [self.robot_position + offset * self.sensor_range for offset in sensor_offsets]
# #
# #         # Detect obstacles
# #         obstacles_detected = [self.simulator.detect_obstacle(position) for position in sensor_positions]
# #
# #         # Calculate sensor readings
# #         sensor_readings = [1 - np.linalg.norm(sensor_positions[i] - self.robot_position) / self.sensor_range
# #                            if obstacles_detected[i] else 0 for i in range(3)]
# #
# #         return sensor_readings
# #
# #
# # class SimpleController:
# #     def __init__(self, proximity_sensors):
# #         self.proximity_sensors = proximity_sensors
# #
# #     def control(self):
# #         # Read sensor data
# #         sensor_readings = self.proximity_sensors.detect()
# #
# #         # Define control rules
# #         if sensor_readings[0] > 0.5:  # If obstacle detected by front-left sensor
# #             new_heading = self.proximity_sensors.robot_heading + np.pi / 4  # Turn right
# #         elif sensor_readings[1] > 0.5:  # If obstacle detected by front sensor
# #             new_heading = self.proximity_sensors.robot_heading - np.pi / 4  # Turn left
# #         elif sensor_readings[2] > 0.5:  # If obstacle detected by front-right sensor
# #             new_heading = self.proximity_sensors.robot_heading + np.pi / 4  # Turn right
# #         else:
# #             new_heading = self.proximity_sensors.robot_heading  # Continue straight
# #
# #         return new_heading
# #
# #
# # # Test the implementation
# # simulator = Simulator(square_size=20, wall_thickness=2)
# # initial_position = [10, 10]
# # initial_heading = np.pi / 4
# # sensor_range = 3
# #
# # proximity_sensors = ProximitySensors(simulator, initial_position, initial_heading, sensor_range)
# # controller = SimpleController(proximity_sensors)
# #
# # trajectory = [initial_position.copy()]
# # heading = initial_heading
# #
# # for _ in range(100):
# #     heading = controller.control()
# #     new_position = simulator.update_position(initial_position, heading, 0.1)
# #     trajectory.append(new_position)
# #     initial_position = new_position
# #
# # # Plot trajectory
# # trajectory = np.array(trajectory)
# # plt.plot(trajectory[:, 0], trajectory[:, 1])
# # plt.xlabel('X')
# # plt.ylabel('Y')
# # plt.title('Trajectory of Robot with Proximity Sensors')
# # plt.show()
