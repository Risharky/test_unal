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
#Importando librerias
import pandas as pd
import numpy as np
import plotly.express as px


st.title(":chart_with_upwards_trend: PRUEBA ANALISTA DE DATOS")
st.markdown("# Dasboard Elaborado por Ricardo Rodriguez Otero #")


#creando horizontal containers
intro= st.container()
fuentedata= st.container()
seriesT=st.container()
EDA_unal=st.container()

#introducción
with intro:
     st.title("EDA")
     st.markdown("Se realiza un análisis de datos en relación a lo solicitado en el punto2 lo cual se encuentra en esta página, en la página ‘Modelo Arima’,  se crearán modelos de series de tiempo usando el paquete AutoTS y Statsmodels de Python.")
     st.markdown(" Para más información [modelos](https://www.statsmodels.org/devel/examples/)")


#data in
with fuentedata:
     st.title(":floppy_disk: Datos")
     st.markdown("Este Dashboard se realiza usando la base de datos de los matriculados en la Universidad Nacional de Colombia por facultad, nivel de estudios, sexo y semestre de ingreso a la Sede Bogotá")
     st.markdown("Estos datos se usaran unicamente para fines laborales y no estan expuestos publicamente, en caso de requerirlos solicitarlos directamente a la Universidad Nacional de Colombia")

#data in
with seriesT:
     st.title("AutoTS")
     st.markdown("La librería autoTS es una librería de Python que permite automatizar la creación de series de tiempo, pero usa a su vez varios paquetes como statsmodels(se utiliza el modelo Arima de esta librería), prophet, sklearn, pytorch-forecasting entre otros. El modelo Arima se utiliza con 3 iteraciones y una validación para dar mayor velocidad a los filtros seleccionados en la pagina del modelo")
     st.markdown(" Para más información [AutoTS](https://github.com/winedarksea/AutoTS)")

#sidebar
st.sidebar.markdown("Desarrollado para fines laborales, se eliminara el dia 31 de agosto o antes en caso de ser requerido ")
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

#introducción
with intro:
     st.title("EDA o Analisis exploratorio de datos")
     #carga de datos
     df= pd.read_excel('dashboard_streamlit/Matriculados pba.xlsx')
     #df=pd.read_csv('Matriculadospba.csv')
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
     st.markdown("Muestra de datos utilizados")
     st.write(df_t.head(10))
     st.write(df_t.info())
     st.markdown("Total de matriculados por facultad seleccione la facultad para mayor detalle")
     st.plotly_chart(px.bar(data_frame=df_t, x="Fecha_c", y="Matriculados", color="Facultad"))
     st.markdown("Distribución de matriculados por Sexo y grado, seleccione el grado para mas detalle")
     st.plotly_chart(px.bar(df_t, x="Sexo", y="Matriculados", color="Grado", title="Distribución de matriculados por Sexo y grado", barmode='group'))
     st.markdown("Distribución de matriculados por Fecha y grado, seleccione el grado para mas detalle")
     st.plotly_chart(px.bar(df_t, x="Fecha_c", y="Matriculados", color="Grado", title="M año", barmode='group'))
     st.markdown("Distribución de matriculados totales por Facultad y sexo, seleccione el sexo para mas detalle")
     st.plotly_chart(px.bar(df_t, x="Facultad", y="Matriculados", color="Sexo", title="Matriculados por sexo", barmode='group'))
     st.markdown("Distribución de matriculados totales por Facultad y grado, seleccione el grado para mas detalle")
     st.plotly_chart(px.bar(df_t, x="Facultad", y="Matriculados", color="Grado", title="Matriculados por Grado", barmode='group'))
     st.markdown("Distribución de matriculados totales por Facultad y sexo, seleccione la facultad para mas detalle")
     st.plotly_chart(px.bar(df_t, x="Sexo", y="Matriculados", color="Facultad", title="Total matriculados por Sexo y por facultad", barmode='group'))
     st.markdown("Distribución de matriculados totales por periodo y sexo, seleccione el periodo que desee vizualizar")
     st.plotly_chart(px.bar(df_t, x="Sexo", y="Matriculados", color="Periodo", title="Distribucion por periodo y sexo"))
     st.markdown("Como análisis preliminar de los datos se observa una mayor proporción de matriculados hombres en el rango de tiempo de 2009 a 2020 pero en las facultades de enfermería y odontología la proporción es inversa donde la mayor cantidad de matriculadas son mujeres.")
     st.markdown("La facultad con la mayor participación de mujeres matriculadas es la facultad de enfermería. ")
     st.markdown("La facultad con la mayor participación de hombres matriculados es la facultad de ingeniería.")
     st.markdown("La facultad más equilibrada en términos de género es la facultad de medicina. ")
     st.markdown("Los matriculados en pregrados en el segundo periodo es el periodo con mayor cantidad de matriculados, con una leve disminución en el primer periodo de cada año, en posgrados se presenta de forma inversa siendo el primer periodo el en el que más se matriculan.")


