import sys
sys.path.append('/home/oskar/Documents/Master/Master_Branch/autosea')
import clutter_maps
import pprint

clutterMap = clutter_maps.GeometricClutterMap(N_min = -500, N_max = 500, E_min = -500, E_max = 500, base_density = 1e-6)

def generate_square_regions(nLength = 20):
	vertices = [clutterMap.N_min, clutterMap.N_min + nLength, clutterMap.E_min, clutterMap.E_min + nLength]
	while vertices[0] < clutterMap.N_max:
		while vertices[2] < clutterMap.E_max:
			region = clutter_maps.SquareRegion(density = clutterMap.base_density, vertices = vertices)
			clutterMap.addRegion(region)
			vertices[2] += nLength
			vertices[3] += nLength
		vertices[0] += nLength
		vertices[1] += nLength
		vertices[2] = clutterMap.E_min
		vertices[2] = clutterMap.E_min + nLength

pprint.pprint(clutterMap.regions)
