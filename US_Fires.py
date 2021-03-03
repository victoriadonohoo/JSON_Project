import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fire_data.json", "w")

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

fire_data = json.load(infile)

print(fire_data["longitude"]["latitude"]["brightness"])

list_of_fires = fire_data["latitude", "longitude", "brightness"]

lons, lats, brights = [], [], []

for fire in list_of_fires:
    lon = fire["longitude"]
    lat = fire["latitude"]
    bright = fire["brightness"]
    lons.append(lon)
    lats.append(lat)
    brights.append(bright)

print(lons[:10])
print(lats[:10])
print(brights[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "brightness": brights,
        "marker": {
            "size": [brightness for brightness in fire_data if brightness > 450],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]


my_layout = Layout(title="US Fires")
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="USFires.html")
