import matplotlib.pyplot as plt
import numpy as np

barWidth = 0.45

#samples_p = ['Wp_M4','Wp_M5','Wp_M10','Wp_M15','Wp_M30','Wp_M60']
#samples_m = ['Wm_M4','Wm_M5','Wm_M10','Wm_M15','Wm_M30','Wm_M60']
remaining_p = [3599,3554,6690,11000,21547,39397]
remaining_m = [4026,4569,6101,10201,21524,39945]
eff_p = [x / 50000 for x in remaining_p]
eff_m = [x / 50000 for x in remaining_m]

r1 = np.arange(len(eff_p))
r2 = [x + barWidth for x in r1]

plt.bar(r1,eff_p,barWidth,color='r',edgecolor='w',label='Wp')
plt.bar(r2,eff_m,barWidth,color='b',edgecolor='w',label='Wm')

plt.xlabel('Zp Mass (GeV)', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(len(eff_p))], ['4','5','10','15','30','60'])
plt.ylabel('Selection Efficiency', fontweight='bold')

plt.legend()
#plt.show()
plt.savefig('output/signal/Signal_Selection_Efficiency.png')
