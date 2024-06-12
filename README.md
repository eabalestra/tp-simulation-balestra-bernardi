# SIR Model Simulation

This project simulates the SIR (Susceptible, Infected, Removed) model of disease spread using two numerical methods: Euler and Heun. The simulation results are plotted and saved as a PNG image.

## Requirements

- Python
- pip

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Configuration

The simulation parameters are set in the `config.ini` file. Here is an example of how it should be configured:

```ini
[Simulation]
days = 20
beta = 0.0022
retired_rate = 0.4477
```

- `days`: Total number of days for the simulation.
- `beta`: Per-capita transmission rate of the disease.
- `retired_rate`: Removal rate (rate at which infected individuals recover or die).

## Usage

1. Run the main script:

```bash
python main.py
```

The script will run the SIR model simulation using both Euler and Heun methods, and then plot the results. The plot will be saved as `sir_model.png` in the project directory.

## Project Structure

- `methods/`: Contains the implementation of Euler and Heun methods.
- `utils/`: Contains utility functions for plotting and calculating derivatives.
- `config.ini`: Configuration file for the simulation parameters.
- `main.py`: The main script to run the simulation.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.