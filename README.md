# A Conflict-Aware Journey Through Lebanon

## Reproducibility and Code
This Streamlit application provides an interactive visualization of conflict events in Lebanon, alongside tools to evaluate the safety of travel between cities. The dashboard highlights conflict data, safety indicators, and road routes based on user selections.

[View the Dashboard on Streamlit](https://conflictroute-ad3syfyapdwg7azmubxkvz.streamlit.app/)

---

## Readme

### Introduction
This project examines the ongoing conflict in Lebanon, focusing on events from October 7, 2023, to October 11, 2024. It combines conflict data with route safety evaluations to provide insights into the scale, distribution, and risk levels associated with traveling between Lebanese cities.

The application offers an engaging and user-friendly experience to explore the impacts of conflict while highlighting the safety of selected routes in Lebanon.

---

### Problem to Solve
This application addresses the dual problem of understanding conflict trends and assessing safety for travelers. By analyzing conflict data and linking it to specific locations and routes, it provides:

- A clear understanding of high-risk areas based on conflict activity.
- A visual and interactive "Safety Factor" for routes between major Lebanese cities.

The goal is to enhance situational awareness for users, aid in decision-making, and provide a starting point for further humanitarian or logistical planning.

---

### Data/Operation Design

#### **Data Source**
- **Source**: The Armed Conflict Location & Event Data (ACLED) Project ([ACLED](https://acleddata.com/data/)).
- **Scope**: Filtered for relevant events in Lebanon, focusing on battles and remote violence, and involving key actors such as Hezbollah, Israeli forces, and civilians.

#### **Features**
- **Conflict Data Visualization**:
  - An interactive map displaying conflict events (e.g., battles, explosions) with details on actors, dates, and fatalities.
- **Route Safety Evaluation**:
  - "Safety Factor" feature dynamically evaluates the risk of travel between two user-selected cities, based on the number of conflict events along the route.
- **Routing**:
  - Integration with OpenRouteService API to calculate and visualize road routes between cities.

#### **Technologies**
- **Streamlit**: For building the web app interface.
- **Folium**: For rendering maps and conflict event markers.
- **OpenRouteService API**: For generating road routes between cities.
- **Pandas**: For data cleaning and filtering.
- **gdown**: For downloading large data files dynamically from Google Drive.

#### **Process**
1. Filtered conflict data for Lebanon from October 2023 to October 2024, focusing on battles and remote violence.
2. Mapped Lebanese cities with their latitude and longitude coordinates.
3. Integrated APIs for dynamic routing and visualizations.
4. Added safety evaluation logic based on the number of conflict events per city.

#### **Visualizations**
- **Interactive Map**:
  - Markers for conflict events with details on actors, dates, and fatalities.
  - Road routes between selected cities with an auto-fit view for better navigation.
- **Safety Indicator**:
  - A color-coded "Safety Factor" (green, yellow, red) based on the frequency of conflict events in the selected cities.

---

### How to Use
1. Select a **starting city** and **destination city** from the dropdown menus.
2. View the "Safety Factor" indicator to assess the risk level of the route.
3. Explore the map to see conflict events and road routes between the selected cities.
4. Analyze detailed conflict data and trends through map tooltips.

---

### Future Work
1. **Enhanced Safety Metrics**:
   - Incorporate proximity to conflict events along the route, not just within the cities.
2. **Additional Data Layers**:
   - Overlay humanitarian aid distribution and population displacement data.
3. **Real-Time Data**:
   - Integrate real-time updates to reflect ongoing events and changes in safety conditions.

---

### Acknowledgments
This project is powered by data from ACLED and leverages Streamlit and OpenRouteService for interactive visualizations and route planning.
