# Integración de Datos y CouchDB

**Integrantes:**
- Benavides Jumbo Hansell Steven
- Robles Campoverde Aaron Jesus

---

## Paso 1: Clonar el repositorio

```bash
git clone https://github.com/PlataformasWeb-P-AA2026/taller05-team01-taller5.git
```

Ingresar al proyecto:

```bash
cd taller05-team01-taller5
```

---

## Paso 2: Instalar dependencias de Python

Entrar a la carpeta de los scripts:

```bash
cd frontend/src
```

Instalar las librerías necesarias:

```bash
pip install pandas beautifulsoup4 pdfplumber requests
```

| Librería | Uso |
|----------|-----|
| `pandas` | Leer archivos CSV |
| `beautifulsoup4` | Parsear y extraer tablas del HTML |
| `pdfplumber` | Extraer texto y tablas del PDF |
| `requests` | Cargar el JSON a CouchDB |

---

## Paso 3: Extraer y unificar los datos

Cada script extrae los datos de su fuente y genera un JSON parcial. Al final se unifican en un solo archivo.

### 3.1 Extraer datos del HTML (Europa)

Usamos `BeautifulSoup` para encontrar la tabla y convertir las filas en diccionarios.

```bash
python extraerHTML.py
```

### 3.2 Extraer datos del CSV (Sudamérica)

Usamos `Pandas` para leer y estructurar el CSV fácilmente.

```bash
python extraerCSV.py
```

### 3.3 Extraer datos del PDF (Norteamérica y Asia)

Usamos `pdfplumber` para extraer el texto y las tablas del PDF.

```bash
python extraerPDF.py
```

### 3.4 Unificar en `mundial_2026.json`

Unifica los tres archivos JSON y los guarda en `mundial_2026.json` con el formato requerido por CouchDB.

```bash
python crearJSON_final.py
```

---

## Paso 4: Cargar los datos a CouchDB

Se crea una base de datos en CouchDB llamada `jugadores` y se hace un `POST` con el archivo `mundial_2026.json`.

> En el script `jugadoresPost.py` se puede modificar el nombre de la base, el puerto y el nombre del archivo a cargar.

```bash
python jugadoresPost.py
```

---

## Paso 5: Vistas en CouchDB

Las vistas se crean dentro del Design Document `losjugadores` con los siguientes índices:

| Index name     | Campo que emite |
|----------------|-----------------|
| `por_club`     | `doc.club_actual` |
| `por_goles`    | `doc.goles` |
| `por_partidos` | `doc.partidos` |

Puedes verificarlas en el panel de CouchDB: [http://localhost:5984/_utils](http://localhost:5984/_utils)

---

## Paso 6: Levantar el frontend con Vite

Entrar a la carpeta frontend:

```bash
cd frontend
```

Instalar dependencias e iniciar el servidor:

```bash
npm install
npm run dev
```

Verificar en el navegador:

```
http://localhost:5173
```
