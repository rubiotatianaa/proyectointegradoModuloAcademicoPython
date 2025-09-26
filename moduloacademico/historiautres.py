import pandas as pd

df_usuarios_simulados = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\usuarios_simulados.csv", sep= ";")

print(df_usuarios_simulados)

df_notas = pd.read_csv(r"C:\Users\rubio\OneDrive\Escritorio\modulo-academico-python\moduloacademico\notas.csv", sep=";")

print(df_notas.head())

#HISTORIA TRES: Agrupar datos por cohorte y generar promedio general anual

# Columna cohorte
df_usuarios_simulados["cohorte"] = pd.to_datetime(df_usuarios_simulados["fecha_registro"], dayfirst = True, errors = "coerce").dt.year

# Estduaintes y notas 
df_merged = df_notas.merge(df_usuarios_simulados[["nombre", "cohorte"]], left_on="estudiantes", right_on="nombre", how="left")

# Promedio General
promedios_cohorte = (df_merged.groupby(["cohorte", "semestre"])["notas"].mean().reset_index())

print("Promedio general anual por cohorte:")
print(promedios_cohorte)
