#!/bin/sh
#chmod u+x

ARGC=$#  
BIP=2

EXPECTED_ARGS=4
E_BADARGS=65

if [ $# -lt $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` {argv}. <pair_consistency>, <num_of_partitions>, <isBipartite> & <Loop repetitions G>"
  exit $E_BADARGS
fi

PAIR_FLAG="$1" 
NUM_PART="$2"
isBipartite="$3"
NUM_REP_LOOP="$4"

# make sure to recompile if needed
make

graphs_g=(100 125 150 175 200 225 250 275 300 325 350 375 400 425 450 475 500)


# for each desired size of G
for g_size in "${graphs_g[@]}"
do

  # loop for the fixed H, create different Gs 
  for (( g=1; g<=$NUM_REP_LOOP; g++ ))
	do  # create G 
		if [ $isBipartite -eq 1 ]
	    then
	      python3 create_bip_graph.py $g_size $NUM_PART "graph_g"
	    else
	      python3 create_rand_graph.py $g_size $NUM_PART "graph_g"
	    fi
		
	
		# pre-process data and run list reduction
		make data
		make list

		# run program for continuos
		../bin/./LP_run ../etc/graph_g.txt ../etc/graph_h.txt ../etc/list_cost.txt ../etc/list_homom.txt ../etc/list_pairs.txt $PAIR_FLAG 1
	
		# run program for integral
		../bin/./LP_run ../etc/graph_g.txt ../etc/graph_h.txt ../etc/list_cost.txt ../etc/list_homom.txt ../etc/list_pairs.txt $PAIR_FLAG 2

	done


done







