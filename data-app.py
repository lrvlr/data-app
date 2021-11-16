import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# TESTING STREAMLIT")
st.write("Diving into Kaggle [NBA Dataset](https://www.kaggle.com/justinas/nba-players-data) ")
df = pd.read_csv("data/archive.zip", index_col=0).reset_index(drop=True)
st.write(df)

st.header("Histogram")
hist_x = st.selectbox("Histogram variable", options=df.columns, index=df.columns.get_loc("net_rating"))
hist_bins = st.slider(label="Histogram bins", min_value=5, max_value=50, value=25, step=1)
hist_cats = df[hist_x].sort_values().values
hist_fig = px.histogram(df, x=hist_x, nbins=hist_bins, title="Histogram of " + hist_x,
                        template="plotly_white", category_orders={hist_x: hist_cats})
st.write(hist_fig)

st.header("Boxplots")
box_x = st.selectbox("Boxplot variable", options=df.columns, index=df.columns.get_loc("gp"))
box_cat = st.selectbox("Categorical variable", ["age", "season"], 0)
box_fig = px.box(df, x=box_cat, y=box_x, title="Box plot of " + box_x, template="plotly_white", category_orders={})
st.write(box_fig)

st.header("Correlations")

corr_x = st.selectbox("Correlation - X variable", options=df.columns, index=df.columns.get_loc("net_rating"))
corr_y = st.selectbox("Correlation - Y variable", options=df.columns, index=df.columns.get_loc("pts"))
corr_col = st.radio("Correlation - color variable", options=["age", "season"], index=1)
corr_filt = st.selectbox("Filter variable", options=df.columns, index=df.columns.get_loc("net_rating"))
min_filt = st.number_input("Minimum value", value=6, min_value=0)
tmp_df = df[df[corr_filt] > min_filt]

fig = px.scatter(tmp_df, x=corr_x, y=corr_y, template="plotly_white",
                 color=corr_col, hover_data=['player_name', 'age', 'season'],
                 color_continuous_scale=px.colors.sequential.OrRd)

st.write(fig)

st.header("Heatmaps")
hmap_params = st.multiselect("Select parameters to include on heatmap", options=list(df.columns), default=[p for p in df.columns if "fg" in p])
hmap_fig = px.imshow(df[hmap_params].corr())
st.write(hmap_fig)