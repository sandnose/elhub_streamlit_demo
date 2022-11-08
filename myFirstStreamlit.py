# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:51:20 2022

@author: christsa
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

# configs
st.set_page_config(layout='wide')

# data
@st.cache
def load_data():
    ''' Add as many sources as you want '''
    df = pd.read_excel('Streamlit\Daglig-produksjon-pr-gruppe-og-prisomrade-MWh.xlsx', skiprows=[0])
    return df

df = load_data()

# feature engineering
df_agg = df.groupby(['Bruksdøgn', 'Prisområde']).agg({'Volum (MWh)': 'sum'})
df_agg = df_agg['Volum (MWh)'].unstack()

fig_area = px.area(df_agg, facet_col='Prisområde', facet_col_wrap=2)
fig_line = px.line(df_agg, x=df_agg.index, y = df_agg.columns,
                   title='en eller annen tittel')

# dashboards
add_sidebar = st.sidebar.selectbox('En random meny', ('Valg1', 'Valg2'))

if add_sidebar == 'Valg1':
    st.write('Her vil informasjon tilhørende valg1 være')
    st.write('Hello, *World!* :sunglasses:')
    st.plotly_chart(fig_area, use_container_width=True)

if add_sidebar == 'Valg2':
    st.write('Her vil informasjon tilhørende valg2 være')
    st.plotly_chart(fig_line, use_container_width=True)
    


