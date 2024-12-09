import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import pandas as pd
from datetime import datetime


# Add custom CSS
st.markdown(
    """
    <style>
    .block-container {
        max-width: 80rem;  /* Adjust the width as needed */
        padding-left: 2rem;  /* Optional: Add padding to the left */
        padding-right: 2rem; /* Optional: Add padding to the right */
        padding-top: 1em;   /* Optional: Add padding to the top */
    }
    .safety-box {
        display: flex;
        align-items: center;
        font-size: 1.2em;
        margin-top: 1em;
        padding: 0.5em;
        border-radius: 0.5em;
    }
    .safe { background-color: #4CAF50; color: white; }  /* Green */
    .warning { background-color: #FFC107; color: black; }  /* Yellow */
    .danger { background-color: #F44336; color: white; }  /* Red */
    </style>
    """,
    unsafe_allow_html=True,
)

# Lebanese cities and their coordinates
cities = {
    "Beirut": [33.8938, 35.5018],
    "Tripoli": [34.4367, 35.8497],
    "Sidon": [33.5606, 35.3758],
    "Zahle": [33.8509, 35.9043],
    "Tyre": [33.2737, 35.2033],
    "Byblos": [34.1214, 35.6488],
    "Baalbek": [34.0058, 36.2181],
    "Jounieh": [33.9808, 35.6178],
    "Nabatiye": [33.3789, 35.4839],
    "Aley": [33.8053, 35.6000],
    "Bcharré": [34.2508, 36.0106],
    "Batroun": [34.2553, 35.6581],
    "Jezzine": [33.5411, 35.5847],
    "Marjayoun": [33.3617, 35.5917],
    "Halba": [34.5450, 36.0817],
    "Bint Jbeil": [33.1172, 35.4322],
    "Rachaiya": [33.5000, 35.8500],
    "Zgharta": [34.3964, 35.8947],
    "Amioun": [34.3564, 35.9403],
    "Beit ed-Dine": [33.6947, 35.5806],
    "Hasbaya": [33.3989, 35.6847],
    "Hermel": [34.3950, 36.3850],
    "Broummana": [33.8711, 35.5875],
    "Deir el Qamar": [33.6972, 35.5656],
    "Baskinta": [33.9333, 35.8000],
    "Ehden": [34.3000, 35.9833],
    "Faqra": [33.9708, 35.8333],
    "Jbeil": [34.1211, 35.6481],
    "Kfardebian": [33.9933, 35.8333],
    "Mtein": [33.8889, 35.7500],
    "Qana": [33.2092, 35.2992],
    "Sarafand": [33.4495, 35.2995],
    "Bourj Hammoud": [33.8936, 35.5403],
    "El Mina": [34.4372, 35.8133],
    "Baalchmay": [33.8000, 35.6000],
    "Barouk": [33.6944, 35.6850],
    "Bhamdoun": [33.8000, 35.6167],
    "Douma": [34.2333, 35.8500],
    "Fanar": [33.8889, 35.5667],
    "Hammana": [33.8253, 35.7333],
    "Jeita": [33.9500, 35.6500],
    "Kousba": [34.3500, 35.9000],
    "Maaser el Shouf": [33.6667, 35.6667],
    "Qoubaiyat": [34.5500, 36.2667],
    "Ras Baalbek": [34.2667, 36.4167],
    "Tannourine": [34.2000, 35.9000],
    "Yammouneh": [34.1000, 36.0000]
}


# Sidebar for user inputs
with st.sidebar:
    st.header("Destination")
    start_city = st.selectbox("Select Starting City:", cities.keys(), key="start")
    end_city = st.selectbox("Select Destination City:", cities.keys(), key="end")

# Load the conflict data
conflict_data_path = "Filtered_Data.csv" 
data = pd.read_csv(conflict_data_path)

# Filter data based on criteria
filtered_data = data[
    (data["country"] == "Lebanon") &
    (pd.to_datetime(data["event_date"]) >= datetime(2023, 10, 7)) &
    (pd.to_datetime(data["event_date"]) <= datetime(2024, 10, 11)) &
    (data["event_type"].isin(["Battles", "Explosions/Remote violence"])) &
    (data["actor1"].isin([
        "Military Forces of Israel (2022-)",
        "Military Forces of Israel (2022-) Mossad",
        "Military Forces of Israel (2022-) Special Forces"
    ])) &
    (data["actor2"].isin([
        "Civilians (Lebanon)",
        "Civilians (Palestine)",
        "Civilians (Syria)",
        "Hezbollah"
    ]))
]

# Function to calculate safety factor
def calculate_safety(start_city, end_city, conflict_data):
    start_conflicts = conflict_data[conflict_data["admin2"] == start_city].shape[0]
    end_conflicts = conflict_data[conflict_data["admin2"] == end_city].shape[0]
    total_conflicts = start_conflicts + end_conflicts

    if total_conflicts == 0:
        return "Safe", "safe" 
    elif total_conflicts <= 5:
        return "Warning", "warning"  
    else:
        return "Dangerous", "danger"  

# Main section
st.title("A Conflict-Aware Journey Through Lebanon")

# Calculate and display safety factor in the sidebar
if start_city != end_city:
    safety_text, safety_class = calculate_safety(start_city, end_city, filtered_data)
    with st.sidebar:
        st.markdown(
            f"""
            <div class="safety-box {safety_class}">
                Safety Factor: <strong>{safety_text}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )
else:
    st.warning("Please select two different cities to calculate a route.")

# Create the default map centered on Lebanon
lebanon_map = folium.Map(location=[33.8938, 35.5018], zoom_start=8)

# Add markers for filtered conflict events
marker_bounds = []  
for _, row in filtered_data.iterrows():
    marker_location = [row["latitude"], row["longitude"]]
    marker_bounds.append(marker_location) 
    fatalities = row["fatalities"]
    folium.CircleMarker(
        location=marker_location,
        radius=3, 
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.7,
        tooltip=(
            f"Date: {row['event_date']}<br>"
            f"Event: {row['event_type']} ({row['sub_event_type']})<br>"
            f"Actors: {row['actor1']} vs {row['actor2']}<br>"
            f"Fatalities: {fatalities}"
        )
    ).add_to(lebanon_map)

# Auto-fit map bounds to include all markers
if marker_bounds:
    lebanon_map.fit_bounds(marker_bounds)

# Check if the selected cities are different for routing
if start_city != end_city:
    start_coords = cities[start_city]
    end_coords = cities[end_city]

    # Call OpenRouteService API for routing
    ORS_API_KEY = "5b3ce3597851110001cf624879bb225755684f93a55db265edbf4603"
    ors_url = "https://api.openrouteservice.org/v2/directions/driving-car"
    params = {
        "api_key": ORS_API_KEY,
        "start": f"{start_coords[1]},{start_coords[0]}",
        "end": f"{end_coords[1]},{end_coords[0]}"
    }

    response = requests.get(ors_url, params=params)

    if response.status_code == 200:
        data = response.json()

        if "features" in data and len(data["features"]) > 0:
            route_geometry = data["features"][0]["geometry"]["coordinates"]
            route_coords = [[coord[1], coord[0]] for coord in route_geometry]  

            folium.Marker(
                location=start_coords,
                tooltip=start_city,
                icon=folium.Icon(color="green", icon="play"),
            ).add_to(lebanon_map)
            folium.Marker(
                location=end_coords,
                tooltip=end_city,
                icon=folium.Icon(color="red", icon="stop"),
            ).add_to(lebanon_map)

            folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.8).add_to(lebanon_map)

# Display the map
st_folium(lebanon_map, width=1200, height=800)
