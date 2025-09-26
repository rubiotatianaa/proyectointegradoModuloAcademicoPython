import pandas as pd
import plotly.express as px

#HISTORIA UNO: Filtrar materias reprobadas y generar alertas personalizadas.

df_usuarios_simulados = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\usuarios_simulados.csv", sep= ";")

print(df_usuarios_simulados)

df_notas = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\notas.csv", sep=";")

print(df_notas.head())

# Estudiantes reprobados -> generar alerta

reprobados = df_notas[df_notas["notas"] < 3.0]
alertas = reprobados.merge(df_usuarios_simulados, left_on="estudiantes", right_on="nombre", how="left")

alertas["alerta"] = ("⚠️ Alerta: " + alertas["estudiantes"] + " reprobó " + alertas["materias"] + " con nota " + alertas["notas"].astype(str) 
    + ". Contactar a: " + alertas["correo"]
)
print(alertas[["estudiantes", "materias", "notas", "alerta"]])
alertas.to_csv("alertas_reprobados.csv", index=False, encoding="utf-8")

#Promedio anual

promedios = df_notas.groupby(["materias", "semestre"])["notas"].mean().reset_index()

print("Promedios por materia y semestre:")
print(promedios)


#  Grafica con librería plotly
fig = px.line(
    promedios,
    x="semestre",
    y="notas",
    color="materias",
    markers=True,
    title="Evolución de promedios por materia y semestre"
)
fig.show()


