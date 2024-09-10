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
from parameter import rml_file_name
from parameter import colors
from parameter import lin_polarization



# file/folder/ml index definition
flux_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_FLUX'
rp_simulation_folder = 'RAYPy_Simulation_'+rml_file_name+'_RP'


SlitSize = SlitSize*1000
varying_var = lin_polarization
varying_var_n = 'Lin Pol'
varying_var_unit = ''

# load Flux simulations results
folder_name  = flux_simulation_folder
oe           = 'CamInput'
flux_path    = os.path.join(flux_simulation_folder, oe+'_RawRaysOutgoing.dat')
flux         = pd.read_csv(flux_path, sep='\t')
en_flux_path = os.path.join(flux_simulation_folder, 'input_param_Laser_photonEnergy.dat')
energy_flux  = np.loadtxt(en_flux_path)

# load RP simulations results
folder_name  = rp_simulation_folder
oe           = 'CamInput'
rp_path      = os.path.join(rp_simulation_folder, oe+'_RawRaysOutgoing.dat')
rp           = pd.read_csv(rp_path, sep='\t')
en_rp_path   = os.path.join(rp_simulation_folder, 'input_param_Laser_photonEnergy.dat')
energy_rp    = np.loadtxt(en_rp_path)



########################################
# plotting Flux and RP

fig, (axs) = plt.subplots(3, 2,figsize=(10,10))
fig.suptitle(f"{rml_file_name}")


# MIRROR COATING
table = 'Henke'
incident_angle = 2
E   = np.arange(40, 200, 1)
Au  = rm.Material('Au',  rho=19.3, kind='mirror',table=table)
Pt  = rm.Material('Pt',  rho=21.45, kind='mirror',table=table)
C   = rm.Material('Pt',  rho=2.2, kind='mirror',table=table)

Au_r, _ = get_reflectivity(Au, E=E, theta=incident_angle)
Pt_r, _ = get_reflectivity(Pt, E=E, theta=incident_angle)
C_r, _ = get_reflectivity(C, E=E, theta=incident_angle)

ax2=axs[0,0]
ax2.set_xlabel('Energy [eV]')
ax2.set_ylabel('Reflectivity [a.u.]')
ax2.set_title('Mirror Coating Reflectivity')
ax2.plot(E, Au_r, label='Au')
ax2.plot(E, Pt_r, label='Pt')
ax2.plot(E, C_r, label='C')
ax2.legend()



# BEAMLINE TRANSMISSION
ax = axs[0,1]

ss = energy_flux.shape[0]
ind=0
for ind, es in enumerate(varying_var):
    ax.plot(energy_flux,flux['PercentageRaysSurvived'][ss*ind:ss*(ind+1)], colors[ind], label=f'{varying_var_n} {es} {varying_var_unit}' )

ax.set_xlabel(r'Energy [eV]')
ax.set_ylabel('Transmission [%]')
ax.set_title('Available Flux [in transmitted bandwidth]')
ax.grid(which='both', axis='both')
ax.legend()



# BANDWIDTH
ax = axs[1,0]
ss = energy_rp.shape[0]

for ind, es in enumerate(varying_var):
    ax.plot(energy_rp,1000*rp['Bandwidth'][ss*ind:ss*(ind+1)],colors[ind])#,label=f'{varying_var_n} {es} {varying_var_unit}')


ax.set_xlabel('Energy [eV]')
ax.set_ylabel('Transmitted Bandwidth [meV]')
ax.set_title('Transmitted Bandwidth (tbw)')
ax.grid(which='both', axis='both')
# ax.set_yscale('log')
ax.legend()


# RESOLVING POWER
ax = axs[1,1]

# plot and deal with bandwidth=0 case.
for ind, es in enumerate(varying_var):
    try:
        res_p = energy_rp / rp['Bandwidth'][ss * ind:ss * (ind + 1)]
    except ZeroDivisionError:
        res_p = 0
    inf_indices = np.where(np.isinf(rp))[0]
    if len(inf_indices)>0:
        print(f"For {varying_var_n} size {ss}, you have zero bandwidth starting at E={energy_rp[inf_indices[0]]} eV.")
    ax.plot(energy_rp, res_p, colors[ind], label=f'{varying_var_n} {es} {varying_var_unit}')

ax.set_xlabel('Energy [eV]')
ax.set_ylabel('RP [a.u.]')
ax.set_title('Resolving Power')
ax.grid(which='both', axis='both')
ax.legend()

# HORIZONTAL FOCUS
ax = axs[2,0]
for ind, es in enumerate(varying_var):
    ax.plot(energy_rp,1000*rp['HorizontalFocusFWHM'][ss*ind:ss*(ind+1)],colors[ind],label=f'{varying_var_n} {es} {varying_var_unit}')

ax.set_xlabel('Energy [eV]')
ax.set_ylabel('Focus Size [um]')
ax.set_title('Horizontal Focus')
ax.legend()

# # VERTICAL FOCUS
ax = axs[2,1]
for ind, es in enumerate(varying_var):
    ax.plot(energy_rp,1000*rp['VerticalFocusFWHM'][ss*ind:ss*(ind+1)],colors[ind],label=f'{varying_var_n} {es} {varying_var_unit}')

ax.set_xlabel('Energy [eV]')
ax.set_ylabel('Focus Size [um]')
ax.set_title('Vertical Focus')

plt.tight_layout()
plt.savefig('plot/FluxRpFocus'+rml_file_name+'.png')

# plt.show()