#Import packages necessary to work with csv file and streamlit

import pandas as pd 
import plotly.express as px
import streamlit as st


#Importing the csv file into Python
imdb_movies = "https://github.com/abedbsatt/streamlit/raw/main/Top_1000_IMDb_movies_New_version.csv"
df = pd.read_csv(imdb_movies)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



st.title('IMDB Top 1000 Movies App!')
st.write('This app will display some interactive visualizations regarding the Top 1000 IMDB Movies!')
st.write(df)

average_rating_per_year = df.groupby('Year of Release')['Movie Rating'].mean().reset_index()
fig2 = px.line(average_rating_per_year, x='Year of Release', y='Movie Rating', title='Average Movie Rating Over the Years')
st.plotly_chart(fig2)



fig3 = px.histogram(df, x='Movie Rating', title='Distribution of Movie Ratings', labels={'Movie Rating': 'Movie Rating'}, nbins=20)
st.plotly_chart(fig3)


#Sidebar

st.sidebar.header('User Input Parameters')
year_range = st.sidebar.slider('Year of Release Range', 1980, 2022, (1990, 2020))
rating_range = st.sidebar.slider('Movie Rating Range', 0.0, 10.0, (5.0, 9.0))

# Filter the data according to user inputs
filtered_data = df[(df['Year of Release'].between(year_range[0], year_range[1])) & (df['Movie Rating'].between(rating_range[0], rating_range[1]))]
st.write(filtered_data)

def load_data():
    df['Year of Release'] = pd.to_numeric(df['Year of Release'], errors='coerce')
    df['Movie Rating'] = pd.to_numeric(df['Movie Rating'], errors='coerce')
    df.dropna(subset=['Year of Release', 'Movie Rating'], inplace=True)
    return df


#Scatter Plot Visualization

st.subheader('Scatter Plot: Movie Rating vs Metascore')
fig1 = px.scatter(filtered_data, x='Movie Rating', y='Metascore of movie', labels={'Movie Rating': 'Movie Rating', 'Metascore of movie': 'Metascore'}, hover_data=['Movie Name', 'Year of Release'])
st.plotly_chart(fig1)

#Line Plot Visualization
st.subheader('Line Plot: Average Movie Ratings Over Years')
average_rating_per_year = filtered_data.groupby('Year of Release')['Movie Rating'].mean().reset_index()
fig2 = px.line(average_rating_per_year, x='Year of Release', y='Movie Rating', title='Average Movie Rating Over the Years')
st.plotly_chart(fig2)

