import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.txt")
fig = px.line(x=df['date'],y=df['temperature'],labels={'x':'Date',
                                                  'y':'Temperature'})
st.plotly_chart(fig)