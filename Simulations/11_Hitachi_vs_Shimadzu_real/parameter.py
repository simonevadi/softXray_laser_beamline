import numpy as np

nrays    = 1e5
rounds   = 10
ncpu     = 8

SlitSize = np.array([0.14])
energy = np.arange(40,200,1)


rml_file_name_Laser_Shimadzu  = 'Laser_Shimadzu_1200_laminar_real'
rml_file_name_Laser_Hitachi   = 'Laser_Hitachi_1200_blazed_real'


### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]