import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


DATA_PATH = Path("../data/processed")
df_summary = pd.read_csv(DATA_PATH / "release_group_summary.csv")
df_top4 = pd.read_csv(DATA_PATH / "top4_artists_by_group.csv")


st.set_page_config(page_title="Spotify ETL Dashboard", layout="wide")
st.title("🎧 Spotify Music Analysis by Release Group")


st.subheader("🎶 Music Characteristics by Release Group")

features = ['avg_bpm', 'avg_danceability', 'avg_valence', 'avg_energy',
            'avg_acousticness', 'avg_instrumentalness', 'avg_liveness', 'avg_speechiness']

selected_feature = st.selectbox("Choose a feature to compare:", features, index=0)

fig1 = px.bar(
    df_summary,
    x='release_group',
    y=selected_feature,
    color='release_group',
    title=f"{selected_feature.replace('_', ' ').title()} by Release Group",
    labels={selected_feature: selected_feature.replace('_', ' ').title(), 'release_group': 'Release Group'},
    template='plotly_white'
)
st.plotly_chart(fig1, use_container_width=True)


st.subheader("🏆 Top 4 Artists per Release Group")

group_options = df_top4["release_group"].unique().tolist()
selected_group = st.selectbox("Select a release group:", group_options, index=0)

top4_filtered = df_top4[df_top4["release_group"] == selected_group]

fig2 = px.bar(
    top4_filtered,
    x='artists_name',
    y='total_streams',
    color='artists_name',
    title=f"Top 4 Artists in {selected_group.title()} Group",
    labels={'artists_name': 'Artist', 'total_streams': 'Total Streams'},
    template='plotly_white'
)
st.plotly_chart(fig2, use_container_width=True)
