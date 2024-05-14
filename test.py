import folium
import streamlit as st


from streamlit_folium import st_folium

option = st.selectbox(
   "Choose One division",
   ("Magway", "Mandalay", "Yangon", "NayPyiTaw"),
   index=None,
   placeholder="Select One to view",
)

if option == "Magway":
    # center on Liberty Bell, add marker
    m = folium.Map(location=[20.15, 94.95], zoom_start=16)
    folium.Marker(
    [20.15, 94.95], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

elif option == "Mandalay":
    m = folium.Map(location=[21.9831, 96.0844], zoom_start=16)
    folium.Marker(
        [21.9831, 96.0844], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

elif option == "Yangon":
    m = folium.Map(location=[16.795, 96.16], zoom_start=16)
    folium.Marker(
        [16.795, 96.16], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

elif option == "NayPyiTaw":
    m = folium.Map(location=[19.7475, 96.115], zoom_start=16)
    folium.Marker(
        [19.7475, 96.115], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)
