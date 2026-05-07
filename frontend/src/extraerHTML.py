import json
import os
from bs4 import BeautifulSoup

def extraerHTML():
    ruta_data = '../data/fuente_html_europa.html'
    print(f"Leyendo HTML desde: {ruta_data}")
    
    with open(ruta_data, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        tabla = soup.find('table')
        headers = [th.text.strip() for th in tabla.find_all('th')]
        
        jugadores = []
        for tr in tabla.find_all('tr')[1:]:
            cells = tr.find_all('td')
            if cells:
                jugador = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
                jugadores.append(jugador)
    
    with open('temp_europa.json', 'w', encoding='utf-8') as f:
        json.dump(jugadores, f, indent=4)
    print("Temporal de Europa generado.")

if __name__ == "__main__":
    extraerHTML()