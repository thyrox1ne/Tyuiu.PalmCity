import streamlit as st
import folium
from streamlit_folium import st_folium

st.markdown('# Город на ладони')
st.header('Информационно-аналитический модуль города Тюмени\n', divider= 'gray')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric('ЖКХ', 64, -1.8)
with col2:
    st.metric('Транспорт', 40, 4.5)
with col3:
    st.metric('Социалка', 50, 6.9)

col1, col2 = st.columns([4,2])

with col1:
    with st.container(border= True):
        st.header("Карта города")
        m = folium.Map(location= (57.153, 65.591), zoom_start= 11.2)
        st_folium(m, width= 1000, height= 480)

with col2:
    st.header("Показатели статистики")
    st.markdown("### Ключевые показатели по Тюмени:")
    btn_gkh = st.button('ЖКХ')
    btn_transport = st.button('Транспорт')
    btn_social = st.button('Социальная сфера')
    btn_return = st.button('Вернуться к начальной карте')

    if btn_gkh:
        st.markdown('#### Вы выбрали: ЖКХ')
    elif btn_transport:
        st.markdown('#### Вы выбрали: Транспорт')
    elif btn_social:
        st.markdown('#### Вы выбрали: Социальная сфера')
    else:
        st.markdown('#### Вы ничего не выбрали')