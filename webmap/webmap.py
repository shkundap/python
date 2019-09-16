#!/usr/local/bin/python3

import folium
import json
import pandas

VOLCANOS_CSV = "/Users/shruthik/shkundap/git/python/webmap/Volcanoes.txt"
WORLD_JSON = "/Users/shruthik/shkundap/git/python/webmap/world.json"

df = pandas.read_csv(VOLCANOS_CSV)
lat = df['LAT']
long = df['LON']
elv = df['ELEV']

POPUP_HTML = '<div><b>Volcano information:</b></div>Height: %s m'

def getColor(elv):
    if float(elv) < 1000:
        return 'green'
    elif float(elv) >= 1000 and float(elv) < 2000:
        return 'orange'
    else:
        return 'red'

map = folium.Map([38, -98], zoom_start=4.5, tiles="Stamen Terrain")

fgv = folium.FeatureGroup('Volcanos')

for lt, lg, el in zip(lat, long, elv):
    iframe = folium.IFrame(html=POPUP_HTML % str(el), width=180, height=50)
    fgv.add_child(folium.vector_layers.CircleMarker(location=(lt, lg), popup = folium.Popup(iframe), radius=7, fill_color=getColor(el), fill=True, color='grey', fill_opacity=0.7 ))

worldJsonData = json.load(open(WORLD_JSON, 'r', encoding='utf-8-sig'))

geoJson = folium.features.GeoJson(worldJsonData, style_function =lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 5000000 else 'yellow' if 5000000 <= x['properties']['POP2005'] < 10000000 else 'red'})

fgp = folium.FeatureGroup('Population Map')
fgp.add_child(geoJson)

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")
