import json

infile = open("US_fires_9_14.json", "r")
outfile = open("readable_fire_data_9_14.json", "w")

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

lons, lats = [], []
brights = []

for fire in fire_data:
    lon = float(fire["longitude"])
    lat = float(fire["latitude"])
    bright = float(fire["brightness"])
    lons.append(lon)
    lats.append(lat)
    if fire["brightness"] > 450:
        bright = fire["brightness"]
        brights.append(bright)


print(lons)
print(lats)
print(brights)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.02 * bright for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]


my_layout = Layout(title="US Fires")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="USFires_9_14.html")
