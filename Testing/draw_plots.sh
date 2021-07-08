#rm slurm/*
#sbatch make_plots.sbatch
#squeue -u nikmenendez
#rm -r output/*
loop plot_Wto3l_2017_cfg.py
sumup plot_Wto3l_2017_cfg.py
#display output/2017_Data_Driven_Background/mass1.png
#display output/2017_Data_Driven_Background/pTL3.png
#display output/Plots/pTL1.png

