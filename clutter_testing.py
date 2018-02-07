import sys
sys.path.append('/home/oskar/Documents/Master/Clutter_map_Branch/autosea')
from autoseapy import clutter_maps
import pprint
import numpy as np
import matplotlib.pyplot as plt
import autoseapy.visualization as autovis

clutterMap = clutter_maps.GeometricClutterMap(N_min = -500, N_max = 500, E_min = -500, E_max = 500, base_density = 1e-6)

# pprint.pprint(clutterMap.area)

def generate_square_regions(nLength = 20):
	N_min = clutterMap.N_min
	N_max = clutterMap.N_max
	E_min = clutterMap.E_min
	E_max = clutterMap.E_max
	vertices = np.array([[N_min, E_min], [N_min + nLength, E_min], [N_min + nLength, E_min + nLength], [N_min, E_min + nLength]])
	while vertices[0][0] < clutterMap.N_max:
		while vertices[0][1] < clutterMap.E_max:
			region = clutter_maps.PolygonRegion(density = clutterMap.base_density, vertices = vertices)
			clutterMap.add_region(region)
			vertices[:, 1] += nLength
		vertices[:, 0] += nLength
		vertices[0:1, 1] = E_min
		vertices[2:3, 1] = E_min + nLength

generate_square_regions()

# fig, ax = plt.subplots()

# clutterMap.plot_density_map(ax=ax, im_args= {'color': 'C0'})

# plt.show()

# pprint.pprint(clutterMap.area)