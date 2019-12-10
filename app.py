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
usando la función `groupby()` y `count()`.
"""

print(df.groupby('Género').count()['Persona'])

"""
Podemos agrupar por otras categorías simplemente cambiando el parámetro
por sobre el cual estamos agrupando.
"""

print(df.groupby('Carrera').count()['Persona'])

"""
Rápidamente nos damos cuenta de que nuestros datos no son perfectos (ya que
han sido ingresados por humanos). Hay varios casos en donde el nombre de la
carrera ha sido ingresado de formas distintas...
"""

print(df.groupby('Carrera').count().index)

"""
Hay nombres de carrera con un espacio al final y sin un espacio al final, lo
cual hace que nuestras carreras se agrupen inadecuadamente. Para esto, tenemos
que reparar nuestro dataset, podemos hacerlo de forma manual, o en el código.

Preferimos usar una expresión regular para seleccionar todas las carreras que
tenían un espacio al final y lo reemplazamos por nada.
"""

df['Carrera'] = df['Carrera'].str.replace(r'(\s)$', '', regex=True)
print(df.groupby('Carrera').count().index)

app = dash.Dash(__name__)

app.layout = html.Div()

if __name__ == "__main__":
    app.run_server(debug=True)