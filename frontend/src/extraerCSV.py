import pandas as pd
import json
import os

def extraerCSV():
    ruta_data = '../data/fuente_csv_sudamerica.csv'
    print(f"Leyendo CSV desde: {ruta_data}")
    
    df = pd.read_csv(ruta_data)
    # Convertir a lista de diccionarios
    jugadores = df.to_dict(orient='records')
    
    with open('temp_sudamerica.json', 'w', encoding='utf-8') as f:
        json.dump(jugadores, f, indent=4)
    print("Temporal de Sudamérica generado.")

if __name__ == "__main__":
    extraerCSV()