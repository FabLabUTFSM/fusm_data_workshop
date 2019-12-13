import dash
import pandas as pd
import dash_html_components as html

"""
Cargamos el archivo CSV que creamos a partir de la hoja de cálculo en un
dataframe de Pandas usando la función `read_csv`.
"""
df = pd.read_csv('./datasets/capacitaciones.csv')

"""
En este caso el archivo es presentado tal como se extrajo, algunos tipos
han sido transformados a tipos nativos de Python, como los booleanos y las
fechas, pero no se ha realizado ningún trabajo adicional.
"""
print(df)

"""
Nuestro objetivo es convertir estos datos en información, por lo que tenemos
que aplicar una serie de transformaciones que nos ayuden a presentar lo que
queremos visualizar. Por ejemplo, saber que alguien es mujer no se presenta
correctamente, queremos ser lo más claros con respecto a qué queremos mostrar.
"""

print(df[['Persona', 'Mujer?']])

"""
Nuestra primera transformación será crear una columna de género, utilizando
de base los datos de la columna "Mujer?" para separar entre Hombres y Mujeres.

La función `map()` sobre una serie puede tomar un diccionario o una función que se
aplicará a todos los valores de la serie y devolverá una nueva serie con el
resultado de la operación.
"""

df['Género'] = df['Mujer?'].map({True: 'Mujer', False: 'Hombre'})
print(df[['Persona', 'Género']])

"""
Habiendo creado la categoría, ahora podemos contar la frecuencia de esta
usando la función `value_counts()`.
"""

print(df['Género'].value_counts())

"""
Podemos agrupar por otras categorías simplemente cambiando el parámetro
por sobre el cual estamos agrupando.
"""

print(df['Carrera'].value_counts())

"""
Rápidamente nos damos cuenta de que nuestros datos no son perfectos (ya que
han sido ingresados por humanos). Hay varios casos en donde el nombre de la
carrera ha sido ingresado de formas distintas...
"""

print(df['Carrera'].value_counts().index)

"""
Hay nombres de carrera con un espacio al final y sin un espacio al final, lo
cual hace que nuestras carreras se agrupen inadecuadamente. Para esto, tenemos
que reparar nuestro dataset, podemos hacerlo de forma manual, o en el código.

Preferimos usar una expresión regular para seleccionar todas las carreras que
tenían un espacio al final y lo reemplazamos por nada.
"""

df['Carrera'] = df['Carrera'].str.replace(r'(\s)$', '', regex=True)
print(df['Carrera'].value_counts().index)

"""
Este proceso tiene un problema: no cuenta aquellas entradas que están vacías.
Para ello, hay que modificar el dataframe que se le entrega a la función, para
llenar los espacios vacíos con una categoría común, usando el método `fillna()`:
"""

print(df['Carrera'].fillna('Desconocido').value_counts())

"""
Luego de que tenemos las categorías contadas podemos empezar a ponerlas en un
gráfico, para lo que utilizaremos la librería 'plotly', y para mostrar este
gráfico en la pantalla, usaremos 'dash'.
"""

import plotly.graph_objects as go
import dash_core_components as dcc

"""
Lo prmero que tenemos que hacer es crear una figura, una figura es el
descriptor de un gráfico, que contiene toda su configuración.
"""

generos = df['Género'].value_counts()
torta = go.Pie(values=generos, labels=generos.index)
figura = go.Figure(data=[torta])

"""
Con nuestra figura lista, ahora podemos crear un gráfico. El gráfico controla
cómo se ve nuestra figura en la pantalla.
"""

grafico_generos = dcc.Graph(figure=figura)

"""
Finalmente, para incorporar el gráfico a la página, lo agregamos a la lista de
hijos de la estructura de nuestra página.
"""
hijos = [grafico_generos]

"""
Podemos escribir una función general que genere estos gráficos por nosotros,
que tome una serie y devuelva un gráfico.
"""

def crear_torta(serie_con_categorias, titulo=None):
    valores = serie_con_categorias.fillna('Desconocido').value_counts()
    torta = go.Pie(values=valores, labels=valores.index, title=valores.name if not titulo else titulo)
    figura = go.Figure(data=[torta])
    return dcc.Graph(figure=figura)

"""
y luego podemos usar esta figura para crear todos los otros gráficos
"""

hijos.append(crear_torta(df['Carrera']))
hijos.append(crear_torta(df['Actividad']))

app = dash.Dash(__name__)
app.layout = html.Div(hijos)

if __name__ == "__main__":
    app.run_server(debug=True)