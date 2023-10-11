import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('Top_1000_IMDb_movies_New_version.csv')
    # Clean the 'Votes' column and convert it to integer
    data['Votes'] = data['Votes'].str.replace(',', '').astype(int)
    # Convert 'Year of Release' to integer
    data['Year of Release'] = pd.to_numeric(data['Year of Release'], errors='coerce')
    return data

data = load_data()

# Title
st.title("IMDb Top 1000 Movies Exploration")

# Introduction
st.write("""
Explore the top 1000 movies according to IMDb. 
Use the side panel to interact with the visualizations below!

**Note:**
- The first slider 'Year of release' will make changes to the first visualization (Distribution of IMDb Ratings).
- The second slider 'IMDb Rating range' will make changes to the second visualization (IMDb Rating vs Metascore).
""")  

# Sidebar
st.sidebar.header('Interactive Features')

# Visualization 1: Histogram of IMDb Ratings
st.subheader("Distribution of IMDb Ratings")
st.write("""
This histogram shows the distribution of IMDb ratings across movies in the dataset.
The x-axis represents IMDb ratings, while the y-axis shows the frequency of movies for each rating.
Use the 'Year of release' slider to observe how the distribution changes over selected years.
""")

# Interactive Feature 1: Filter based on year
year_to_filter = st.sidebar.slider('Year of release', int(data['Year of Release'].min()), int(data['Year of Release'].max()), (int(data['Year of Release'].min()), int(data['Year of Release'].max())))

# Filter the data
filtered_data = data[(data['Year of Release'] >= year_to_filter[0]) & (data['Year of Release'] <= year_to_filter[1])]

# Plot using Plotly Express
fig1 = px.histogram(filtered_data, x='Movie Rating', nbins=30, title='Distribution of IMDb Ratings')
fig1.update_xaxes(title='IMDb Rating')
fig1.update_yaxes(title='Frequency')
st.plotly_chart(fig1)

# Visualization 2: Scatter plot of IMDb Rating vs Metascore
st.subheader("IMDb Rating vs Metascore")
st.write("""
The scatter plot below shows the relationship between IMDb ratings and Metascores across movies in the dataset.
The x-axis indicates the IMDb rating, while the y-axis denotes the Metascore.
Use the 'IMDb Rating range' slider to explore patterns within specific rating ranges.
""")

# Interactive Feature 2: Select a range of IMDb ratings to visualize
rating_range = st.sidebar.slider('IMDb Rating range', float(data['Movie Rating'].min()), float(data['Movie Rating'].max()), (float(data['Movie Rating'].min()), float(data['Movie Rating'].max())))

# Filter the data
filtered_data_2 = data[(data['Movie Rating'] >= rating_range[0]) & (data['Movie Rating'] <= rating_range[1])]

# Plot using Plotly Express
fig2 = px.scatter(filtered_data_2, x='Movie Rating', y='Metascore of movie', title='IMDb Rating vs Metascore')
fig2.update_xaxes(title='IMDb Rating')
fig2.update_yaxes(title='Metascore')
st.plotly_chart(fig2)
