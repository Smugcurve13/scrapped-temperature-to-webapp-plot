import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.txt")
fig = px.line(df,x='date',y='temperature',labels={'x':'Date',
                                                  'y':'Temperature'})
st.plotly_chart(fig)