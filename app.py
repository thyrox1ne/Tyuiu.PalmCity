import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] a span {
        font-size: 22px !important;
        font-weight: 500 !important;
        color: #FBF9F5 !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    </style>
""",
    unsafe_allow_html=True,
)

pages = [
    st.Page('home.py', title= 'Главная'),
    st.Page('statistics.py', title= 'Статистические показатели'),
    st.Page('data_source.py', title= 'Источник данных')
]

pg = st.navigation(pages)
pg.run()

