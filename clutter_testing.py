import sys
sys.path.append('/home/oskar/Documents/Master/Master_Branch/autosea')
from autoseapy import clutter_maps
import pprint
import numpy as np

clutterMap = clutter_maps.GeometricClutterMap(N_min = -500, N_max = 500, E_min = -500, E_max = 500, base_density = 1e-6)

def generate_square_regions(nLength = 20):
	N_min = clutterMap.N_min
	N_max = clutterMap.N_max
	E_min = clutterMap.E_min
	E_max = clutterMap.E_max
	vertices = np.array([[N_min, E_min], [N_min + nLength, E_min], [N_min, E_min + nLength], [N_min + nLength, E_min + nLength]])
	# vertices = [clutterMap.N_min, clutterMap.N_min + nLength, clutterMap.E_min, clutterMap.E_min + nLength]
	while vertices[0][0] < clutterMap.N_max:
		while vertices[0][1] < clutterMap.E_max:
			region = clutter_maps.SquareRegion(density = clutterMap.base_density, vertices = vertices)
			clutterMap.add_region(region)
			for v in vertices:
				v[1] += nLength
		for v in vertices:
				v[0] += nLength
		print(region.area)

generate_square_regions()

pprint.pprint(clutterMap.regions)
pprint.pprint(clutterMap.area)