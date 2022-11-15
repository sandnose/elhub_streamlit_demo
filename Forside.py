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
from PIL import Image

# configs
st.set_page_config(layout='wide', page_title='Statistikk fra Elhub', page_icon='bar_chart')
st.title('Statistikk fra Elhub')
st.subheader('''Denne siden vil samlet vise åpen statistikk fra Elhub til markedet. Velg kategori i menyen til venstre. Det er også mulig å laste ned grunnlaget slik at du kan lage dine egne kurver.''')
st.image(Image.open('elhub_logo.png'))

# =============================================================================
# if 'alle' not in st.session_state:
#     st.session_state.alle = True
#     st.session_state.mba = ['NO1', 'NO2', 'NO3', 'NO4', 'NO5']
# 
# # functions
# @st.cache
# def load_data():
#     ''' Add as many sources as you want '''
#     df = pd.read_excel('oversikt-nettap-2022-11-07.xlsx')#, skiprows=[0])
#     return df
# 
# def check_change():
#     if st.session_state.alle:
#         st.session_state.mba = ['NO1', 'NO2', 'NO3', 'NO4', 'NO5']
#     else:
#         st.session_state.mba = []
#     return
# 
# def multi_change():
#     if len(st.session_state.mba) == 5:
#         st.session_state.alle = True
#     else:
#         st.session_state.alle = False
#     return
# 
# mba = st.multiselect('Velg prisområde(r)',
#                      ['NO1', 'NO2', 'NO3', 'NO4', 'NO5'],['NO1', 'NO2', 'NO3', 'NO4', 'NO5'],
#                      help='Viser data for valgt prisområde.', key='mba',
#                      on_change=multi_change)
# 
# all = st.checkbox('Velg alle', key='alle', on_change=check_change)
# 
# # data
# df = load_data()
# 
# # feature engineering
# df_agg = df.groupby(['BRUKSDØGN', 'PRISOMRÅDE']).agg({'Volum (MWh)': 'sum'})
# df_agg = df_agg['Volum (MWh)'].unstack()
# 
# fig_line = px.line(df_agg, x=df_agg.index, y = df_agg.columns[df_agg.columns.isin(mba)])
# fig_line.update_layout(title=f'Produksjon for {mba}',
#                        xaxis_title='Bruksdøgn',
#                        yaxis_title='Volum (MWh)',
#                        legend_title='Prisområde')
# 
# 
# st.plotly_chart(fig_line, use_container_width=True)
# =============================================================================

# dashboards
# st.sidebar.success('Test')
# =============================================================================
# add_sidebar = st.sidebar.selectbox('En random meny', ('Valg1', 'Valg2'))
# 
# if add_sidebar == 'Valg1':
#     st.write('Her vil informasjon tilhørende valg1 være')
#     st.write('Hello, *World!* :sunglasses:')
#     st.plotly_chart(fig_area, use_container_width=True)
# 
# if add_sidebar == 'Valg2':
#     st.write('Her vil informasjon tilhørende valg2 være')
#     st.plotly_chart(fig_line, use_container_width=True)
#     
# =============================================================================



