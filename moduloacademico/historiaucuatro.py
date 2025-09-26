import pandas as pd
import plotly.express as px

df_usuarios_simulados = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\usuarios_simulados.csv", sep= ";")

print(df_usuarios_simulados)

df_notas = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\notas.csv", sep=";")

print(df_notas.head())

#HISTORIA CUATRO: Clasificar estudiantes por riesgo académico con base en múltiples variables.

#Promedio por estudiante
promedios = df_notas.groupby("estudiantes")["notas"].mean().reset_index()
promedios.rename(columns={"notas": "promedio_general"}, inplace=True)

#Materias reprobadas: menor a 3.0
reprobadas = (df_notas[df_notas["notas"] < 3.0].groupby("estudiantes")["materias"].count().reset_index())
reprobadas.rename(columns={"materias": "materias_reprobadas"}, inplace=True)

#datos
df_riesgo = df_usuarios_simulados.merge(promedios, left_on="nombre", right_on="estudiantes", how="left")
df_riesgo = df_riesgo.merge(reprobadas, left_on="nombre", right_on="estudiantes", how="left")

#Se reemplaza valor NaN por 0
df_riesgo["materias_reprobadas"] = df_riesgo["materias_reprobadas"].fillna(0)

#Notas en riesgo
def clasificar_riesgo(row):
    if row["promedio_general"] < 3.0 or row["materias_reprobadas"] >= 2:
        return "Alto"
    else:
        return "Bajo"


df_riesgo["riesgo_academico"] = df_riesgo.apply(clasificar_riesgo, axis=1)

print(df_riesgo[["nombre", "promedio_general", "materias_reprobadas", "riesgo_academico"]])
