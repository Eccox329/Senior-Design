import pandas as pd
from geopy.distance import geodesic
from tabulate import tabulate
import matplotlib.pyplot as plt
import folium
from matplotlib.patches import Ellipse
import random

mainAED = pd.read_csv('https://raw.githubusercontent.com/Eccox329/Senior-Design/main/AllMainAEDPoints_Excel.csv')


def generate_random_point(lat_min, lat_max, lon_min, lon_max):
    """
    Generates a random point within the specified latitude and longitude bounds.
    
    Parameters:
    lat_min (float): Minimum latitude
    lat_max (float): Maximum latitude
    lon_min (float): Minimum longitude
    lon_max (float): Maximum longitude
    
    Returns:
    tuple: (latitude, longitude) of the random point
    """
    lat = random.uniform(lat_min, lat_max)
    lon = random.uniform(lon_min, lon_max)
    return lat, lon

# NC State Main Campus bounds
lat_min = 35.781839  # minimum latitude
lat_max = 35.789152  # maximum latitude
lon_min = -78.681110  # minimum longitude
lon_max = -78.662734

  # maximum longitude

# Generate random point within these bounds
random_lat, random_lon = generate_random_point(lat_min, lat_max, lon_min, lon_max)

# Print the random point
print(f"Random point: Latitude: {random_lat}, Longitude: {random_lon}")

#Take in found lat, long
user_lat = random_lat
user_lon = random_lon
user_location = (user_lat, user_lon)

# Function to compute the distance
def calculate_distance(row):
    point_location = (row['Y'], row['X'])  # Assuming Y is Latitude and X is Longitude
    return geodesic(user_location, point_location).miles  # Change to .kilometers if needed

# Apply the function to all rows
mainAED['Distance'] = mainAED.apply(calculate_distance, axis=1)

# Find the closest point
closest_point = mainAED.loc[mainAED['Distance'].idxmin()]

# Display the result
print("\nClosest AED Location:")
print(closest_point[['X', 'Y','Distance', 'BLDG_Name', 'Location']])  # Modify this to include other relevant columns

# # Add BLDG_Name labels to each point
# for i, row in mainAED.iterrows():
#     plt.text(row['X'], row['Y'], row['BLDG_Name'], fontsize=8, ha='right', va='bottom', color='red')

# for index, row in mainAED.iterrows():
#        # Define radii for longitude (width) and latitude (height)
#        radius_lon = 0.001373626374
#        radius_lat = 0.001086956522
#        # Create an Ellipse instead of Circle
#        ellipse = Ellipse((row['X'], row['Y']), width=radius_lon, height=radius_lat, color='red', fill=False)
#        plt.gca().add_patch(ellipse)

# User inputs their current location
# user_lat = float(input("Enter your Latitude: "))
# user_lon = float(input("Enter your Longitude: "))
# user_location = (user_lat, user_lon)

# #Print the table
# print(tabulate(mainAED, headers='keys', tablefmt='grid'))
# Plot the latitude (Y) vs longitude (X)
# plt.figure(figsize=(30, 15))  # Set figure size
# plt.scatter(mainAED['X'], mainAED['Y'], color='blue', alpha=0.6, edgecolors='black')

# Show the plot
#plt.show()