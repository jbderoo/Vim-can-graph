# Problem 11, Biomechanics Hw 3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.integrate import simps

length = 12 # mm
area   = 4 # mm
strain = np.array( [0, .012, .0276, .0492, .06, .0804, .0948, .1068, .1212, .1356, .1584, .1872, .204, .24]) # mm
force  = np.array([0, 80, 184, 328, 400, 496, 576, 628, 688, 736, 764, 788, 796, 804])
stress = force/area # Mega Pascal

area = simps(stress, dx = len(strain))
print('area =', area)
pp  = PdfPages('Desktop/Stress_Strain_Curve.pdf')
fig = plt.figure(1)
ax  = fig.add_subplot(111)
plt.figure(1)
plt.plot(strain, stress, 'r', label= 'Behavior Line')
ax.set_xlabel('Strain')
ax.set_ylabel('Stress (Mega Pascal)')
ax.set_title('Problem 11 Stress Strain Curve')
pp.savefig()
pp.close()
