import folium

# India map create
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Delhi
folium.Marker(
    [28.6139, 77.2090],
    popup="Delhi Population: 19,000,000"
).add_to(m)

# Mumbai
folium.Marker(
    [19.0760, 72.8777],
    popup="Mumbai Population: 20,000,000"
).add_to(m)

# Chennai
folium.Marker(
    [13.0827, 80.2707],
    popup="Chennai Population: 11,000,000"
).add_to(m)

# Andhra Pradesh
folium.Marker(
    [15.9129, 79.7400],
    popup="Andhra Pradesh Population: 53,903,393"
).add_to(m)

# Save map
m.save("india_population_map.html")