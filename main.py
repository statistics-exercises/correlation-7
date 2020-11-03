import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = np.zeros(100), np.zeros(100)
# Your code goes here




# The commands to plot the data 
plt.plot( xdata, ydata, 'bo' )
plt.plot( [-2.6,-2.6], [8,1], 'k-' )
plt.plot( [-2.6,3.9], [8,8], 'k-' )
plt.plot( [-2.6,3.9], [1,1], 'k-' )
plt.plot( [3.9,3.9], [1,8], 'k-' )
plt.savefig('joint_uniform.png')
