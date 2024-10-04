import numpy as np

nrays    = 1e5
rounds   = 1400
ncpu     = 10

SlitSize = np.array([0.14])
energy   = np.array([120])
energySpread = np.array([160])      #means half the value arround the set energy
lin_polarization = np.array([1])


rml_file_name_Laser_BL              = 'Laser_Shimadzu_Hitachi_1200'
rml_file_name_Laser_BL_Kapillare    = 'Laser_Shimadzu_Hitachi_1200_Kapillare'


### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]