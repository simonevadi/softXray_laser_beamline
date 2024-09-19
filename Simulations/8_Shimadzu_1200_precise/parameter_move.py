import numpy as np

nrays    = 1e5
rounds   = 3
ncpu     = 12

SlitSize = np.array([0.14])
energy = np.arange(40,180,2)
SlitSizeCam = np.array([0.018])   #Pixel size of the cam 
Ydirection = np.arange(-40,40,2)  #last value is the pixel size of CCD, Step in mm


rml_file_name_Laser_BL_Shimadzu_move = 'Laser_BL_Shimadzu_1200_Foil_move'


### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]