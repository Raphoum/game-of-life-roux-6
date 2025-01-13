import numpy as np
import time
import os

def clear_console():
    """Clears the console output."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    """Prints the grid to the console."""
    for row in grid:
        print("".join('█' if cell else ' ' for cell in row))

def create_grid(rows, cols, randomize=True):
    """Creates a grid of the specified size.

    Args:
        rows (int): Number of rows.
        cols (int): Number of columns.
        randomize (bool): If True, initialize the grid with random values.

    Returns:
        numpy.ndarray: The initialized grid.
    """
    if randomize:
        return np.random.choice([0, 1], size=(rows, cols))
    return np.zeros((rows, cols), dtype=int)

def update_grid(grid):
    """Updates the grid according to the rules of Conway's Game of Life.

    Args:
        grid (numpy.ndarray): The current grid.

    Returns:
        numpy.ndarray: The updated grid.
    """
    rows, cols = grid.shape
    new_grid = np.copy(grid)

    for row in range(rows):
        for col in range(cols):
            # Count live neighbors
            live_neighbors = sum(
                grid[i, j]
                for i in range(row - 1, row + 2)
                for j in range(col - 1, col + 2)
                if (0 <= i < rows and 0 <= j < cols and (i != row or j != col))
            )

            # Apply the rules of the Game of Life
            if grid[row, col] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = 0
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[row, col] = 1

    return new_grid

def main():
    """Runs the Game of Life simulation."""
    rows, cols = 20, 40  # Size of the grid
    grid = create_grid(rows, cols)

    try:
        while True:
            clear_console()
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.3)  # Adjust speed here
    except KeyboardInterrupt:
        print("\nSimulation terminated.")

if __name__ == "__main__":
    main()
