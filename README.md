# Geospatial Proximity Filter
This project provides a Python tool to filter out closely located points in geospatial datasets, using a specified proximity threshold. This is especially useful for reducing redundancy in datasets with densely packed points, such as environmental observations or location-based data points, where multiple nearby points may represent the same or similar information.

## Purpose and Approach
The **Geospatial Proximity Filter** processes datasets containing latitude and longitude coordinates in **decimal** degrees. Using a customizable threshold (in decimal degrees), this filter identifies and removes points that are located within the specified distance of each other, creating a cleaner, more streamlined dataset.

### Input Data Format
The tool expects a CSV file with decimal degree coordinates. The column names for latitude and longitude must be **decimallatitude** and **decimallongitude**, respectively.

### Usage Example
An example usage script is provided in the file main.py. This script demonstrates how to load a dataset in CSV format and apply the Geospatial Proximity Filter with a specified threshold.

## Before and After Filtering Example
Below are visualizations of a dataset before and after applying the Geospatial Proximity Filter. The before image shows the original dataset with multiple nearby points, while the after image shows the dataset with closely located points removed:

![](/Example/Threshold2.png)


## Used versions

python == 3.8.13
numpy == 1.22.4
pandas == 1.5.2
