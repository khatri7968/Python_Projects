import pygame
import numpy as np

# Parameters
GRID_SIZE = 100
CELL_SIZE = 5
NUM_COLORS = 5
COLOR_SCHEME = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
SPEED = 10

# Initialize the grid
grid = np.random.randint(0, NUM_COLORS, size=(GRID_SIZE, GRID_SIZE))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))

# Update function
def update(grid):
    new_grid = np.copy(grid)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            neighbors = []

            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    ni = (i + x) % GRID_SIZE
                    nj = (j + y) % GRID_SIZE

                    neighbors.append(grid[ni, nj])

            new_grid[i, j] = (grid[i, j] + np.random.choice(neighbors)) % NUM_COLORS

    return new_grid

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = update(grid)

    # Draw the grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = COLOR_SCHEME[grid[i, j]]
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()
