import pandas as pd
import numpy as np
import os
import shutil

def delete_round_folders(directory):
    """
    Delete all folders in the specified directory that are named with a "round" pattern.

    This function assumes folders to be deleted follow a naming convention like 'round1', 'round2', etc.

    Args:
        directory (str): The path to the directory where folders are to be deleted.

    Raises:
        FileNotFoundError: If the specified directory does not exist.

    Returns:
        None: This function does not return any value, it performs a deletion operation.
    """
    # Check if the provided directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    # List all items in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Check if the item is a directory and matches the 'round' naming pattern
        if os.path.isdir(item_path) and item.startswith('round'):
            # Remove the directory
            shutil.rmtree(item_path)
            print(f"Deleted folder: {item_path}")
            
def extract_param_from_csv(path_to_csv):
    """
    Extract simulation parameters from a CSV file and return them as separate numpy arrays.

    Args:
        path_to_csv (str): The file path to the CSV file containing the simulation parameters.

    Returns:
        tuple: A tuple containing four numpy arrays:
            - tg_exit_arm_mer (np.ndarray): Meridional exit arm lengths.
            - tg_exit_arm_sag (np.ndarray): Sagittal exit arm lengths.
            - slit_distance (np.ndarray): Distances of the slit.
            - energy (np.ndarray): Photon energy values.

    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path_to_csv)
    # Rename the columns to simplify access
    df = df.rename(columns={
        'Point Source-Photon Energy / eV': 'energy',
        'Toroidal Grating-Exit arm length (sagittal, x-y) / mm': 'tg_exit_arm_sag',
        'Toroidal Grating-Exit arm length (meridional, y-z) / mm': 'tg_exit_arm_mer',
        'Slit-Distance / mm': 'slit_distance'
    })

    # Extract parameters as numpy arrays
    tg_exit_arm_sag = df['tg_exit_arm_sag'].to_numpy()
    tg_exit_arm_mer = df['tg_exit_arm_mer'].to_numpy()
    slit_distance   = df['slit_distance'].to_numpy()
    energy          = df['energy'].to_numpy()
    
    return tg_exit_arm_mer, tg_exit_arm_sag, slit_distance, energy

def calculate_resolving_power(bandwidth, energy):
    """
    Calculate the resolving power of an instrument given bandwidth and energy.

    Args:
        bandwidth (np.ndarray): The bandwidth values, which must not be zero for calculation.
        energy (np.ndarray): The energy values at which resolving power is calculated.

    Returns:
        np.ndarray: The calculated resolving power.

    Raises:
        ZeroDivisionError: An error is raised when the bandwidth includes zero values, as division by zero is not permitted.

    """
    try:
        resolving_power = energy / bandwidth
    except ZeroDivisionError:
        resolving_power = 0  # Set resolving power to zero in case of division by zero
    inf_indices = np.where(np.isinf(bandwidth))[0]
    if len(inf_indices) > 0:
        print(f"You have zero bandwidth starting at E={energy[inf_indices[0]]} eV.")
    return resolving_power
