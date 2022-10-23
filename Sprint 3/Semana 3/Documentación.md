# Documentación para ejecutables en Python 2 y 3

## Ejecutable en Python 2
Para instalar el ejecutable de NaoService se tiene que instalar primero la libreria `cx-Freeze`
es importante instalar la version correcta, puesto que las ultimas versiones ya no soportan Python 2.7 (ya que esta deprecado)

### Instalar paquete
Para instalar el paquete:
>pip install cx-Freeze==5.1.1

Una vez instalada la dependencia, se tiene que crear un nuevo `.py` llamado `setup.py` donde se ejecutará el codigo para crear el `.exe`:

### Setear el codigo para ejecutable
Codigo en Python3:
```python
import sys from cx_Freeze import setup, Executable 
setup( 
	  name = "myProgram", 
	  version = "0.1", 
	  description = "", 
	  executables = [Executable("myProgram.py")])
```

En este caso se creará un simple ejecutable en Python, sin embargo se puede poner mas opciones para que el ejecutable funcione tanto en windows/mac/linux. 

### Para crear el ejecutable:
> python setup.py build

Resutlados:
Dentro de la carpeta `root` se encontrara la siguiente carpeta: `build`, dentro de esta se encontrará otra carpeta donde estará el .exe

>build/exe.win-amd64-2.7/Main.exe

### Extraer .exe a carpeta principal
Si se quiere quitar las carpetas adiciones es importante copiar todos los files que estan en el mismo lugar que el .exe:
>lib
>Main
>python27.dll


## Ejecutable en Python 3
Para crear el ejecutable en Python 3 es un poco mas complicado, esto debido a que el programa usa mas dependencias. El mayor problema es `MediaPipe` el cual bota error a la hora de realizar el ejecutable.

### Install pyinstaller
Para este ejecutable se necesita instalar `pyinstaller`. Para instalarlo realice el siguiente comando en la terminal.

>pip install pyinstaller

### Verificar si se tiene la url correcta en download_utils.py
Una vez instalado el paquete se tiene que confirmar que el el archivo `download_utils.py` tenga la url correcta. Para esto entre a la carpeta de mediapipe la cual instalo al momento de hacer `pip install mediapipe`. En mi caso se encuentra aquí:

>C:\\Users\\franc\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\mediapipe\\python\\solutions\\download_utils.py

Si dentro del archivo la url no dice `_GCS_RUL_PREFIX = 'https://storage.googleapis.com/mediapipe-assets/'` 
significa que la version de su mediapipe esta desactualizada. De ser el caso es necesario actualizarla a la version `0.8.11`.
_**NOTA:** Si la url es correcta entonces puede pasar al siguiente paso._

### Actualizar Mediapipe
Para actualizar puede: Desinstalar mediapipe y volverlo a instalar o actualizar con `upgrade`.

Version 1:
>pip uninstall mediapipe
>pip install mediapipe

Version 2:
>pip install -U mediapipe== 0.8.11
>

Una vez instalada la ultima versión deberia ser capaz de ver la  url mencionada anteriormente.

### Verificar si se tiene pose_landmark_heavy.tflite
Como ultimo paso, se tiene que verificar que se tenga el archivo `pose_landmark_heavy.tflite` que al momento de tener la ultima versión deberia estar. Para comprobar que la tiene entre a la carpeta `site_package` de python, como ejemplo la mia se encuentra aquí:

>C:\\Users\\franc\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\mediapipe\\modules\\pose_landmark

De no estar el archivo, tiene que instalarlo a mano en [este link]('https://google.github.io/mediapipe/solutions/models.html'). Es importante que descargue el correcto, el cual se encuentra en la subcategoria `Pose`, ahi tiene que descargar el `TFLite model (heavy)`. Una vez instalado pegue el archivo en el path mencionado anteriormente.

### Correr el script para el .exe
Para tener el ejecutable se usa el siguiente comando:

>pyinstaller --onefile main_ui.py --add-data="C:\\Users\\franc\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\mediapipe\\modules;mediapipe/modules" -F -w

Una vez completada la instalación, se crearan dos carpetas `build` y `dist`, la carpetaa build se puede eliminar, y dentro de la dist se encuentra el `.exe`. Puede retirar el .exe de esa carpeta para que este en el root. Además se crea un `.espec` con el mismo nombre queel archivo main, el cual tambien se puede eliminar.
