import numpy as np
import pandas as pd

#### XRT
def get_reflectivity(material,E,theta):
    """Calculate the reflectivity for a given material at
    a certain incident angle theta for a given energy range E

    Args:
        material (XRT material): A material defined in XRT
        E (np.array): the desidered energy range
        theta (float): the grazing incidence angle

    Returns:
        rs,rp: reflectivity fr the s and p polarization
    """    
    theta = np.deg2rad(theta)
    rs, rp = material.get_amplitude(E, np.sin(theta))[0:2]
    return abs(rs)**2, abs(rp)**2


### UNDULATOR
def scale_undulator_flux(ray_energy, ray_flux, undulator_file):
    """Takes as input the flux points in percentage at defined energy points and
    returns the absolute flux. Performs interpolation if needed.

    Args:
        ray_energy (np.array): array of energy
        ray_flux (np.array): array of flux
        undulator_file (str): the filename and location of the undulator flux file

    Returns:
        absolute_flux (np.array): the absolute flux
    """    
    undulator       = np.loadtxt(undulator_file,skiprows=8)
    en_undulator    = undulator[:,0]
    flux_undulator  = undulator[:,3]
    und_interp_flux = np.interp(ray_energy, en_undulator, flux_undulator) 

    return ray_flux*und_interp_flux/100 

def order(unordered):
    ordered = []
    for i in range(5):
        for v in range(10):
            ordered.append(unordered[int(i+v*5)])
    return np.array(ordered)


import os
import shutil

def delete_round_folders(directory):
    """
    Deletes subdirectories within a specified directory that match the pattern 'round*'.

    This function iterates over each item in the specified directory. If an item is a directory and its name
    starts with "round", the function deletes it along with all its contents. If the specified directory does
    not exist, it prints an error message and terminates the operation without any modification.

    Args:
        directory (str): The path to the directory where subdirectories beginning with "round" will be deleted.

    Returns:
        None: This function does not return anything but prints messages about the directories it deletes
              or if the main directory does not exist.

    Raises:
        OSError: If there are issues accessing the directory or removing subdirectories, such as
                 permission issues, this function will raise an OSError.

    Example:
        >>> delete_round_folders("/path/to/directory")
        Directory not found: /path/to/directory
        Deleted: /path/to/directory/round1
    """
    # Check if the provided directory exists
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    # Loop through each item in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Check if the item is a directory and matches the 'round*' pattern
        if os.path.isdir(item_path) and item.startswith("round"):
            # Remove the directory and all its contents
            shutil.rmtree(item_path)
            print(f"Deleted: {item_path}")
        
# Example usage:
# Replace '/path/to/folder' with the path to the directory where you want to delete the subfolders
# delete_round_folders('/path/to/folder')

