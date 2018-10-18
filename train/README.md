# This is a folder to generate data
The generated data, each entry of them, includes two part:
1. A Newick string that is used to generate the phylogenetic tree.
2. A picture of the generated tree picture.

The generated picture is used as input to train the model, the string is used as the label and ground truth to calculate the error from prediction of the model.

## Constraints and freedom on data
1. All species' names are randomly sampled from a list you can find in file namelist.txt
2. The number of species convered in each phylogenetic tree is sampled from range 10 to 100.
3. There two extremist forms of the tree with a given number of species n. 
    The layers number of the shallowest one will be n_l_min = ceil(log2(n))+1 
    The layers number of the shallowest one will be n_l_max = n for even n and n+1 for odd n
   Then we grow the tree from the root to leafs by randomly choosing if this node should split. 
   A loo
