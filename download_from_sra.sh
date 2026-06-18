#!/bin/bash
# Job name:
#SBATCH --job-name=download_lichina_metatranscriptome_data
#
# Account:
#SBATCH --account=fc_koskella
#
# Partition:
#SBATCH --partition=savio2_htc
#
# Wall clock limit:
#SBATCH --time=12:00:00
#
## Command(s) to run:
module load python
python download_from_sra.py
