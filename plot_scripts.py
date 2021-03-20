import matplotlib.pyplot as plt

def plot_lat_long(rundf):
    plt.plot(rundf['latitude'], rundf['longitude'])
    plt.show()
