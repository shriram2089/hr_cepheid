
#importing libraries
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
star_data = fits.open('asu (2).fit')   #creating hdulist
sd=star_data[1].data
#print(sd)
abs_mag=sd['Vmag']+5*(np.log10(sd['Plx']/100))     #calculating abs_mag values
sd_np=np.stack((sd['HIP'],sd['B-V'],sd['Vmag'],sd['Plx'],abs_mag),axis=1)   #creating stack array of required columns
#print(sd_np)
#sd_np.shape
sd_full=sd_np[(~np.isnan(sd_np)).any(axis=1)]     #checking for null entries and removing them if found
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

ax.set_facecolor("white")
ax.scatter(sd_full[:,1], sd_full[:,4],

           s=2,edgecolors="none",c='g')

ax.tick_params(axis='both', labelsize=12)
plt.show()
