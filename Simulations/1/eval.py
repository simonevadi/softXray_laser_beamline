import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from parameter import param_dict
from helper_functions import calculate_resolving_power

for rml_file_name in param_dict.keys():

    # file/folder/ml index definition
    simulation_folder = 'RAYPy_Simulation_'+rml_file_name

    # load RP simulations results
    oe           = 'Slit'
    rp_path      = os.path.join(simulation_folder, oe+'_RawRaysOutgoing.dat')
    rp           = pd.read_csv(rp_path, sep='\t')
    en_path      = os.path.join(simulation_folder, 'input_param_PointSource_photonEnergy.dat')
    energy    = np.loadtxt(en_path)



    ########################################
    # plotting Flux and RP

    fig, (axs) = plt.subplots(2, 1,figsize=(10,10))
    fig.suptitle(f"{rml_file_name}")

    # BANDWIDTH
    ax = axs[0]

    ax.plot(energy,1000*rp['Bandwidth'])#,label=f'{varying_var_n} {es} {varying_var_unit}')


    ax.set_xlabel('Energy [eV]')
    ax.set_ylabel('Transmitted Bandwidth [meV]')
    ax.set_title('Transmitted bandwidth (tbw)')
    ax.grid(which='both', axis='both')


    # RESOLVING POWER
    ax = axs[1]

    resolving_power = calculate_resolving_power(rp['Bandwidth'], energy)
    ax.plot(energy, resolving_power)

    ax.set_xlabel('Energy [eV]')
    ax.set_ylabel('RP [a.u.]')
    ax.set_title('Resolving Power')
    ax.grid(which='both', axis='both')


    plt.tight_layout()
    plt.savefig(f'plot/FluxRpFocus_{rml_file_name}.png')

