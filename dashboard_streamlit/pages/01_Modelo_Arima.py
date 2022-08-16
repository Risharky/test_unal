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
sexo_variable = df_t.loc[df_t['Sexo'] == select_sexo]
sexo_variable.reset_index(inplace=True)
select_facultad = st.selectbox('Seleccione una facultad: ', options=pd.unique(sexo_variable['Facultad']))
facultad_variable = sexo_variable.loc[sexo_variable['Facultad'] == select_facultad]
facultad_variable.reset_index(inplace=True)
select_grado = st.selectbox('Seleccione un grado: ', options=pd.unique(facultad_variable['Grado']))
grado_variable = facultad_variable.loc[facultad_variable['Grado'] == select_grado]
select_periodo = st.selectbox('Seleccione un periodo: ', options=pd.unique(grado_variable['Semestre_A']))
periodo_variable = grado_variable.loc[grado_variable['Semestre_A'] == select_periodo]

st.write(periodo_variable.head())

#model_list = ['LastValueNaive', 'GLS', 'GLM', 'ETS', 'AverageValueNaive', 'ARIMA', 'Theta', 'ARDL']
model_list = ['ARIMA']
model = AutoTS(forecast_length=2, frequency='infer', prediction_interval=0.80,
                ensemble='simple', model_list=model_list, transformer_list='fast',
                max_generations=3, num_validations=0)
model = model.fit(periodo_variable, date_col='Fecha_c', value_col='Matriculados', id_col=None)
prediction = model.predict()
forecast = prediction.forecast
st.write(print(model))
st.write(print(forecast))

fig = go.Figure([
    go.Scatter(
        name=(select_facultad.title()+ grado_variable.title()+' ' + select_sexo.title()+' P.'+ select_periodo.title()),
        x=periodo_variable['Fecha_c'],
        y=periodo_variable['Matriculados'],
        mode='lines+markers',
        marker=dict(color='red', size=2),
        showlegend=True
    ),
    go.Scatter(
        name='Pronostico: F.Odontología, pregrado mujeres P.2',
        x=forecast.index,
        y=forecast['Matriculados'],
        mode='lines+markers',
        marker=dict(color='violet', size=2),
        line=dict(width=2),
        showlegend=True
    )
    ])
fig.update_layout(
    yaxis_title='No. Matriculados',
    title='Matriculados facultad de Odontología',
    hovermode="x"
)


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
