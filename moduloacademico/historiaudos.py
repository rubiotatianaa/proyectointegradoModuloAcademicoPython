import pandas as pd 
import plotly.express as px 

df_usuarios_simulados = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\usuarios_simulados.csv", sep= ";")

print(df_usuarios_simulados)

df_notas = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\notas.csv", sep=";")

print(df_notas.head())

#HISTORIA DOS: Agrupar promedios por materia y semestre y graficar su evolución.

# Agrupamos por materia y semestre, calculamos el promedio
promedios = (
    df_notas.groupby(["materias", "semestre"])["notas"].mean().reset_index()
)

print("Promedios por materia y semestre:")
print(promedios)

# Graficar 
fig = px.line(
    promedios,
    x="semestre",
    y="notas",
    color="materias",
    markers=True,
    title="Evolución de promedios por materia y semestre"
)

fig.show()
