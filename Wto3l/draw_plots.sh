#rm slurm/*
#sbatch make_plots.sbatch
#squeue -u nikmenendez
rm -r output/*
loop plot_Wto3l_2017_cfg.py
sumup plot_Wto3l_2017_cfg.py