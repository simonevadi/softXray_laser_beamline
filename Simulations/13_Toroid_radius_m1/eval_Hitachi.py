import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# path to xrt:
import os, sys; sys.path.append(os.path.join('..', '..', '..'))  # analysis:ignore
import xrt.backends.raycing.materials as rm


# from helper library
from helper_lib import get_reflectivity
from helper_lib import scale_undulator_flux, order

# import simulation parameters
from parameter import energy
from parameter import SlitSize
from parameter import rml_file_name_Laser_Hitachi_45 as rml_file_name
from parameter import colors
#from parameter import lin_polarization



# file/folder/ml index definition
rp_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_RP'



# load RP simulations results
folder_name  = rp_simulation_folder
oe           = 'CamInput'
rp_path      = os.path.join(rp_simulation_folder, oe+'_RawRaysOutgoing.csv')
rp           = pd.read_csv(rp_path, sep=',')
en_rp_path   = os.path.join(rp_simulation_folder, 'input_param_Laser_photonEnergy.dat')
m1 = rp['M1.shortRadius']

########################################
# plotting Flux and RP

fig, (axs) = plt.subplots(1, 2,figsize=(10,10))
fig.suptitle(f"{rml_file_name}")


# HORIZONTAL FOCUS
ax = axs[0]
ax.plot(m1,1000*rp['HorizontalFocusFWHM'])

ax.set_xlabel('Energy [eV]')
ax.set_ylabel('Focus Size [um]')
ax.set_title('Horizontal Focus')
ax.legend()

# # VERTICAL FOCUS
ax = axs[1]
ax.plot(m1,1000*rp['VerticalFocusFWHM'])

ax.set_xlabel('Energy [eV]')
ax.set_ylabel('Focus Size [um]')
ax.set_title('Vertical Focus')

plt.tight_layout()
plt.savefig(f'plot/'+rml_file_name+'_m1.pdf')

# plt.show()