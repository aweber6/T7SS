T7SS
====
These scripts are used together to determine the whether certain genes of interest are present in various species

##master.ipy
This is the master script to run the remaining scripts in this directory. 
###Input:
  - NCBI nucleotide sequence of species with all genes of interest clearly labeled with gene names (M.tb)  
  - Directory of blast results from blasting all species to be used in analysis with the above NCBI sequence  
  ***File names in blast results directory should match the file names of PROKKA annotation files for the species***  
  - File containing the names of all the genes of interest (one per line)  
  - File containing the last four (or less) letters of the PROKKA annotation file names (one per line)  
  ***last four letters of the prokka annotations should be unique***  
  - groups.txt file of the orthomcl run of all species  

###Output:
  - orthologs : directory of files for each gene of interest containing the orthologous group(s) which correspond to the gene  
  - by_species directory : direcotry of files for each species containing the genes of interest which are present in the species  


##geneToNC.ipy

##searchBlastFiles.ipy

##orthoCodes.ipy

##orthoGeneGroups.ipy

##bySpecies.ipy
 
