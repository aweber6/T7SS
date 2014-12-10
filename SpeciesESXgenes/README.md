T7SS
====
These scripts are used together to determine the whether certain genes of interest are present in various species

##master.ipy
This is the master script to run the remaining scripts in this directory. 
###Input:
- NCBI nucleotide sequence of species with all genes of interest clearly labeled with gene names (M.tb)
- Directory of blast results from blasting all species to be used in analysis with the above NCBI sequence
 _**File names in blast results directory should match the file names of PROKKA annotation files for the species**_
- File containing the names of all the genes of interest (one per line)
- File containing the last four (or less) letters of the PROKKA annotation file names (one per line)
  _**Last four letters of the prokka annotations should be unique**_
- groups.txt file of the orthomcl run of all species

###Output:

- orthologs : directory of files for each gene of interest containing the orthologous group(s) which correspond to the gene
- by_species directory : direcotry of files for each species containing the genes of interest which are present in the species

##geneToNC.ipy
This script takes an NCBI FASTA nucleotide sequence file and a list of genes
and finds the NC numbers corresponding to each of the gene names. These are 
placed into two directories - one containing just the NC number (to be used
in further analysis) and one with both the NC number and the corresponding
gene name (to be used as reference)

##searchBlastFiles.ipy
This script returns files with blast results (for each gene) which correspond 
to supplied NC numbers (directory of files containing NC numbers)

##orthoCodes.ipy
This script convert the blast results into the codes used by orthoMCL
(last for letters of oringinal file name (speices name), followed by
'|', followed by the PROKKA gene code) and places them in a the 
directory ortho_codes

##orthoGeneGroups.ipy
This script takes a directory which has a files for each gene that 
contain the "ortho codes" for the gene. It creates a file for each
gene that contains the orthologous groups that gene in a part of.

##bySpecies.ipy
This script takes orthologous groups sorted by genes and determines what 
genes are present in each species
