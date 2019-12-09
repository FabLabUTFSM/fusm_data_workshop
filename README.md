# Workshop de Visualización de Datos

Pablo Albornoz  
13 de Diciembre de 2019  
FabLab UTFSM

## Requisitos

* Python 3.7 o superior

## Instalación

Clonar o descargar el repositorio, ingresar en la carpeta y crear un entorno virtual:

```
cd fusm_data_workshop
python -m venv .
```

Activar el entorno virtual en Windows 

```
.\Scripts\activate.bat
```

Activar el entorno virtual en MacOS y Linux

```
source ./bin/activate
```

Luego:

```
pip install -r requirements.txt
```

Si tiene instaladas varias versiones de Python, ocupe los ejecutables adecuados para `python` y `pip` (ej, `pip3` para python 3)

## Uso del programa

para lanzar el servicio, active el entorno virtual si no lo ha hecho antes y ejecute el archivo `app.py`

```
./Scripts/activate.bat
python app.py
``` 

## Sobre el repositorio

La rama `master` contiene la aplicación terminada mientras que hay una rama para cada parte del desarrollo. 

* `parte-1`: Estado inicial del repositorio
* `parte-2`: Leyendo y transformando el conjunto de datos con Pandas
* `parte-3`: Seleccionando por categoría
* `parte-4`: Dibujando el gráfico con Plotly

Para cambiar de rama utilice `git checkout`:

```
git checkout -f parte-1
```

Utilizar el flag `-f` borrará cualquier cambio que haya hecho a los archivos del repositorio.

