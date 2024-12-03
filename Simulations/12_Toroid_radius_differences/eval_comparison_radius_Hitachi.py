import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from helper_lib import delete_round_folders


# import simulation parameters
from parameter import energy
from parameter import SlitSize
from parameter import rml_file_name_Laser_Shimadzu_35, rml_file_name_Laser_Shimadzu_42, rml_file_name_Laser_Shimadzu_45
from parameter import rml_file_name_Laser_Hitachi_35, rml_file_name_Laser_Hitachi_42, rml_file_name_Laser_Hitachi_45
from parameter import colors
#from parameter import grating

from raypyng.postprocessing import PostProcessAnalyzed
p = PostProcessAnalyzed()
moving_average = p.moving_average

SlitSize = SlitSize*1000
rml_comparison_list = {}
#rml_comparison_list[rml_file_name_Laser_Shimadzu_35] = 0
#rml_comparison_list[rml_file_name_Laser_Shimadzu_42] = 0
#rml_comparison_list[rml_file_name_Laser_Shimadzu_45] = 0
rml_comparison_list[rml_file_name_Laser_Hitachi_35] = 0
rml_comparison_list[rml_file_name_Laser_Hitachi_42] = 0
rml_comparison_list[rml_file_name_Laser_Hitachi_45] = 0

# set moving average window
window = 1

# prepare figures
fig, (axs) = plt.subplots(3, 2,figsize=(10,10))
fig.suptitle(f"MetrokX-BL grating (1200 L/mm) comparison Hitachi (blazed) vs. Shimadzu (laminar)")


# HORIZONTAL FOCUS
hf_ax = axs[2,0]
hf_ax.set_xlabel('Energy [eV]')
hf_ax.set_ylabel('Focus Size [um]')
hf_ax.set_title('Horizontal Focus')

# VERTICAL FOCUS
vf_ax = axs[2,1]
vf_ax.set_xlabel('Energy [eV]')
vf_ax.set_ylabel('Focus Size [um]')
vf_ax.set_title('Vertical Focus')    
# vf_ax.set_ylim(6000, 10500)

color_index = -1
for rml_file_name, ind in rml_comparison_list.items():
    color_index += 1
    # file/folder/ml index definition
    rp_simulation_folder = 'RAYPy_Simulation_' + rml_file_name + '_RP'

    # load RP simulations results
    folder_name = rp_simulation_folder
    oe = 'CamInput'
    rp_path = os.path.join(rp_simulation_folder, oe + '_RawRaysOutgoing.dat')
    rp = pd.read_csv(rp_path, sep='\t', index_col=None)
    en_rp_path = os.path.join(rp_simulation_folder, 'input_param_Laser_photonEnergy.dat')
    energy_rp = np.loadtxt(en_rp_path)
    ssrp = energy_rp.shape[0]

    energy_rp = moving_average(energy_rp, window)

    # HORIZONTAL FOCUS
    hor_foc = rp['HorizontalFocusFWHM'][ssrp * ind:ssrp * (ind + 1)]
    hor_foc = moving_average(hor_foc.to_numpy(), window)
    hf_ax.plot(energy_rp, 1000 * hor_foc, colors[color_index])

    # VERTICAL FOCUS
    ver_foc = rp['VerticalFocusFWHM'][ssrp * ind:ssrp * (ind + 1)]
    ver_foc = moving_average(ver_foc.to_numpy(), window)
    vf_ax.plot(energy_rp, 1000 * ver_foc, colors[color_index], label=f'{rml_file_name}')

# Add legends
#hf_ax.legend(title="Horizontal Focus")
vf_ax.legend(title="Vertical Focus")


# delete round folders

#sim_name = rml_file_name+'_FLUX'
sim_name = rml_file_name+'_RP'

delete_round_folders('RAYPy_Simulation_'+sim_name)


# Create a folder for the evaluation plots
if not os.path.exists('plot'):
    os.makedirs('plot')

# Plot and save

plt.tight_layout()
plt.savefig('plot/MetrokX-BL Toroid sagittal radius comparison Hitachi grating.pdf')
