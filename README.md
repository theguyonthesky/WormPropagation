# Worm Propagation Simulation

## Overview
This repository contains two Python scripts, `rndm.py` and `l_p_s.py`, for simulating worm propagation based on different scanning techniques: random scan (`rndm.py`) and local preference scan (`l_p_s.py`).

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## Features
- Simulates the propagation of a computer worm through a network.
- Utilizes different scanning techniques for infection.
- Provides the ability to plot the simulation runs using Matplotlib.

## How to Run
1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/worm-propagation.git
    ```

2. Navigate to the folder
    ```bash
    cd worm-propagation
    ```

3. Run `rndm.py` for a simulation based on random scan or run `l_p_s.py` for a simulation based on local preference.
    ```bash
    python rndm.py
    ```
    or
    ```bash
    python l_p_s.py
    ```

## Understanding the Code
- `initip()`: Initializes the IP address states ('immune' or 'vulnerable').
- `getlocip(addressstip)`: Determines IPs to scan based on local preference.
- `worm_propagation(addressstip, mainMethod)`: Simulates worm propagation.
- `plotsim(count, run)`: Plots the simulation run.
- `worm_propagation_simulation(mainMethod, plot)`: Runs the simulation.

## Contributing
Feel free to fork this repository, make changes, and submit pull requests.

## License
MIT License
