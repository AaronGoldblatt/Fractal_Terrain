
import numpy, noise, random
# NumPy provides the array object for creating a heightmap
# Noise module provides function pnoise2 for generating 2-dimensional Perlin noise

from mayavi import mlab
# Mayavi is a 3d visualization API for python, it will provide the surf function
# which will create a 3d surface map with point heights taken from a heightmap array

base=10
side=2**base+1
# Each side of the array will be 2^n+1 form to allow for cleaner iteration
# 2^10+1=1025, meaning the array has 1050625 indices, the highest number that is still efficient
# on my computer
ref_side=side-1
heightmap=numpy.zeros(shape=(side,side))
# Creates a 2d array of all zeros of our chosen size

def generate():             

	scale = 250.0      
	# This value affects the frequency of the algorithm, the higher it is fewer mountains and bigger are generated
	# the lower it is more mountains are generated that are smaller
	seed = random.randint(0,100)
	# Creates a random seed value for the noise to generate based upon, this allows the terrain to be different each time 
	for i in range(ref_side-1):
		for j in range(ref_side):
			heightmap[i][j]=noise.pnoise2(i/scale, j/scale, octaves=6, lacunarity=10.0, persistence=0.04, base=seed)
			# Iterates through the heightmap making every index into a noise-generated float
			# The parameters affect the roughness and number of the islands
			if(heightmap[i][j]<0): heightmap[i][j]/=4.0
			# If the float is negative, this divides it by four to give the shallow water impression

def main():

	generate()
	xg, yg = numpy.mgrid[-1:1:1j*(side-1),-1:1:1j*(side-1)]
	surf = mlab.surf(xg, yg, heightmap, colormap='terrain', warp_scale='auto')
	# Takes in the heightmap as values for height, using the row and column values as location parameters
	# then uses surf to generate a terrain
	mlab.show()

def show_heightmap():

	print(heightmap)

if __name__=="__main__":
	main()
	show_heightmap()

