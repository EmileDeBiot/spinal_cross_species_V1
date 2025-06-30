# Cross species annotation of spinal V1 interneurons

Spinal interneurons' role in motor processes is essential and multiple eletrophysiological studies have been conducted to study their potential roles. Some subtypes have been defined, but never has there been a complete characterization of these interneurons their roles, transcriptomic and morphological profiles. 

This analysis uses cross-species transcriptomics to characterize human spinal V1 interneurons. 


## Download fastq on terminal on the cluster
download: wget command + link
extract: tar -xvf filename

## Compute count matrices
Change the names of the files: folder in folder with the same name + all files from the same sample (see example on the cluster)
Use cell ranger with slurm job: got to jobs, select count_matrix, change the folder name in the script
(if you want to run only one script for multiple samples, you can set up your directories to use the script in that way, you can also run multiple scripts to run in parallel)

## Preprocessing 
Start an interactive R session: adjust RAM depending on what you want to do
Modify the script to preprocess only the new datasets

## Co-integration
Use the cross_species_cointegration file, change the script to add the new samples.

## Cross-species annotation
Use cross_species_annotation notebook to train ML classifiers (don't run all cells, some are hyperparameter tuning, and don't have to be rerun)

## Clustering
Use clustering notebook to generate figures, compute clusters and do marker analysis specific to these clusters.