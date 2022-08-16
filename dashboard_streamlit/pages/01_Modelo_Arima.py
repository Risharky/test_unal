##################################################
## {Description: PRUEBA ANALISTA DE DATOS}
##################################################
## {License_info: Restricted For educational proporses}
##################################################
## Author: {Ricardo Rodriguez Otero}
## Copyright: Copyright {2022}, {}
## Credits: [{credit_list: Fuente de datos Universidad Nacional}]
## License: {Ninguna}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {Unmaintained}
## Email: {contact_email}
## Status: {dev_status: under development}
##################################################

#Importando paquetes
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from autots import AutoTS #permite crear series de tiempo usando librerias segundarias
st.title(":chart_with_upwards_trend: Series de tiempo U.Nal AutoTS Modelo Arima")




df= pd.read_excel('dashboard_streamlit/Matriculados pba.xlsx')
df['Facultad']=df['Facultad'].replace(['C.  Humanas', 'Ingenieria', 'Odontologia'],['C. Humanas', 'Ingeniería', 'Odontología'])
df_t = df.convert_dtypes()
df_t[['Año','Semestre_A']]=df_t['Periodo'].str.split('-', expand=True)
df_t['Fecha']=df_t['Periodo']
df_t['Mes']= df_t['Semestre_A']
df_t['Mes']=df_t['Mes'].map({'1':'1','2':'6'})
df_t['Fecha_c'] = df_t['Año']+'-'+df_t['Mes']
df_t['Fecha_c'] = pd.to_datetime(df_t['Fecha_c'])
df_t["Facultad"] = df_t["Facultad"].astype('category')
df_t["Grado"] = df_t["Grado"].astype('category')
df_t["Matriculados"] = df_t["Matriculados"].astype('int')
df_t["Año"] = df_t["Año"].astype('int')

select_sexo = st.selectbox('Seleccione un sexo: ', options=pd.unique(df_t['Sexo']))
sexo_serie = df_t.loc[df_t['Sexo'] == select_sexo]
select_facultad = st.selectbox('Seleccione una facultad: ', options=pd.unique(sexo_serie['Facultad']))
facultad_serie = sexo_serie.loc[sexo_serie['Facultad'] == select_facultad]
select_grado = st.selectbox('Seleccione un grado: ', options=pd.unique(facultad_serie['Grado']))
grado_serie = facultad_serie.loc[facultad_serie['Grado'] == select_grado]
select_periodo = st.selectbox('Seleccione un periodo: ', options=pd.unique(grado_serie['Semestre_A']))
periodo_serie = facultad_serie.loc[grado_serie['Semestre_A'] == select_periodo]


#sidebar
st.sidebar.markdown("Desarrollado para fines academicos, no use los datos generados para realizar transacciones")
st.sidebar.write(f'''
    <a target="_blank" href="https://risharky.github.io">
        <button>
            Retornar a GH pages de Ricardo Rodriguez Otero
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)
st.sidebar.markdown(" &copy; 2022 &copy;")
