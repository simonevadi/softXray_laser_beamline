from raypyng import Simulate
import numpy as np
import os

from helper_functions import extract_param_from_csv, delete_round_folders
from parameter import param_dict, nrays, rounds, ncpu

for rml_file_name, csv_file in param_dict.items():

    # work out absolute path of rml file
    rml_file_path = os.path.join('rml', rml_file_name)
    csv_file_path = os.path.join('param', csv_file)

    sim = Simulate(rml_file_path, hide=True)

    beamline = sim.rml.beamline

    # cpu


    # name for simulation folder
    sim_name = rml_file_name


    # extract params from csv file
    tg_exit_arm_mer, tg_exit_arm_sag, slit_distance, energy = extract_param_from_csv(csv_file_path)

    # define a list of dictionaries with the parameters to scan
    params = [  
                
                {beamline.PointSource.photonEnergy:energy,
                beamline.ToroidalGrating.exitArmLengthSag:tg_exit_arm_sag,
                beamline.ToroidalGrating.exitArmLengthMer:tg_exit_arm_mer, 
                beamline.Slit.distancePreceding:slit_distance},
                
                {beamline.PointSource.numberRays:nrays}
            ]

    #and then plug them into the Simulation class
    sim.params=params

    # sim.simulation_folder = '/home/simone/Documents/RAYPYNG/raypyng/test'
    sim.simulation_name = sim_name

    # turn off reflectivity
    sim.reflectivity(reflectivity=False)

    # repeat the simulations as many time as needed
    sim.repeat = rounds

    sim.analyze = False # don't let RAY-UI analyze the results
    sim.raypyng_analysis=True # let raypyng analyze the results

    ## This must be a list of dictionaries
    sim.exports  =  [
        {beamline.Slit:['RawRaysOutgoing']}
        ]


    # create the rml files
    #sim.rml_list()

    #uncomment to run the simulations
    sim.run(multiprocessing=ncpu, force=False)
    delete_round_folders('RAYPy_Simulation_'+sim_name)