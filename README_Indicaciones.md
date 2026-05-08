Nombres: BENAVIDES JUMBO HANSELL STEVEN, ROBLES CAMPOVERDE AARON JESUS

Primer paso clonar el respositorio

git clone https://github.com/PlataformasWeb-P-AA2026/taller05-team01-taller5.git

Ingresar al proyecto

cd taller05

Entrar a la carpeta data

cd frontend/src

Primero lo que debemos hacer es instalar las siguientes librerias con el siguiente comando :

Instalar estas librerias dependencias:
-Pandas
-Beautifulsoup4
-pdfplumber

"pip install pandas beautifulsoup4 pdfplumber"

En este caso se usaria Pandas para el Csv, beautifulsoup4 para el HTML y pdfplumber para extaer las tablas del PDFs.

Paso 2:
Crear un Script que nos permita extraer y unificar los archivos, en este caso sacamos cada script para cada archivo de manera que nos de como resultado tres archivos Json, por cada documento.


En el archivo HTML usamos la libreria BeautifulSoup para enontrar la tabla y convertir las filas en diccionarios.

#### 2.1 Extraer datos del HTML (Europa)
```bash
python extraerHTML.py
```

En el archivo CSV usamos Pandas para leer mas facil el CSV.


#### 2.2 Extraer datos del CSV (Sudamérica)
```bash
python extraerCSV.py
```

En el PDF usamos pdfplumber para extraer el texto o las tablas y poder estructuralos.

#### 2.3 Extraer datos del PDF (Norteamérica y Asia)
```bash
python extraerPDF.py
```

Luego de eso los unificamos los tres archivos y lo guardamos en un archivo llamado mundial_2026.json, haciendo el llamado de los tres archivos JSON.

#### 2.4 Unificar todo en `mundial_2026.json`
```bash
python crearJSON_final.py
```

Paso 3:
Cargamos los datos a CouchDB
Creamos una base de Datos en CouchDb llamada jugadores, luego creamos un script en el cual hacemos un POST de manera que se carge el archivo JSON mundial_2026.json
En el cual en la URL se puede modificar el nombre de la base,el puerto y el nombre del archivo al cargar al CouchDb.

Creamos un Script llamado jugadoresPost.py utilizando la libreria request con el siguiente comando

"pip install requests"

Para hacer el POST es decir la carga de datos utilizamos el siguiente comando :

```bash
python jugadoresPost.py
```
Paso 4:
 Las vistas se crean dentro del Design Document `losjugadores` con los siguientes índices:
 Club,Partidos,Goles.

 Paso 5:

 Levantar el frontend con Vite

 Entrar a la carpeta frontend

 cd frontend

 ```bash
npm install
npm run dev
```

Verficar en el localHost

"http://localhost:5173"


