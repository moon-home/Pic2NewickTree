# code to generate pdfs of newick trees from R
library(phytools)
library(ape)

all_trees <- phytools::read.newick(file = "path_to_file_with_newick_strings")

for(i in seq(all_trees)){
  pdf(paste0("newick2pdfR/tree", i, ".pdf"))
  ape::plot.phylo(all_trees[[i]])
  dev.off()
}
