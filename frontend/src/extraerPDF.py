import pdfplumber
import json
import os

def extraerPDF():
    ruta_data = '../data/'
    # Asegúrate de que el nombre del archivo coincida con el tuyo
    path_pdf = os.path.join(ruta_data, 'fuente_pdf_norteamerica_asia (1).pdf')
    
    lista_final_jugadores = []
    # Definimos las cabeceras manualmente para que no cambien entre páginas
    # Las ponemos con la primera letra en Mayúscula para que coincidan con tus otros archivos
    cabeceras_fijas = ["Nombre", "Seleccion", "Posicion", "Edad", "Goles"]
    
    print(f"Leyendo PDF desde: {path_pdf}")

    try:
        with pdfplumber.open(path_pdf) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    for row in table:
                        # Limpiamos la fila de saltos de línea y comillas
                        fila_limpia = [str(celda).replace('\n', '').replace('"', '').strip() for celda in row if celda is not None]
                        
                        # Filtramos: Solo procesamos si la fila NO es el encabezado del PDF 
                        # y si tiene datos (para evitar que los datos de la pág 2 se usen como llaves)
                        if fila_limpia and "Nombre" not in fila_limpia[0]:
                            # Si la fila tiene el mismo número de elementos que nuestras cabeceras
                            if len(fila_limpia) == len(cabeceras_fijas):
                                jugador = {cabeceras_fijas[i]: fila_limpia[i] for i in range(len(cabeceras_fijas))}
                                lista_final_jugadores.append(jugador)

        # Guardar el temporal
        with open('temp_norte_asia.json', 'w', encoding='utf-8') as f:
            json.dump(lista_final_jugadores, f, indent=4, ensure_ascii=False)
            
        print(f"Éxito: Se extrajeron {len(lista_final_jugadores)} jugadores con cabeceras correctas.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extraerPDF()