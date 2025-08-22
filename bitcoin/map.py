import folium


# Create a base map centered on Paris
paris_map = folium.Map(location=[48.8566, 2.3522], zoom_start=13)

# Add some famous places
places = {
    "Eiffel Tower": [48.8584, 2.2945],
    "Louvre Museum": [48.8606, 2.3376],
    "Notre-Dame Cathedral": [48.852968, 2.349902],
    "Arc de Triomphe": [48.8738, 2.2950],
    "Sacré-Cœur Basilica": [48.8867, 2.3431],
}

for place, coords in places.items():
    folium.Marker(location=coords, popup=place, tooltip=place).add_to(paris_map)

# Save to HTML file
paris_map.save("paris_places.html")