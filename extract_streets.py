import spacy
import re
import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep
import folium
from folium.plugins import HeatMap
import googlemaps

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key="YOUR_API_KEY")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
geolocator = Nominatim(user_agent="accident-mapper")

# Read accident reports from the cleaned_output.txt file
with open("cleaning_file/cleaned_corpus.txt", "r", encoding="utf-8") as file:
    reports = file.readlines()

def extract_location_details(report):
    """Extract street names and city names from accident reports."""
    doc = nlp(report)
    street, city = None, None

    # Extract named entities
    for ent in doc.ents:
        if ent.label_ == "GPE":  # City name
            city = ent.text
        if ent.label_ == "FAC" or "on " in report:  # Possible street names
            street_match = re.search(r"on ([A-Za-z0-9\s]+?(?: Avenue| Road| Drive| Street| Blvd| Highway| Route| Pkwy| Ln| Ct| Way))", report)
            if street_match:
                street = street_match.group(1)

    return city, street

# Process reports
accident_data = []
for report in reports:
    city, street = extract_location_details(report)
    if city and street:
        accident_data.append({"city": city, "street": street, "report": report.strip()})

# Convert to DataFrame
df_accidents = pd.DataFrame(accident_data)

def get_coordinates(location):
    """Convert street + city to latitude and longitude using Google Maps API."""
    try:
        # Request geocoding information for the location
        geocode_result = gmaps.geocode(f"{location}, California")
        
        # Check if the geocoding result is valid
        if geocode_result:
            lat = geocode_result[0]["geometry"]["location"]["lat"]
            lng = geocode_result[0]["geometry"]["location"]["lng"]
            print(f"Geocoding successful: {location} -> {lat}, {lng}")
            return lat, lng
        else:
            print(f"Geocoding failed for {location}")
    except Exception as e:
        print(f"Geocoding error for {location}: {e}")
    return None, None

# Apply geocoding
df_accidents["Latitude"], df_accidents["Longitude"] = zip(*df_accidents.apply(
    lambda row: get_coordinates(f"{row['street']}, {row['city']}"), axis=1
))

# Save geocoded data
df_accidents.to_csv("geocoded_accidents.csv", index=False)

# Initialize the map
accident_map = folium.Map(location=[33.9533, -117.3961], zoom_start=9)

# Add markers for each accident
for _, row in df_accidents.iterrows():
    if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"Location: {row['street']}, {row['city']}",
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(accident_map)
    else:
        print(f"Skipping marker for {row['street']}, {row['city']} due to invalid coordinates.")

# Add heatmap
heat_data = [
    (row["Latitude"], row["Longitude"]) 
    for _, row in df_accidents.dropna(subset=["Latitude", "Longitude"]).iterrows()
]

if heat_data:
    HeatMap(heat_data).add_to(accident_map)
else:
    print("No valid coordinates for heatmap.")

# Save map
accident_map.save("accident_map.html")
print("Interactive map saved as street_level_accident_map.html!")
