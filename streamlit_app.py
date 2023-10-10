#Import packages necessary to work with csv file and streamlit

import streamlit as st
import pandas as pd
import plotly.express as px


#Importing the CSV file into Python
imdb_movies = "Top_1000_IMDb_movies_New_version.csv"
df = pd.read_csv(imdb_movies)

# Data cleaning
data['Votes'] = data['Votes'].str.replace(',', '').astype(int)
data['Year of Release'] = pd.to_numeric(data['Year of Release'], errors='coerce')
return data

df = load_data()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Title and Introduction
st.title("IMDb Top 1000 Movies Exploration")
st.write("""
Explore the top 1000 movies according to IMDb. 
Use the side panel to interact with the visualizations below!
""")

# Sidebar for interactive features
st.sidebar.header('Interactive Features')

# Visualization 1: Histogram of IMDb Ratings
st.subheader("Distribution of IMDb Ratings")

# Interactive Feature 1: Filter based on year
year_to_filter = st.sidebar.slider('Year of release', int(df['Year of Release'].min()), int(df['Year of Release'].max()), (int(df['Year of Release'].min()), int(df['Year of Release'].max())))

# Filter the data
filtered_data = df[(df['Year of Release'] >= year_to_filter[0]) & (df['Year of Release'] <= year_to_filter[1])]

# Plot using Plotly Express
fig1 = px.histogram(filtered_data, x='Movie Rating', nbins=30, title='Distribution of IMDb Ratings')
fig1.update_xaxes(title='IMDb Rating')
fig1.update_yaxes(title='Frequency')
st.plotly_chart(fig1)

# Visualization 2: Scatter plot of IMDb Rating vs Metascore
st.subheader("IMDb Rating vs Metascore")

# Interactive Feature 2: Select a range of IMDb ratings to visualize
rating_range = st.sidebar.slider('IMDb Rating range', float(df['Movie Rating'].min()), float(df['Movie Rating'].max()), (float(df['Movie Rating'].min()), float(df['Movie Rating'].max())))

# Filter the data
filtered_data_2 = df[(df['Movie Rating'] >= rating_range[0]) & (df['Movie Rating'] <= rating_range[1])]

# Plot using Plotly Express
fig2 = px.scatter(filtered_data_2, x='Movie Rating', y='Metascore of movie', title='IMDb Rating vs Metascore')
fig2.update_xaxes(title='IMDb Rating')
fig2.update_yaxes(title='Metascore')
st.plotly_chart(fig2)
