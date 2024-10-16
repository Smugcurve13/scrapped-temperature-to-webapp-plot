import streamlit as st

import plotly.express as px
from read_db import read_db

date,temp = read_db()

fig = px.line(x=date,y=temp,labels={'x':'Date','y':'Temperature'})
st.plotly_chart(fig)