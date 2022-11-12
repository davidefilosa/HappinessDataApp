import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('happy.csv')

options = [item.replace('_', ' ').title() for item in df.iloc[:, 2:].columns]
countries = df['country'].unique()
st.header('In Search for Happiness')
st.selectbox('Select a country', options=countries, key='country')
st.selectbox('Select the data for the Y-axis', options=options, key='xaxis')
xaxis = st.session_state['xaxis']
xaxis_columns = xaxis.lower().replace(' ', '_')
st.subheader(f'Happiness vs {xaxis}')
y = df['happiness']
x = df[xaxis_columns]
figure = px.scatter(x=x, y=y, labels={'x': xaxis, 'y': 'Happiness'})
st.plotly_chart(figure)


