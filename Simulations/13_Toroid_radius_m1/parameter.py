import numpy as np

nrays    = 1e5
rounds   = 5
ncpu     = 10

SlitSize  = np.array([0.12])
energy    = np.array([100])
m1_radius = np.arange(30, 50, .1)

rml_file_name_Laser_Shimadzu_35 = 'Laser_Shimadzu_1200_laminar_real_35mm'
rml_file_name_Laser_Shimadzu_42 = 'Laser_Shimadzu_1200_laminar_real_42mm'
rml_file_name_Laser_Shimadzu_45 = 'Laser_Shimadzu_1200_laminar_real_45mm'

rml_file_name_Laser_Hitachi_35 = 'Laser_Hitachi_1200_blazed_real_35mm'
rml_file_name_Laser_Hitachi_42 = 'Laser_Hitachi_1200_blazed_real_42mm'
rml_file_name_Laser_Hitachi_45 = 'Laser_Hitachi_1200_blazed_real_45mm'


### plotting colors
import matplotlib
import matplotlib.pyplot as plt
# Generate 20 colors from the 'hsv' colormap which resembles a rainbow
colors_rainbow = plt.cm.tab20(np.linspace(0, 2, int(max(1,2))))
# Convert the colors to hex format for easy usage
colors = [matplotlib.colors.rgb2hex(color) for color in colors_rainbow]
colors = ["Red", "Orange", "Green", "Blue", "Indigo", "Violet"]