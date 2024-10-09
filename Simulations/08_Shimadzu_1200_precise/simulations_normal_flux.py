from raypyng import Simulate
import numpy as np
import os

from helper_functions import delete_round_folders

from parameter_normal import nrays, rounds, ncpu
from parameter_normal import energy, SlitSize, lin_polarization
from parameter_normal import rml_file_name_Laser_BL_Shimadzu as rml_file_name
#from parameter import lin_polarization


# work out absolute path of rml file
rml_file_path = os.path.join('rml', rml_file_name+'.rml')

sim = Simulate(rml_file_path, hide=True)

beamline = sim.rml.beamline


# name for simulation folder
sim_name = rml_file_name+'_FLUX'

# define a list of dictionaries with the parameters to scan
# and plug them into the Simulation class

sim.params = [              
            {beamline.ExitSlit.openingHeight:SlitSize},
            {beamline.Laser.photonEnergy:energy},
            {beamline.Laser.numberRays:nrays},
            {beamline.Laser.linearPol_0:lin_polarization}
        ]

# sim.simulation_folder = '/home/simone/Documents/RAYPYNG/raypyng/test'
sim.simulation_name = sim_name

# turn off reflectivity
sim.reflectivity(reflectivity=True)

# repeat the simulations as many time as needed
sim.repeat = rounds

sim.analyze = False # don't let RAY-UI analyze the results
sim.raypyng_analysis=True # let raypyng analyze the results

## This must be a list of dictionaries
sim.exports  =  [
    {beamline.CamInput:['RawRaysOutgoing']}
    ]


# create the rml files
#sim.rml_list()

#uncomment to run the simulations
sim.run(multiprocessing=ncpu, force=False)
# delete_round_folders('RAYPy_Simulation_'+sim_name)