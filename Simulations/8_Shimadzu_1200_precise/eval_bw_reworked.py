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
from parameter_bw import energy
from parameter_bw import SlitSize
from parameter_bw import rml_file_name_Laser_BL_Shimadzu_bw as rml_file_name
from parameter_bw import colors
#from parameter import lin_polarization



# file/folder/ml index definition
flux_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_FLUX'
rp_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_RP'



folder_name = flux_simulation_folder
all_rays = []  # Create an empty list to store all the data

for r in range(0, 12):
    round_folder = f'round_{r}'
    filepath = os.path.join(folder_name, round_folder, '0_CamInput-RawRaysOutgoing.csv')
    
    # Read the CSV file, skipping the first two header lines
    rays = pd.read_csv(filepath,sep='\t', skiprows=1)
    
    # Append the data to the list
    all_rays.append(rays)

# Optionally, concatenate all data into a single DataFrame
combined_rays = pd.concat(all_rays, ignore_index=True)
combined_rays = combined_rays.sort_values(by='CamInput_EN')

energy_step = 1
# Define the bin edges with a 1 eV range
bins = np.arange(combined_rays['CamInput_EN'].min(), combined_rays['CamInput_EN'].max() + energy_step, energy_step)

# Use numpy to calculate the histogram values (frequencies) for the 1 eV bins
flux, bin_edges = np.histogram(combined_rays['CamInput_EN'], bins=bins)

# Calculate the center of each bin for plotting purposes
energy_flux = (bin_edges[:-1] + bin_edges[1:]) / 2



# load RP simulations results
folder_name  = rp_simulation_folder
all_rays = []  # Create an empty list to store all the data

for r in range(0, 12):
    round_folder = f'round_{r}'
    filepath = os.path.join(folder_name, round_folder, '0_CamInput-RawRaysOutgoing.csv')
    
    # Read the CSV file, skipping the first two header lines
    rays = pd.read_csv(filepath,sep='\t', skiprows=1)
    
    # Append the data to the list
    all_rays.append(rays)

# Optionally, concatenate all data into a single DataFrame
combined_rays = pd.concat(all_rays, ignore_index=True)
combined_rays = combined_rays.sort_values(by='CamInput_OY')


pixel_size = 0.018
# Define the bin edges with the pixel size
bins = np.arange(combined_rays['CamInput_OY'].min(), combined_rays['CamInput_OY'].max() + pixel_size, pixel_size)

# Bin the CamInput_DY column based on the defined bin edges
combined_rays['OY_bin'] = pd.cut(combined_rays['CamInput_OY'], bins=bins)

# Group by the binned 'DY_bin' column and calculate the mean of 'CamInput_EN' for each bin
energy_bw = combined_rays.groupby('OY_bin')['CamInput_EN'].mean()

# Group by the binned 'DY_bin' column and calculate the max and min of 'CamInput_EN' for each bin
energy_max_per_bin = combined_rays.groupby('OY_bin')['CamInput_EN'].max()
energy_min_per_bin = combined_rays.groupby('OY_bin')['CamInput_EN'].min()

# Calculate the bandwidth (max - min) for each bin
bw = energy_max_per_bin - energy_min_per_bin
# Calculate the centers of each bin for plotting
position_on_camera = (bins[:-1] + bins[1:]) / 2



# ########################################
# # plotting Flux and RP

fig, (axs) = plt.subplots(2, 2,figsize=(10,10))
fig.suptitle(f"{rml_file_name}")


# # MIRROR COATING
# table = 'Henke'
# incident_angle = 2
# E   = np.arange(40, 600, 1)
# Au  = rm.Material('Au',  rho=19.3, kind='mirror',table=table)
# Pt  = rm.Material('Pt',  rho=21.45, kind='mirror',table=table)
# # C   = rm.Material('C',   rho=2.2, kind='mirror',table=table)
# Ni  = rm.Material('Ni',  rho=8.91, kind='mirror',table=table)

# Au_r, _ = get_reflectivity(Au, E=E, theta=incident_angle)
# Pt_r, _ = get_reflectivity(Pt, E=E, theta=incident_angle)
# # C_r, _  = get_reflectivity(C, E=E, theta=incident_angle)
# Ni_r, _ = get_reflectivity(Ni, E=E, theta=incident_angle)

# ax2=axs[0,0]
# ax2.set_xlabel('Energy [eV]')
# ax2.set_ylabel('Reflectivity [a.u.]')
# ax2.set_title('Mirror Coating Reflectivity')
# ax2.plot(E, Au_r, label='Au')
# ax2.plot(E, Pt_r, label='Pt')
# # ax2.plot(E, C_r, label='C')
# ax2.plot(E, Ni_r, label='Ni')
# ax2.legend()



# BEAMLINE TRANSMISSION
ax = axs[0,1]
ax.plot(energy_flux,flux )

ax.set_xlabel(r'Energy [eV]')
ax.set_ylabel('Transmission [%]')
ax.set_title('Available Flux [in transmitted bandwidth]')
ax.grid(which='both', axis='both')
# ax.legend()



# BANDWIDTH
ax = axs[1,0]

ax.plot(energy_bw, bw)#,label=f'{varying_var_n} {es} {varying_var_unit}')


ax.set_xlabel('Energy [eV]')
ax.set_ylabel('Transmitted Bandwidth [meV]')
ax.set_title('Transmitted Bandwidth (tbw)')
ax.grid(which='both', axis='both')
# ax.set_yscale('log')
ax.legend()


# # RESOLVING POWER
ax = axs[1,1]

ax.plot(energy_bw, energy_bw/bw)#,label=f'{varying_var_n} {es} {varying_var_unit}')

ax.set_xlabel('Energy [eV]')
ax.set_ylabel('RP [a.u.]')
ax.set_title('Resolving Power')
ax.grid(which='both', axis='both')
ax.legend()


plt.tight_layout()
plt.savefig('plot/FluxRpFocus'+rml_file_name+'BW'+'_reworked.pdf')

plt.show()