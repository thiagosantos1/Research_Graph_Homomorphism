import random
import sys
import os # to get full directory

# program to create a random bipirtite graph, with N vertices
# in the promp, the user defines N, as well the percentage of vertices in the left of graph

def make_rand_bip_graph(num_vertices, perc_left_of_g, output_name):

	# to save in the octave folder
	sub_path = "/../../LP_LORA/bin/version_1/" # to save the file in the LP folder automatic
	abs_path = os.getcwd()
	path = abs_path + sub_path + output_name + ".mat"

	try:
		list_output = open(output_name+".txt", 'w')
		list_output_octave = open(path, 'w')
	except IOError as exc:
		print("Failure opening file " + str(output_name) + " to write")
		sys.exit(2)

	if perc_left_of_g > 1: # it meas the user enter in % (like 50%)
		perc_left_of_g /=100

	num_vert_left = int(num_vertices * perc_left_of_g)
	num_vert_right = num_vertices - num_vert_left

	left_of_g = [x for x in range(num_vert_left)]
	right_of_g = [x for x in range(num_vert_left,num_vertices)]
	list_output.write(str(num_vertices) + "\n") 
	list_output_octave.write(str(num_vertices) + "\n") 

	for vertice_left in left_of_g:
		rand_num_edges = random.randint(1, num_vert_right)
		edg_list = []
		while len(edg_list) < rand_num_edges: # untill all edges of vertice has not been choosen, keep addind
			index = random.randint(0, num_vert_right-1)
			vertice_right = right_of_g[index]
			if vertice_right not in edg_list:
				edg_list.append(vertice_right)

		edg_list.sort()	

		for edge in edg_list:
			list_output.write(str(vertice_left) + " " + str(edge))
			list_output_octave.write(str(vertice_left) + " " + str(edge))

			if vertice_left != left_of_g[len(left_of_g)-1] or edge != edg_list[len(edg_list)-1]:
				list_output.write("\n")
				list_output_octave.write("\n")


if len(sys.argv) < 4:
  print("Please provide <num_vertices>, <perc_left_of_g in % > & <output_name>\n")
  sys.exit(1)

num_vertices = int(sys.argv[1])
perc_left_of_g = float(sys.argv[2])
output_name = sys.argv[3]

make_rand_bip_graph(num_vertices, perc_left_of_g, output_name)