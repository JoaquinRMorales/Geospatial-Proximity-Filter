import numpy as np
from IPython.display import clear_output

def remove_nearby_points(df, threshold=5):
    #Set to avoid duplicates
    points_to_remove = set()  

    #Check every pair of lat-lon
    for p in range(len(df)):
        if p not in points_to_remove:  #Check if the point is already marked for removal
            #Get the lat-lob data
            lat = df['decimallatitude'][p]
            lon = df['decimallongitude'][p]
            
            
            #O(n2) solution -> compare the current lat-lon pait with the rest of not removed points
            for e in range(len(df)):
                #Check if not comparing the row with itself and only consider non-removed points
                if e != p and e not in points_to_remove:  #
                    lat_e = df['decimallatitude'][e]
                    lon_e = df['decimallongitude'][e]

                    #Calculate differences with circular limits
                    lat_diff = min(np.abs(lat - lat_e), 180 - np.abs(lat - lat_e))
                    lon_diff = min(np.abs(lon - lon_e), 360 - np.abs(lon - lon_e))

                    #Check if difference is less and threshold
                    if lat_diff <= threshold and lon_diff <= threshold:
                        points_to_remove.add(e)  # Mark this point for removal
                        
            print(f'{p}/{len(df)-1}')
            clear_output(wait=True)

    # Remove marked points and reset the DataFrame index
    filtered_df = df.drop(points_to_remove).reset_index(drop=True)
    
    return filtered_df