# indiamap_python_project
# India Map using Python (Folium)

## Project Description

This project creates an interactive map of India using Python.
The map is generated using the Folium library and displayed in an HTML file.
Markers and popups can be added to show different locations in India.

## Features

* Create an interactive India map
* Add markers to locations
* Show popup messages on the map
* Save the map as an HTML file

## Technologies Used

* Python
* Folium
* HTML

## Installation

Install the required library:

pip install folium

## How to Run the Project

1. Create a Python file `indiamap.py`
2. Write the map creation code
3. Run the program:

python indiamap.py

4. Open the generated HTML file in a browser.

## Example Code

```python
import folium

# Create map centered on India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add marker
folium.Marker([28.6139, 77.2090], popup="New Delhi").add_to(m)

# Save map
m.save("indiamap.html")
```

## Output

The program generates an HTML file showing an interactive map of India with markers.

## Author

Prasanna

