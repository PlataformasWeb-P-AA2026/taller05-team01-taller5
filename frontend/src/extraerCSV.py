import pandas as pd
import json
import os

def extraerCSV():
    # Ruta relativa para los datos
    ruta_data = '../data/fuente_csv_sudamerica.csv'
    print(f"Leyendo CSV desde: {ruta_data}")
    
    df = pd.read_csv(ruta_data)
    
    # Transformar cabeceras: Poner la primera letra en mayúscula
    df.columns = [col.capitalize() for col in df.columns]

    # Esto transforma todas las columnas numéricas a string
    df = df.astype(str)
    
    # Convertir a lista de diccionarios
    jugadores = df.to_dict(orient='records')
    
    # Guardar el archivo temporal
    with open('temp_sudamerica.json', 'w', encoding='utf-8') as f:
        json.dump(jugadores, f, indent=4, ensure_ascii=False)
        
    print("Temporal de Sudamérica generado. Ahora los números tienen comillas.")

if __name__ == "__main__":
    extraerCSV()