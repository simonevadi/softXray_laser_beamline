
# Running the Simulations
This will work under Linux, and probably also under MacOS. It can not be run in Windows.

## Install RAY-UI and RayPyNG
Install RAY-UI using one of these [installers](https://github.com/hz-b/ray-installers/releases/tag/1.159). Then follow [these instructions](https://raypyng.readthedocs.io/en/latest/installation.html) to install RayPyNG.

## Files Description
| File |Description     |
|---------------------|------------------|
| `simulations.py`    | Contains the code running the simulations. |
| `helper_functions.py` | Contains a couple of functions: one to extract parameters from the CSV files and another to calculate the resolving power.|
| `parameter.py`      | Contains the parameters to run the simulations, including a dictionary that contains the RML file names as keys and corresponding CSV files holding the values. |
| `eval.py`           | Contains the code for the evaluation. |


## Running the Simulation
To run the simulation, navigate to your project directory in a terminal or command prompt and execute:
```bash
python simulations.py
```

This will start the simulation process based on the parameters defined in `param_dict` and adjusted through the CSV files specified. The script is configured to run multiple simulations using multiprocessing, based on the number of CPUs specified in `parameter.py`. Adjust this parameter accordingly to the number of cpu of you machine, and the expected RAM usage. If you have no idea, start low and increase it monitoring the RAM. 

## Customization
To modify simulation parameters or adjust the behavior, edit the `parameter.py. In particular you can add the rml and csv files couples. 

## Running the Evaluation
Once all the simulations runned execute:
```bash
python eval.py
```
This script plots the transmitted bandwidth and the resolving power for rml file. 
