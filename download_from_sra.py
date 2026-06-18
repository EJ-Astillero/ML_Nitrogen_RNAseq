import subprocess

# list all run IDs in the Lichina pygmaea metatranscriptome dataset
sra_numbers = ['SRR24154940',
                'SRR24154939',
                'SRR24154938',
                'SRR24154937',
                'SRR24154936',
                'SRR24154935',
                'SRR24154934',
                'SRR24154933',
                'SRR24154932',
                'SRR24154931',
                'SRR24154930',
                'SRR24154929']

# for each run, fetch the .sra file from NCBI
for sra_id in sra_numbers:
    print('Downloading ' + sra_id + ' ... ')
    subprocess.run(['prefetch', sra_id])
    print('... done!\n')

# extract the .sra files from above into a folder named 'fastq'
for sra_id in sra_numbers:
    print ("Generating fastq for " + sra_id + ' ... ')
    outdir = '/global/scratch/users/nikodarcimaher/fastq_lichina_metatranscriptome'
    infile = '/global/scratch/users/nikodarcimaher/sra/' + sra_id + '.sra'
    subprocess.run(['fastq-dump', 
                    '--outdir', outdir,
                    '--gzip', 
                    '--skip-technical',
                    '--readids',
                    '--read-filter', 'pass',
                    '--dumpbase',
                    '--split-3',
                    '--clip',
                    infile])
    print('... done!\n')
