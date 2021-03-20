import gpx_scripts
import plot_scripts

rundf = gpx_scripts.gpx_read('gpx_files/Heuvelloopjes_Amsterdamse_bos.gpx')
plot_scripts.plot_lat_long(rundf)