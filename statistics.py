import streamlit as st

st.markdown('# Статистические показатели')
st.header('Демонстрационные данные', divider= 'gray')

st.markdown("### Выберите направление для просмотра показателей")
col1, col2, col3 = st.columns(3)
with col1:
    btn_gkh = st.button('ЖКХ')
with col2:
    btn_transport = st.button('Транспорт')
with col3:
    btn_social = st.button('Социальная сфера')

col1, col2 = st.columns(2)
if btn_gkh:
    with col1:
        with st.container(border= True):
            st.metric('Аварии на сетях', 124, 'условных случая')
    with col2:
        with st.container(border=True):
            st.metric('Износ сетей', 38, 'условное значение')
elif btn_transport:
    with col1:
        with st.container(border=True):
            st.metric('Аварии на дорогах', 12, 'условных случая')
    with col2:
        with st.container(border=True):
            st.metric('Загруженность', 45, 'условное значение')
elif btn_social:
    with col1:
        with st.container(border=True):
            st.metric('Загруженность детских садов', 95, 'условных случаев')
    with col2:
        with st.container(border=True):
            st.metric('Демография', 62, 'условное значение')
