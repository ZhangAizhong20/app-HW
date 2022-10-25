import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('California Housing Data(1990)')
data = pd.read_csv('housing.csv')
max_value_housing = int(data['median_house_value'].max())
silder_value = st.slider('Minimal Median House Price',min_value=0,max_value=max_value_housing)
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    list(data['ocean_proximity'].unique()),
    list(data['ocean_proximity'].unique())
)
slect_filter = st.sidebar.radio('choose income level',['Low','Medium','High'])
data2 = data[data['median_house_value']<=silder_value]
data1 = data2.copy()
data1 = data1[data1['ocean_proximity'].isin(location_filter)]
if slect_filter == 'Low':
    data1 = data1[data1['median_income'] <= 2.5]
if slect_filter == 'High':
    data1 = data1[data1['median_income'] >= 4.5]
if slect_filter == 'Medium':
    data1 = data1[(data1.median_income > 2.5) & (data1.median_income <= 4.5)]
st.map(data1)


st.subheader('See more in the figure')
fig , ax = plt.subplots(figsize=(30, 20))
data2['median_house_value'].hist(bins=30)
st.pyplot(fig)
