import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

with st.sidebar:
    st.header('Карта города')
    st.header('Статистические показатели')
    st.header('Источники данных')

st.title('Карта города')
st.header('Информационно-аналитический модуль города тюмени', divider= 'blue')

col1, col2 = st.columns([3,1])

with col1:
    st.subheader("Карта города")
    m = folium.Map(location= (57.153, 65.541), zoom_start= 11.2)
    print(st_folium(m, width= 1000, height= 600))

with col2:
    st.subheader("Показатели статистики")