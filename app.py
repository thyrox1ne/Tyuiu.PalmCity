import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

with st.sidebar:
    st.header('Карта города')
    st.header('Статистические показатели')
    st.header('Источники данных')

st.markdown('# Город на ладони')
st.header('Информационно-аналитический модуль города тюмени', divider= 'blue')

col1, col2 = st.columns([4,2])

with col1:
    st.header("Карта города")
    m = folium.Map(location= (57.153, 65.591), zoom_start= 11.2)
    print(st_folium(m, width= 1000, height= 480))

with col2:
    st.header("Показатели статистики")
    st.markdown("### Ключевые показатели по Тюмени:")
    # statistics = st.radio(label= '', options= ['ЖКХ', 'Транспорт', 'Социальная сфера'],
    #                       index= None, label_visibility="collapsed")
    # if statistics is None:
    #     st.markdown('### Вы ничего не выбрали')
    # else:
    #     st.markdown(f'### Вы выбрали: **{statistics}**')

    btn_gkh = st.button('ЖКХ')
    btn_transport = st.button('Транспорт')
    btn_social = st.button('Социальная сфера')
    btn_return = st.button('Вернуться к начальной карте')

    if btn_gkh:
        st.markdown(f'#### Вы выбрали: ЖКХ')
    elif btn_transport:
        st.markdown(f'#### Вы выбрали: Транспорт')
    elif btn_social:
        st.markdown(f'#### Вы выбрали: Социальная сфера')
    else:
        st.markdown(f'#### Вы ничего не выбрали')