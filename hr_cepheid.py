import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
star_data = fits.open('asu (2).fit')
sd=star_data[1].data
#print(sd)
abs_mag=sd['Vmag']+5*(np.log10(sd['Plx']/100))
sd_np=np.stack((sd['HIP'],sd['B-V'],sd['Vmag'],sd['Plx'],abs_mag),axis=1)
#print(sd_np)
#sd_np.shape
sd_full=sd_np[(~np.isnan(sd_np)).any(axis=1)]
#print(sd_full)
#sd_full.shape
#print(max(sd_full[:,1]))
#print(min(sd_full[:,4]))
'''
plt.ylim([15,-10])
plt.xlim([-0.5,3])
xpoints = sd_full[:,1]
ypoints = sd_full[:,4]

plt.plot(xpoints, ypoints, '.')
plt.show()
'''

fig, ax = plt.subplots(figsize=(10,12))

ax.set_xlim(-0.5, 3)
ax.set_ylim(15, -10)

ax.set_title('H-R Diagram')

ax.title.set_fontsize(15)
ax.set_xlabel('B-V')
ax.xaxis.label.set_fontsize(15)
ax.set_ylabel('abs_mag')
ax.yaxis.label.set_fontsize(15)

ax.scatter(sd_full[:,1], sd_full[:,4],

           s=2,edgecolors="none",c='k')

ax.tick_params(axis='both', labelsize=14)
plt.show()