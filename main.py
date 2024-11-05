import pandas as pd
from geospatial_proximity_filter.Geospatial_Proximity_Filter import remove_nearby_points

if __name__ == "__main__":
    #Load data from a CSV file
    df = pd.read_csv("data.csv")  

    # Apply the function to remove nearby points
    threshold = 2  # Set the desired threshold
    filtered_df = remove_nearby_points(df, threshold)

    #filtered_df.to_csv("filtered_data.csv", index=False)
