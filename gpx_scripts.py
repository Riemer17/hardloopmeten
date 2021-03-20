from gpx_converter import Converter
import haversine

def gpx_read(file_path):
    rundf = Converter(input_file=file_path).gpx_to_dataframe()
    return rundf

def calculate(rundf):
    dist_dif_hav_2d = [0]
    time_dif = [0]
    dist_hav_no_alt = [0]
    for index, row in rundf.iterrows():
        if index == 0:
            pass
        else:
            start = rundf.iloc[index-1]
            stop = row

            distance_hav_2d = haversine.haversine((start['latitude'], start['longitude']), (stop['latitude'], stop['longitude'])) * 1000
            dist_dif_hav_2d.append(distance_hav_2d)

            dist_hav_no_alt.append(dist_hav_no_alt[-1] + distance_hav_2d)

            time_delta = (stop.time - start.time).total_seconds()
            time_dif.append(time_delta)

    rundf['dist_dif_hav_2d'] = dist_dif_hav_2d
    rundf['dist'] = dist_hav_no_alt
    rundf['time_dif'] = time_dif

    rundf['dist_dif_per_sec'] = rundf['dist_dif_hav_2d'] / rundf['time_dif']
    rundf['spd'] = rundf['dist_dif_per_sec'] * 3.6

    return rundf
