import json

def crearJSON_final():
    archivos = ['temp_europa.json', 'temp_sudamerica.json', 'temp_norte_asia.json']
    todos_los_docs = []

    for archivo in archivos:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                todos_los_docs.extend(data)
        except FileNotFoundError:
            print(f"Error: No se encontró {archivo}. Ejecuta primero los extractores.")

    # Formato final requerido por CouchDB
    resultado_final = {
        "docs": todos_los_docs
    }

    with open('mundial_2026.json', 'w', encoding='utf-8') as f:
        json.dump(resultado_final, f, ensure_ascii=False, indent=4)
    
    print(f"Archivo final 'mundial_2026.json' creado con {len(todos_los_docs)} registros.")

if __name__ == "__main__":
    crearJSON_final()