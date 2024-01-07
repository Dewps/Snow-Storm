# Snow-Storm
-
Snow Storm Simulation
## Created By Dewps

This is a Python program that simulates snowfall in the terminal. It uses ASCII characters to represent snowflakes and creates a grid-like animation effect.
-

Requirements:
 Python 3.x

-
Usage:
 Open a terminal or command prompt.
 Navigate to the directory where the code file is located.
 Run the following command to execute the program:
  python snow_storm.py

Note: The program will run until you press Ctrl+C or close the terminal window.
-

Explanation:

 The program starts by importing necessary modules: os, random, and time.
 Constants SNOW_DENSITY, SNOW_DELAY, and SNOW_FLAKES are defined. These variables control the density, delay, and appearance of snowflakes, respectively.
 The terminal size is obtained using os.get_terminal_size() and stored in the variables w and h representing the width and height of the terminal.
 An empty grid is created using a nested list comprehension. Each cell in the grid is represented by a space character.
 The function draw_grid() is defined to clear the terminal, construct the output string from the grid, and print the output.
 The main loop starts with an infinite loop (while True) to continuously update and display the snowfall animation.
 Inside the loop, a new row is created by randomly selecting snowflakes or empty spaces based on the SNOW_DENSITY value.
 The new row is inserted at the top of the grid using grid.insert(0, row), and the last row is removed using grid.pop() to maintain a fixed grid height.
 The draw_grid() function is called to update the terminal display with the latest grid.
 A delay is introduced using time.sleep(SNOW_DELAY) to control the speed of the animation.

Note: The os.system('cls' if os.name == 'nt' else 'clear') line is used to clear the terminal screen. It uses different commands (cls for Windows and clear for Unix-like systems) based on the os.name value.
