# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:50:10 2022

@author: christsa
"""
#import xlsxwriter
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime
from io import BytesIO
from scipy import stats

# functions
@st.cache
def load_data():
    ''' Add as many sources as you want '''
    df = pd.read_excel('oversikt-nettap-2022-11-07.xlsx')
    return df
df = load_data()

# page config
st.title('Nettap')
st.write('Her vises nettap og administrativt tap. Alle figurene er basert på tall fra filen du kan laste ned under.')
with open('oversikt-nettap-2022-11-07.xlsx', 'rb') as my_file:
    st.download_button(label = 'Last ned grunnlag', data = my_file, file_name = 'Nettap_alle_prisomr.xlsx', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  

# data engineering
df_gloss = df[['PRISOMRÅDE', 'BRUKSDØGN', 'nettap_d5', 'endring_nettap', 'nåværende_nettap']].set_index(['PRISOMRÅDE', 'BRUKSDØGN'])
df_aloss = df[['PRISOMRÅDE', 'BRUKSDØGN', 'adm_nettap_d5', 'endring_adm_nettap', 'nåværende_adm_nettap']].set_index(['PRISOMRÅDE', 'BRUKSDØGN'])
df_aloss.columns = ['nettap_d5', 'endring_nettap', 'nåværende_nettap']

# Dash - Totalt tap Norge
st.subheader('Totalt tap for hele Norge')
st.info('Klikk på type i "legend" for å aktivere/deaktivere...')
df_loss_norway = pd.concat([df_gloss, df_aloss]).groupby(['BRUKSDØGN']).sum()
fig_loss_norway = px.line(df_loss_norway, x=df_loss_norway.index, y = df_loss_norway.columns)
fig_loss_norway.update_layout(title='Nettap for hele Norge',
                              xaxis_title='Bruksdøgn',
                              yaxis_title='Volum (MWh)',
                              legend_title='Type tap')

st.plotly_chart(fig_loss_norway, use_container_width=True)

# Dash - Tap per MBA
st.subheader('Nåværende tap per MBA')
st.info('Les om prisområder, blabla, *legg til lenke*')
mba = ['NO1', 'NO2', 'NO3', 'NO4', 'NO5']
option = st.selectbox('Velg hvilket "cutoff" du vil se på',
                      ('nettap_d5', 'endring_nettap', 'nåværende_nettap'))
outliers = st.checkbox('Ekskluder ekstremverdier')

if option=='nettap_d5':
    st.write('Nettapsprofilen som ble sendt til eSett ved D+5')
    df_gloss_mba = df_gloss['nettap_d5'].unstack(0)
elif option=='endring_nettap':
    st.write('Endringen som har skjedd mellom avkutting D+5 og nå')
    df_gloss_mba = df_gloss['endring_nettap'].unstack(0)
elif option=='nåværende_nettap':
    st.write('Nettapsprofil som er gjeldende nå')
    df_gloss_mba = df_gloss['nåværende_nettap'].unstack(0)

if outliers:
    zscores = df_gloss_mba.apply(lambda x: x if np.std(x) == 0 else np.abs(stats.zscore(x, nan_policy='omit')))
    df_gloss_mba = df_gloss_mba[zscores<3]
    
fig_line = px.line(df_gloss_mba, x=df_gloss_mba.index, y = df_gloss_mba.columns[df_gloss_mba.columns.isin(mba)])
fig_line.update_layout(title='Nåværende nettap for gitt prisområde',
                       xaxis_title='Bruksdøgn',
                       yaxis_title='Volum (MWh)',
                       legend_title='Prisområde')

st.plotly_chart(fig_line, use_container_width=True)
