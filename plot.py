import matplotlib.pyplot as plt
from gpx_read import rundf

plt.plot(rundf['latitude'], rundf['longitude'])
plt.show()
