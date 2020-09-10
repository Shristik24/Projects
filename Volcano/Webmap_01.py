import folium
import pandas

volcano_data=pandas.read_csv("Volcanoes.txt")
latitude=list(volcano_data['LAT'])
longitude=list(volcano_data['LON'])
elevation=list(volcano_data['ELEV'])
name=list(volcano_data['NAME'])

def elev_color(el):
        if (el<=2000):
            return 'green'
        elif (2000<el<4000):
            return 'orange'
        else:
            return 'red'

map=folium.Map(location=[38,-100],zoom_start=5,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")
html="""<b>Volcano information:</b>
        <br><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a></br>
        <br>Elevation: %s m </br>
     """

for lt,ln,el,name in zip(latitude,longitude,elevation,name):
    iframe=folium.IFrame(html=html %(name,name,el),width=200,height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(iframe),radius=6,color=elev_color(el),fill=True,fill_opacity=0.7))

fgp=folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                                        style_function=lambda x: {'fillColor': 'orange' if x['properties']['POP2005']<1000000 
                                        else 'green' if 1000000<=x['properties']['POP2005']<2000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Webmap.html")
