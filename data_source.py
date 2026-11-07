import streamlit as st
import pandas as pd

st.markdown('# Источники данных')
st.header('Демонстрационные данные', divider= 'gray')

df = pd.DataFrame ({'Источник': ['Росстат', 'Тюменьстат', 'Другие'],
                    'Направление' : ['ЖКХ', 'Социалка', 'Транспорт'],
                    'Ссылки' : ['file1.csv', 'file2.csv', 'file3.csv']})

st.dataframe(df)
